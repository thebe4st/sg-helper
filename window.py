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
stuck_key_enabled = False  # 卡键启用状态


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


def timer_exec():
    global curHwnd
    # 找角色名
    pic = util.grab_image_qt(curHwnd, util.Position(130, 7), util.Rectangle(90, 15))
    util.show_pix_on_graph_view(window.CurrentRolePicture, pic)

    # 找血量
    pic = find_blood_pic(curHwnd)
    util.show_pix_on_graph_view(window.CurrentBloodPicture, pic)

    # 绘制二值化之后的血条
    qcimg = binary_img(pic.toImage())
    precentage = int(window.MinBloodPrecentageSelecter.currentText())* 0.01
    position = math.ceil(qcimg.width() * precentage)
    if qcimg.pixelColor(position, 0).red() > 200:
        do_add_blood()
    # util.show_pix_on_graph_view(window.CurrentBinaryBloodPicture, QPixmap.fromImage(qcimg))

    # 找蓝
    pic = find_magic_pic(curHwnd)
    qimg = pic.toImage()
    util.show_pix_on_graph_view(window.CurrentMagicPicture, pic)

    # 绘制二值化之后的蓝条
    qcimg = binary_img(qimg)
    # util.show_pix_on_graph_view(window.CurrentBinaryMagicPicture, QPixmap.fromImage(qcimg))

    position = math.ceil(qcimg.width() * 0.3)
    if qcimg.pixelColor(position, 0).red() > 200:
        do_add_magic()

    if stuck_key_enabled:
        if window.Tick1.currentText() != '':
            util.press(curHwnd,window.Tick1.currentText().lower())
        if window.Tick2.currentText() != '':
            util.press(curHwnd,window.Tick2.currentText().lower())
        if window.Tick3.currentText() != '':
            util.press(curHwnd,window.Tick3.currentText().lower())
        if window.Tick4.currentText() != '':
            util.press(curHwnd,window.Tick4.currentText().lower())


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
    global curHwnd
    curHwnd = window.WindowSelecter.itemData(idx)


def init(main_window):
    # 初始化窗口选择器
    ws = util.find_window('QQ三国')
    for w in ws:
        main_window.WindowSelecter.addItem(w.window_text, w.hwnd)
    on_window_select(0)
    main_window.WindowSelecter.currentIndexChanged.connect(on_window_select)

    # 初始化卡键复选框
    main_window.StuckKeyStatus.stateChanged.connect(lambda state: on_stuck_key_toggled(state))
    
    # 注册全局快捷键 CTRL+`
    keyboard.add_hotkey('ctrl+`', on_ctrl_backtick_pressed)
    
    # 初始化定时器
    main_window.timer = QTimer()
    main_window.timer.start(300)
    main_window.timer.timeout.connect(timer_exec)


def on_stuck_key_toggled(state):
    global stuck_key_enabled
    stuck_key_enabled = (state == 2)  # 2 = Qt.Checked, 0 = Qt.Unchecked


def on_ctrl_backtick_pressed():
    global stuck_key_enabled, window
    stuck_key_enabled = not stuck_key_enabled
    window.StuckKeyStatus.setChecked(stuck_key_enabled)

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
