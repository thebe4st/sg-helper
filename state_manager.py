class WindowState:
    """单个窗口的状态"""
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.stuck_key_enabled = False
        self.enable_blood_helper = False
        self.enable_magic_helper = False
        self.blood_key = 'R'
        self.magic_key = 'T'
        self.tick_keys = ['A', '', '', '']  # Tick1-4

class WindowStateManager:
    """管理所有窗口的状态"""
    def __init__(self):
        self.window_states = {}  # {hwnd: WindowState}
        self.current_hwnd = None
    
    def get_state(self, hwnd):
        """获取或创建窗口状态"""
        if hwnd not in self.window_states:
            self.window_states[hwnd] = WindowState(hwnd)
        return self.window_states[hwnd]
    
    def set_current_hwnd(self, hwnd):
        """设置当前窗口"""
        self.current_hwnd = hwnd
    
    def get_current_state(self):
        """获取当前窗口的状态"""
        if self.current_hwnd and self.current_hwnd in self.window_states:
            return self.window_states[self.current_hwnd]
        return None
    
    def toggle_stuck_key(self):
        """切换当前窗口的卡键状态"""
        state = self.get_current_state()
        if state:
            state.stuck_key_enabled = not state.stuck_key_enabled
            return state.stuck_key_enabled
        return False
    
    def set_stuck_key(self, enabled):
        """设置当前窗口的卡键状态"""
        state = self.get_current_state()
        if state:
            state.stuck_key_enabled = enabled
    
    def remove_window(self, hwnd):
        """移除窗口状态"""
        if hwnd in self.window_states:
            del self.window_states[hwnd]
    
    def get_all_states(self):
        """获取所有窗口状态"""
        return self.window_states