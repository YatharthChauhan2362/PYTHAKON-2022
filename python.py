'''
PYTHAKON 2022

TEAM MEMBERS:
Yatharth Chauhan
Mehul Patel
Reeya Thanki

Project: File Organization With Automation Using Python
'''


import os

import shutil

from tkinter import *


from threading import *


from PIL import ImageTk, Image

from tkinter import messagebox, filedialog


Extensions = {
    'Documents': ('.pdf', '.doc', '.xls', 'txt', '.csv', '.zip',
                  '.xml', '.zip', '.docx', '.DOCX', '.odt'),
    'Pictures': ('.jpg', '.jpeg', '.png', '.JPG', '.svg'),
    'Videos': ('.mp4', '.mkv', '.3gp', '.flv', '.mpeg'),
    'Music': ('.mp3', '.wav', '.m4a', '.webm'),
    'Programs': ('.py', '.cpp', '.c', '.sh', '.js', '.css'),
    'Apps': ('.exe', '.apk'),
}


class File_Organizer:

    def __init__(self, root):

        self.window = root
        self.window.geometry("720x500")

        self.window.title('File Organizer - Using Python')

        self.window.resizable(width=False, height=False)

        self.window.configure(bg='gray90')

        self.Selected_Dir = ''

        self.Browsed = False

        self.frame_1 = Frame(self.window, bg='gray90',

                             width=280, height=70)
        self.frame_1.pack()
        self.frame_1.place(x=20, y=20)
 #
        self.Display_Logo()

        About_Btn = Button(self.window, text="About",
                           font=("Kokila", 10, 'bold'), bg="green",
                           fg="white", width=5, command=self.About_Window)
        About_Btn.place(x=600, y=20)

        Exit_Btn = Button(self.window, text="Exit",
                          font=("Kokila", 10, 'bold'), bg="green",
                          fg="white", width=5, command=self.Exit_Window)
        Exit_Btn.place(x=600, y=60)

        self.frame_2 = Frame(self.window, bg="white",
                             width=720, height=480)
        self.frame_2.place(x=0, y=110)

        self.Main_Page()

    def Display_Logo(self):

        image = Image.open('Images/fo.png')

        resized_image = image.resize((300, 98))

        self.img_1 = ImageTk.PhotoImage(resized_image)

        label = Label(self.frame_1, bg='gray90', image=self.img_1)
        label.pack()

    def Main_Page(self):
        Heading_Label = Label(self.frame_2, text="Please Select the Folder", font=(
            "Kokila", 20, 'bold'), bg='white')
        Heading_Label.place(x=160, y=20)

        Folder_Button = Button(self.frame_2, text="Select Folder",
                               font=("Kokila", 10, 'bold'), bg="white", width=10,
                               command=self.Select_Directory)
        Folder_Button.place(x=130, y=80)

        self.Folder_Entry = Entry(self.frame_2,
                                  font=("Helvetica", 12), width=32)
        self.Folder_Entry.place(x=256, y=85)

        Status = Label(self.frame_2, text="Status: ",
                       font=("Kokila", 12, 'bold'), bg='white')
        Status.place(x=180, y=130)

        self.Status_Label = Label(self.frame_2, text="Not Started Yet",
                                  font=("Kokila", 12), bg="white", fg="red")
        self.Status_Label.place(x=256, y=130)

        Start_Button = Button(self.frame_2, text="Start",
                              font=("Kokila", 13, 'bold'), bg="green", fg="white",
                              width=8, command=self.Organizer)
        Start_Button.place(x=280, y=180)

    def Select_Directory(self):
        self.Selected_Dir = filedialog.askdirectory(title="Select a location")

        self.Folder_Entry.insert(0, self.Selected_Dir)

        self.Selected_Dir = str(self.Selected_Dir)

        if os.path.exists(self.Selected_Dir):
            self.Browsed = True

    def Threading(self):

        self.x = Thread(target=self.Organizer, daemon=True)
        self.x.start()

    def Organizer(self):

        if not self.Browsed:
            messagebox.showwarning('No folders are choosen',
                                   'Please Select a Folder First')
            return
        try:

            self.Status_Label.config(text='Processing...')

            self.Current_Path = self.Selected_Dir

            if os.path.exists(self.Current_Path):

                self.Folder_List1 = []

                self.Folder_List2 = []
                self.Flag = False

                for folder, extensions in Extensions.items():
                    self.folder_name = folder
                    self.folder_path = os.path.join(
                        self.Current_Path, self.folder_name)

                    os.chdir(self.Current_Path)

                    if os.path.exists(self.folder_name):
                        self.Folder_List1.append(self.folder_name)

                    else:
                        self.Folder_List2.append(self.folder_name)
                        os.mkdir(self.folder_path)

                    for item in self.File_Finder(self.Current_Path, extensions):
                        self.Old_File_Path = os.path.join(
                            self.Current_Path, item)
                        self.New_File_Path = os.path.join(
                            self.folder_path, item)

                        shutil.move(self.Old_File_Path, self.New_File_Path)

                        self.Flag = True
            else:
                messagebox.showerror('Error!', 'Please Enter a Valid Path!')

            if self.Flag:
                self.Status_Label.config(text='Complete!')
                messagebox.showinfo('Done!', 'Complete!')
                self.Clear()

            if not self.Flag:
                self.Status_Label.config(text='Complete!')
                messagebox.showinfo('Done!',
                                    'Folders have been created\nNo Files were there to move')
                self.Clear()

        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {str(es)}")

    def File_Finder(self, folder_path, file_extensions):
        self.files = []
        for file in os.listdir(folder_path):
            for extension in file_extensions:
                if file.endswith(extension):
                    self.files.append(file)
        return self.files

    def Clear(self):
        self.Status_Label.config(text='Not Started Yet')
        self.Folder_Entry.delete(0, END)
        self.Selected_Dir = ''

    def About_Window(self):
        messagebox.showinfo("File Organizer 22.05",
                            "Developed By Team Mind Sight\n~CHARUSAT")

    def Exit_Window(self):
        self.window.destroy()


if __name__ == "__main__":
    root = Tk()

    obj = File_Organizer(root)
    root.mainloop()
  # Competed
