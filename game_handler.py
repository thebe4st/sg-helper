import math
import numpy as np
from PySide6.QtCore import QTimer, QPoint
from PySide6.QtGui import QColor, QPixmap, QImage

import util

class GameHandler:
    """游戏逻辑处理器"""
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.window = None
        self.timer = None
        self.refresh_timer = None
    
    def set_window(self, window):
        """设置 UI 窗口引用"""
        self.window = window
    
    def start_timers(self):
        """启动定时器"""
        # 游戏操作定时器（300ms）
        self.timer = QTimer()
        self.timer.start(300)
        self.timer.timeout.connect(self.timer_exec)
        
        # 窗口刷新定时器（3秒）
        self.refresh_timer = QTimer()
        self.refresh_timer.start(3000)
        self.refresh_timer.timeout.connect(self.refresh_windows)
    
    def timer_exec(self):
        """定时器执行的游戏操作"""
        window_states = self.state_manager.get_all_states()
        
        # 为所有窗口执行操作
        for hwnd, state in list(window_states.items()):
            # 找血量
            pic = self.find_blood_pic(hwnd)
            
            # 绘制二值化之后的血条
            if pic:
                qcimg = self.binary_img(pic.toImage())
                precentage = int(self.window.MinBloodPrecentageSelecter.currentText()) * 0.01
                position = math.ceil(qcimg.width() * precentage)
                if qcimg.pixelColor(position, 0).red() > 200:
                    if state.enable_blood_helper:
                        self.do_add_blood(hwnd, state.blood_key)
            
            # 找蓝
            pic = self.find_magic_pic(hwnd)
            
            # 绘制二值化之后的蓝条
            if pic:
                qcimg = self.binary_img(pic.toImage())
                position = math.ceil(qcimg.width() * 0.3)
                if qcimg.pixelColor(position, 0).red() > 200:
                    if state.enable_magic_helper:
                        self.do_add_magic(hwnd, state.magic_key)
            
            # 卡键
            if state.stuck_key_enabled:
                for tick_key in state.tick_keys:
                    if tick_key != '':
                        util.press(hwnd, tick_key.lower())
        
        # 更新 UI 显示（当前选中的窗口）
        current_hwnd = self.state_manager.current_hwnd
        if current_hwnd:
            # 显示角色名
            pic = util.grab_image_qt(current_hwnd, util.Position(130, 7), util.Rectangle(90, 15))
            util.show_pix_on_graph_view(self.window.CurrentRolePicture, pic)
            
            # 显示血量
            pic = self.find_blood_pic(current_hwnd)
            util.show_pix_on_graph_view(self.window.CurrentBloodPicture, pic)
            
            # 显示蓝量
            pic = self.find_magic_pic(current_hwnd)
            util.show_pix_on_graph_view(self.window.CurrentMagicPicture, pic)
    
    def refresh_windows(self):
        """动态刷新窗口列表"""
        if not self.window:
            return
        
        # 获取当前所有 QQ三国 窗口
        ws = util.find_window('QQ三国')
        
        # 获取现有窗口列表
        existing_hwnds = set()
        for i in range(self.window.WindowSelecter.count()):
            existing_hwnds.add(self.window.WindowSelecter.itemData(i))
        
        # 添加新窗口
        for w in ws:
            if w.hwnd not in existing_hwnds:
                self.window.WindowSelecter.addItem(w.window_text, w.hwnd)
                self.state_manager.get_state(w.hwnd)
                print(f"发现新窗口: {w.window_text} ({w.hwnd})")
        
        # 检查已关闭的窗口
        current_items = []
        for i in range(self.window.WindowSelecter.count()):
            hwnd = self.window.WindowSelecter.itemData(i)
            item_text = self.window.WindowSelecter.itemText(i)
            current_items.append((hwnd, item_text))
        
        # 移除已关闭的窗口
        for hwnd, text in current_items:
            window_exists = False
            for w in ws:
                if w.hwnd == hwnd:
                    window_exists = True
                    # 更新窗口标题
                    if w.window_text != text:
                        index = self.window.WindowSelecter.findData(hwnd)
                        if index >= 0:
                            self.window.WindowSelecter.setItemText(index, w.window_text)
                    break
            
            if not window_exists:
                # 窗口已关闭
                index = self.window.WindowSelecter.findData(hwnd)
                if index >= 0:
                    self.window.WindowSelecter.removeItem(index)
                    print(f"窗口已关闭: {text} ({hwnd})")
                
                # 如果关闭的是当前窗口，切换到其他窗口
                if self.state_manager.current_hwnd == hwnd:
                    if self.window.WindowSelecter.count() > 0:
                        new_hwnd = self.window.WindowSelecter.itemData(0)
                        self.state_manager.set_current_hwnd(new_hwnd)
                        state = self.state_manager.get_state(new_hwnd)
                        self.window.StuckKeyStatus.setChecked(state.stuck_key_enabled)
                    else:
                        self.state_manager.set_current_hwnd(None)
    
    def do_add_magic(self, hwnd, key):
        """发送加蓝按键"""
        util.alt_press(hwnd, key.lower())
    
    def do_add_blood(self, hwnd, key):
        """发送加血按键"""
        util.alt_press(hwnd, key.lower())
    
    def find_blood_pic(self, hwnd):
        """查找血条图片"""
        return util.grab_image_qt(hwnd, util.Position(100, 33), util.Rectangle(118, 15))
    
    def find_magic_pic(self, hwnd):
        """查找蓝条图片"""
        return util.grab_image_qt(hwnd, util.Position(100, 54), util.Rectangle(98, 8))
    
    def binary_img(self, img):
        """二值化图像"""
        qcimg = img.copy(0, 0, img.width(), 1)
        for i in range(qcimg.width()):
            for j in range(qcimg.height()):
                c = qcimg.pixelColor(i, j)
                rc = self.binary_color(c)
                qcimg.setPixelColor(QPoint(i, j), rc)
        return qcimg
    
    def binary_color(self, c):
        """二值化颜色"""
        r = c.red()
        g = c.green()
        b = c.blue()
        if np.var([r, g, b]) < 100:
            return QColor(255, 255, 255)
        else:
            return QColor(0, 0, 0)