import win32gui, win32con, win32api
from PIL import ImageGrab
from PySide6.QtWidgets import QApplication, QGraphicsPixmapItem, QGraphicsScene
from PySide6.QtCore import QRect
from PySide6.QtGui import QPixmap

import const
import time
global app


class Window:
    window_text = ''
    hwnd = 0x00

    def __init__(self, hwnd):
        self.window_text = win32gui.GetWindowText(hwnd)
        self.hwnd = hwnd


class Rectangle:
    width = 0
    hight = 0

    def __init__(self, w, h):
        self.width = w
        self.hight = h


class Position:
    x = 0
    y = 0

    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

def press(handle,key):
    win32api.SendMessage(handle, win32con.WM_KEYDOWN, const.keyboard_map[key], 0)
    win32api.SendMessage(handle, win32con.WM_KEYUP, const.keyboard_map[key], 0)

def alt_press(handle,key):
    win32api.SendMessage(handle, win32con.WM_KEYDOWN, const.keyboard_map[key], 1<<29)
    win32api.SendMessage(handle, win32con.WM_KEYUP, const.keyboard_map[key], 1<<29)

def alt_pressv2(handle,key):
    win32api.PostMessage(handle, win32con.WM_SYSKEYDOWN, win32con.VK_MENU,  1<<29)
    win32api.PostMessage(handle, win32con.WM_SYSKEYDOWN, const.keyboard_map[key],  1<<29)
    win32api.PostMessage(handle, win32con.WM_SYSKEYUP, const.keyboard_map[key],  1<<29)
    win32api.PostMessage(handle, win32con.WM_SYSKEYUP, win32con.VK_MENU,  1<<29)

def alt_pressv3(handle,key):
    win32api.keybd_event(0x12,0,0,0)
    win32api.keybd_event(const.keyboard_map[key],0,0,0)
    win32api.keybd_event(0x12,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(const.keyboard_map[key],0,win32con.KEYEVENTF_KEYUP,0)

def find_window(window_name):
    windows = []
    win32gui.EnumWindows(_callback, windows)
    ret = []
    for i in windows:
        if window_name in i.window_text:
            ret.append(i)
    return ret


def grab_image(hwnd, pos, rectangle):
    game_rect = win32gui.GetWindowRect(hwnd)
    return ImageGrab.grab(game_rect)


def grab_image_qt(hwnd, pos, rectangle):
    screen = QApplication.primaryScreen()
    pixmap = screen.grabWindow(hwnd)
    pic = QPixmap.copy(pixmap, rect=QRect(pos.x, pos.y, rectangle.width, rectangle.hight))
    return pic


def _callback(hwnd, ret):
    ret.append(Window(hwnd))


def int2rgb(num):
    return num >> 16 & 255, num >> 8 & 255, num & 255


def show_pix_on_graph_view(widget, pixmap):
    item = QGraphicsPixmapItem(pixmap)
    scene = QGraphicsScene()
    scene.addItem(item)
    widget.setScene(scene)


if __name__ == '__main__':
    ws = find_window('QQ三国')
    img = grab_image_qt(ws[0].hwnd, Position(100, 200), Rectangle(100, 200))
    img.show()
