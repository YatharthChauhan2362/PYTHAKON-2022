'''
PYTHAKON 2022

TEAM MEMBERS:
Yatharth Chauhan
Mehul Patel
Reeya Thanki

Project: File Organization With Automation Using Python

'''
# import os
# import glob
from tkinter import *
from threading import *
from PIL import ImageTk, Image
from tkinter import messagebox, ttk, filedialog
import shutil


file_types = ['.jpg', 'jpeg', '.png', '.mp3', '.mp4', '.pdf']
# Extensions to this dictionary
Extensions = {
    'Documents': ('.pdf', '.doc', '.xls', 'txt', '.csv', '.zip',
                  '.xml', '.zip', '.docx', '.DOCX', '.odt'),
    'Pictures': ('.jpg', '.jpeg', '.png', '.JPG'),
    'Videos': ('.mp4', '.mkv', '.3gp', '.flv', '.mpeg'),
    'Music': ('.mp3', '.wav', '.m4a', '.webm'),
    'Programs': ('.py', '.cpp', '.c', '.sh', '.js'),
    'Apps': ('.exe', '.apk'),
}


class File_automation:
    def __init__(self, root):
        # Setting the Tkinter main window
        self.window = root
        self.window.geometry("720x500")
        self.window.title('File Renamer - PySeek')
        self.window.resizable(width=False, height=False)
        self.window.configure(bg='gray90')


# The main function
if __name__ == "__main__":
    root = Tk()

    obj = File_automation(root)
    root.mainloop()
