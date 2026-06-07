import sys
import math
import numpy as np
import keyboard
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QGraphicsPixmapItem,QMainWindow
from PySide6.QtCore import QFile, QIODevice, QPoint, QTimer
from PySide6.QtGui import QColor, QPixmap,QImage, QKeyEvent
from PySide6.QtCore import Qt

from ui import Ui_MainWindow

import util

global app
window = {}
curHwnd = {}

# 每个窗口的独立状态
class WindowState:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.stuck_key_enabled = False
        self.enable_blood_helper = True
        self.enable_magic_helper = True
        self.blood_key = 'R'
        self.magic_key = 'T'
        self.tick_keys = ['A', '', '', '']  # Tick1-4

window_states = {}  # {hwnd: WindowState}


def do_add_magic():
    if not window.EnableMagicHelper.isChecked():
        return
    txt = window.MinMagicKeySelecter.currentText()
    util.alt_press(curHwnd, txt.lower())


def do_add_blood():
    if not window.EnableBloodHelper.isChecked():
        return
    
    print('加血')
    txt = window.MinBloodKeySelecter.currentText()
    util.alt_press(curHwnd, txt.lower())


def do_add_magic_for_hwnd(hwnd, key):
    util.alt_press(hwnd, key.lower())

def do_add_blood_for_hwnd(hwnd, key):
    util.alt_press(hwnd, key.lower())

def timer_exec():
    global curHwnd, window_states
    
    # 为所有窗口执行操作
    for hwnd, state in list(window_states.items()):
        # 获取当前窗口的 UI 元素
        curHwnd[hwnd] = hwnd
        
        # 找血量
        pic = find_blood_pic(hwnd)
        
        # 绘制二值化之后的血条
        if pic:
            qcimg = binary_img(pic.toImage())
            precentage = int(window.MinBloodPrecentageSelecter.currentText()) * 0.01
            position = math.ceil(qcimg.width() * precentage)
            if qcimg.pixelColor(position, 0).red() > 200:
                if state.enable_blood_helper:
                    do_add_blood_for_hwnd(hwnd, state.blood_key)
        
        # 找蓝
        pic = find_magic_pic(hwnd)
        
        # 绘制二值化之后的蓝条
        if pic:
            qcimg = binary_img(pic.toImage())
            position = math.ceil(qcimg.width() * 0.3)
            if qcimg.pixelColor(position, 0).red() > 200:
                if state.enable_magic_helper:
                    do_add_magic_for_hwnd(hwnd, state.magic_key)
        
        # 卡键
        if state.stuck_key_enabled:
            for tick_key in state.tick_keys:
                if tick_key != '':
                    util.press(hwnd, tick_key.lower())
    
    # 更新 UI 显示（当前选中的窗口）
    current_hwnd = curHwnd.get('current')
    if current_hwnd:
        # 显示角色名
        pic = util.grab_image_qt(current_hwnd, util.Position(130, 7), util.Rectangle(90, 15))
        util.show_pix_on_graph_view(window.CurrentRolePicture, pic)
        
        # 显示血量
        pic = find_blood_pic(current_hwnd)
        util.show_pix_on_graph_view(window.CurrentBloodPicture, pic)
        
        # 显示蓝量
        pic = find_magic_pic(current_hwnd)
        util.show_pix_on_graph_view(window.CurrentMagicPicture, pic)


def binary_img(img):
    qcimg = img.copy(0,0,img.width(),1)
    for i in range(0, qcimg.width()):
        for j in range(0, qcimg.height()):
            c = qcimg.pixelColor(i, j)
            rc = binary_color(c)
            qcimg.setPixelColor(QPoint(i, j), rc)
    return qcimg


def binary_color(c):
    r = c.red()
    g = c.green()
    b = c.blue()
    count = r + g + b
    if np.var([r,g,b]) < 100:
        return QColor(255, 255, 255)
    else:
        return QColor(0, 0, 0)

def find_blood_pic(hwnd):
    return util.grab_image_qt(hwnd, util.Position(100, 33), util.Rectangle(118, 15))


def find_magic_pic(hwnd):
    return util.grab_image_qt(hwnd, util.Position(100, 54), util.Rectangle(98, 8))

def on_window_select(idx):
    global curHwnd, window_states
    hwnd = window.WindowSelecter.itemData(idx)
    curHwnd['current'] = hwnd
    
    # 如果这个窗口没有状态，创建一个新的
    if hwnd not in window_states:
        window_states[hwnd] = WindowState(hwnd)
    
    # 从 UI 加载状态到 WindowState
    state = window_states[hwnd]
    state.blood_key = window.MinBloodKeySelecter.currentText()
    state.magic_key = window.MinMagicKeySelecter.currentText()
    state.tick_keys = [
        window.Tick1.currentText(),
        window.Tick2.currentText(),
        window.Tick3.currentText(),
        window.Tick4.currentText()
    ]
    
    # 更新 UI 显示当前窗口的状态
    window.StuckKeyStatus.setChecked(state.stuck_key_enabled)


def save_current_window_state():
    """保存当前 UI 设置到当前窗口的状态"""
    global curHwnd, window_states
    hwnd = curHwnd.get('current')
    if hwnd and hwnd in window_states:
        state = window_states[hwnd]
        state.blood_key = window.MinBloodKeySelecter.currentText()
        state.magic_key = window.MinMagicKeySelecter.currentText()
        state.tick_keys = [
            window.Tick1.currentText(),
            window.Tick2.currentText(),
            window.Tick3.currentText(),
            window.Tick4.currentText()
        ]


def init(main_window):
    # 初始化窗口选择器
    ws = util.find_window('QQ三国')
    for w in ws:
        main_window.WindowSelecter.addItem(w.window_text, w.hwnd)
    on_window_select(0)
    main_window.WindowSelecter.currentIndexChanged.connect(on_window_select)
    
    # 连接 UI 变化事件，保存状态
    main_window.MinBloodKeySelecter.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.MinMagicKeySelecter.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.Tick1.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.Tick2.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.Tick3.currentIndexChanged.connect(lambda: save_current_window_state())
    main_window.Tick4.currentIndexChanged.connect(lambda: save_current_window_state())

    # 初始化卡键复选框
    main_window.StuckKeyStatus.stateChanged.connect(lambda state: on_stuck_key_toggled(state))
    
    # 注册全局快捷键 CTRL+`
    keyboard.add_hotkey('ctrl+`', on_ctrl_backtick_pressed)
    
    # 初始化定时器
    main_window.timer = QTimer()
    main_window.timer.start(300)
    main_window.timer.timeout.connect(timer_exec)


def on_stuck_key_toggled(state):
    global curHwnd, window_states
    hwnd = curHwnd.get('current')
    if hwnd and hwnd in window_states:
        window_states[hwnd].stuck_key_enabled = (state == 2)


def on_ctrl_backtick_pressed():
    global curHwnd, window_states, window
    hwnd = curHwnd.get('current')
    if hwnd and hwnd in window_states:
        window_states[hwnd].stuck_key_enabled = not window_states[hwnd].stuck_key_enabled
        window.StuckKeyStatus.setChecked(window_states[hwnd].stuck_key_enabled)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    window = mainWindow.ui
    init(window)
    sys.exit(app.exec())
