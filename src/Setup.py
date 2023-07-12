import configparser
from pathlib import Path
import os


config_file = Path(__file__).parent / "data" / "config.cfg"
folder = Path(__file__).parent / "data"

class Settings(object):
    def __init__(self):
        if not folder.exists():
            os.makedirs(folder)
        if not config_file.exists():
            print("Config does not exist and is being created automatically...")
            f = open(config_file,'w')
            f.write('[config]\n')
            f.write('dev_mode = False\n')
            f.write('keep_login = True\n')
            f.write('\n')
            f.write('[Settings]\n')
            f.write('port = 5000\n')
            f.write('host = 127.0.0.1\n')
            f.write('\n')
            f.close()
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_file)

    def bg_path(self):
        out = self.cfg.get("config","Background_path")
        return out
    
    def keep_login(self):
        out = self.cfg.get("config","keep_login")
        return out

    def cfg_in(self, section, option, value):
        value = str(value)
        self.cfg.set(section,option,value)
        self.cfg.write(open(config_file, "w"))

    def dev_mode(self):
        out = self.cfg.get('config',"Dev_Mode")
        return out

    def rd(self, section, option):
        out = self.cfg.get(section,option)
        return out
    