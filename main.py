import sys
from PySide6.QtWidgets import QApplication

from window import MainWindow
from hotkey_manager import HotkeyManager
from state_manager import WindowStateManager
from game_handler import GameHandler
from config_manager import ConfigManager

def main():
    app = QApplication(sys.argv)
    
    # 初始化配置管理器
    config_manager = ConfigManager()
    
    # 初始化状态管理器
    state_manager = WindowStateManager()
    
    # 初始化游戏处理器
    game_handler = GameHandler(state_manager)
    
    # 初始化快捷键管理器
    hotkey_manager = HotkeyManager(state_manager)
    
    # 创建主窗口（传递配置管理器）
    main_window = MainWindow(state_manager, game_handler, hotkey_manager, config_manager)
    main_window.show()
    
    # 启动事件循环
    sys.exit(app.exec())

if __name__ == "__main__":
    main()