import os
import json
from pathlib import Path

class ConfigManager:
    """配置文件管理器"""
    
    def __init__(self):
        # 用户目录下的配置文件路径
        self.config_dir = Path.home() / ".sg-util"
        self.config_file = self.config_dir / "config.json"
        
        # 默认配置
        self.default_config = {
            "gameExe": ""
        }
        
        # 加载配置
        self.config = self.load_config()
    
    def load_config(self):
        """加载配置文件"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"加载配置文件失败: {e}")
                return self.default_config.copy()
        else:
            # 创建默认配置
            return self.default_config.copy()
    
    def save_config(self):
        """保存配置文件"""
        try:
            # 确保目录存在
            self.config_dir.mkdir(parents=True, exist_ok=True)
            
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            print(f"配置已保存到: {self.config_file}")
        except Exception as e:
            print(f"保存配置文件失败: {e}")
    
    def get(self, key, default=None):
        """获取配置项"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """设置配置项"""
        self.config[key] = value
        self.save_config()