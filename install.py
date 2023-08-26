#!/bin/python3

import tkinter, os, shutil
from tkinter import filedialog, messagebox
from random import choice

class main():
    def __init__(self) -> None:
        self.get_path()
        self.popup()
        if self.choose():
            if self.prepare():
                if not self.install():
                    self.remove()
        
    def remove(self) -> None:
        os.unlink(self.target_data)
    
    def install(self) -> bool:
        os.chdir(self.working_dir + r"\\data")
        return not os.system(self.command)
    
    def cp_data(self) -> bool:
        print(">> Please wait....")
        self.target_data = "\\".join(self.path_install.split(r"\\")[:-1]) + r"\\Pie64_5.12.115.1002.exe"
        return shutil.copy(
            self.working_dir + r"\\data\\VM.7z",
            self.target_data
        )
    
    def prepare(self) -> bool:
        self.command = " ".join([
            'start', 
            '""', 
            r'"{dir}\\BlueStacksInstaller_5.12.115.1002_native_e9abc662bd6053e7c8e6890ba057d82a_MzsxNQ==.exe"'.format(dir = self.working_dir + r"\\data"), 
            '-versionMachineID={id}'.format(id = self.get_id()), 
            '-machineID={id}'.format(id = self.get_id()), 
            '-pddir="{path}"'.format(path = self.path_install), 
            '-defaultImageName=Pie64', 
            '-imageToLaunch=Pie64', 
            '-isSSE4Available=1',
            '-appToLaunch=bs5',
            '-bsxVersion=10.3.10.1008',
            '-country=VN',
            # '-isWalletFeatureEnabled', 
        ])
        
        return self.cp_data()
    
    def popup(self) -> None:
        messagebox.showinfo('BlueStacks 5 (KhanhNguyen9872)', 'Click OK to select the installation directory')
    
    def choose(self) -> bool:
        root = tkinter.Tk()
        root.withdraw()
        self.path_install = filedialog.askdirectory(initialdir="{}".format(os.environ["PROGRAMDATA"]), title='BlueStacks 5 (KhanhNguyen9872)')
        if not self.path_install:
            return False
        self.path_install = r"\\".join(str(self.path_install).split("/")) + r"\\BlueStacks_nxt"
        return True
    
    def get_id(self) -> str:
        return '{id1}-{id2}-{id3}-{id4}-{id5}'.format(
            id1 = self.random(8), 
            id2 = self.random(4), 
            id3 = self.random(4), 
            id4 = self.random(4), 
            id5 = self.random(12), 
        )
    
    def random(self, length=0) -> str:
        return "".join([choice("qwertyuiopasdfghjklzxcvbnm1234567890") for i in range(length)])
    
    def get_path(self) -> None:
        self.working_dir = os.getcwd().replace("\\", r"\\")

if __name__ == '__main__':
    main()
del main