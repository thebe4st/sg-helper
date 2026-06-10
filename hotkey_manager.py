import keyboard

class HotkeyManager:
    """全局快捷键管理器"""
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.window = None
    
    def set_window(self, window):
        """设置 UI 窗口引用"""
        self.window = window
    
    def register_hotkeys(self):
        """注册所有全局快捷键"""
        # CTRL+` 切换卡键状态
        keyboard.add_hotkey('ctrl+`', self.on_ctrl_backtick_pressed)
    
    def on_ctrl_backtick_pressed(self):
        """处理 CTRL+` 快捷键"""
        print(f"快捷键被触发，当前窗口: {self.state_manager.current_hwnd}")
        enabled = self.state_manager.toggle_stuck_key()
        
        if self.window:
            self.window.StuckKeyStatus.setChecked(enabled)
        
        print(f"卡键状态已切换为: {enabled}")