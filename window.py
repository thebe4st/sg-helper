from PySide6.QtWidgets import QMainWindow, QFileDialog
from ui import Ui_MainWindow
import subprocess
import os

class MainWindow(QMainWindow):
    def __init__(self, state_manager, game_handler, hotkey_manager, config_manager):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.state_manager = state_manager
        self.game_handler = game_handler
        self.hotkey_manager = hotkey_manager
        self.config_manager = config_manager
        
        # 设置引用
        self.game_handler.set_window(self.ui)
        self.hotkey_manager.set_window(self.ui)
        
        # 初始化窗口
        self.init_window()
    
    def init_window(self):
        """初始化窗口"""
        # 初始化窗口选择器
        self.init_window_selector()
        
        # 连接 UI 变化事件
        self.connect_ui_events()
        
        # 注册快捷键
        self.hotkey_manager.register_hotkeys()
        
        # 启动定时器
        self.game_handler.start_timers()
    
    def init_window_selector(self):
        """初始化窗口选择器"""
        import util
        
        ws = util.find_window('QQ三国')
        for w in ws:
            self.ui.WindowSelecter.addItem(w.window_text, w.hwnd)
            self.state_manager.get_state(w.hwnd)
        
        if self.ui.WindowSelecter.count() > 0:
            self.on_window_select(0)
        
        self.ui.WindowSelecter.currentIndexChanged.connect(self.on_window_select)
    
    def connect_ui_events(self):
        """连接 UI 事件"""
        # 保存状态事件
        self.ui.MinBloodKeySelecter.currentIndexChanged.connect(self.save_current_state)
        self.ui.MinMagicKeySelecter.currentIndexChanged.connect(self.save_current_state)
        self.ui.Tick1.currentIndexChanged.connect(self.save_current_state)
        self.ui.Tick2.currentIndexChanged.connect(self.save_current_state)
        self.ui.Tick3.currentIndexChanged.connect(self.save_current_state)
        self.ui.Tick4.currentIndexChanged.connect(self.save_current_state)
        
        # 卡键状态变化
        self.ui.StuckKeyStatus.stateChanged.connect(self.on_stuck_key_toggled)
        
        # 快速启动按钮
        if hasattr(self.ui, 'btnQuickStart'):
            self.ui.btnQuickStart.clicked.connect(self.on_quick_start)
        
        # 重新选择游戏路径按钮
        if hasattr(self.ui, 'btnReSelectExe'):
            self.ui.btnReSelectExe.clicked.connect(self.on_reselect_exe)
    
    def on_window_select(self, idx):
        """窗口选择变化"""
        hwnd = self.ui.WindowSelecter.itemData(idx)
        self.state_manager.set_current_hwnd(hwnd)
        print(f"切换到窗口: {hwnd}")
        
        # 更新 UI 显示当前窗口的状态
        state = self.state_manager.get_current_state()
        if state:
            self.ui.StuckKeyStatus.setChecked(state.stuck_key_enabled)
            print(f"当前窗口卡键状态: {state.stuck_key_enabled}")
    
    def save_current_state(self):
        """保存当前窗口状态"""
        state = self.state_manager.get_current_state()
        if state:
            state.blood_key = self.ui.MinBloodKeySelecter.currentText()
            state.magic_key = self.ui.MinMagicKeySelecter.currentText()
            state.tick_keys = [
                self.ui.Tick1.currentText(),
                self.ui.Tick2.currentText(),
                self.ui.Tick3.currentText(),
                self.ui.Tick4.currentText()
            ]
    
    def on_stuck_key_toggled(self, state):
        """卡键状态变化"""
        self.state_manager.set_stuck_key(state == 2)
    
    def on_quick_start(self):
        """快速启动按钮点击事件 - 创建子进程启动游戏"""
        try:
            # 从配置获取游戏路径
            game_exe = self.config_manager.get("gameExe", "")
            
            # 如果没有配置，让用户选择
            if not game_exe:
                print("未配置游戏路径，请选择游戏客户端...")
                
                # 显示文件选择对话框
                exe_path, _ = QFileDialog.getOpenFileName(
                    self,
                    "选择游戏客户端",
                    "",
                    "可执行文件 (*.exe);;所有文件 (*.*)"
                )
                
                if exe_path:
                    game_exe = exe_path
                    self.config_manager.set("gameExe", game_exe)
                    print(f"已选择并保存: {game_exe}")
                else:
                    print("未选择游戏客户端")
                    return
            
            # 检查文件是否存在
            if not os.path.exists(game_exe):
                print(f"游戏文件不存在: {game_exe}")
                
                # 让用户重新选择
                exe_path, _ = QFileDialog.getOpenFileName(
                    self,
                    "游戏文件不存在，请重新选择",
                    "",
                    "可执行文件 (*.exe);;所有文件 (*.*)"
                )
                
                if exe_path:
                    game_exe = exe_path
                    self.config_manager.set("gameExe", game_exe)
                    print(f"已重新选择: {game_exe}")
                else:
                    return
            
            # 启动游戏
            args = [game_exe]
            args.append(" -.	")
            
            process = subprocess.Popen(
                args,
                shell=False,
                creationflags=subprocess.CREATE_NEW_CONSOLE,
                cwd=os.path.dirname(game_exe)
            )
            print(f"游戏已启动，PID: {process.pid}")
            
        except Exception as e:
            print(f"启动游戏失败: {e}")
    
    def on_reselect_exe(self):
        """重新选择游戏路径按钮点击事件"""
        try:
            # 显示文件选择对话框
            exe_path, _ = QFileDialog.getOpenFileName(
                self,
                "重新选择游戏客户端",
                "",
                "可执行文件 (*.exe);;所有文件 (*.*)"
            )
            
            if exe_path:
                # 更新配置
                self.config_manager.set("gameExe", exe_path)
                print(f"游戏路径已更新为: {exe_path}")
            else:
                print("未选择游戏客户端")
                
        except Exception as e:
            print(f"选择游戏路径失败: {e}")