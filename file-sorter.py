import os
from tkinter import *
from tkinter import filedialog

root=Tk()
root.title('File sorter - Automation')

def sort():
    video = ".mp4"
    picture = ".jpg"

    parent_dir = folder
    path1 = parent_dir+'/videos'
    path2 = parent_dir+'/pictures'

    os.makedirs(path1)
    os.makedirs(path2)
    #'C:/test folder'

    for object in objects:
        if object.endswith((video)):
            print('video')
            print(object)
            path = parent_dir+'/'+object
            new_path = path1+'/'+object
            os.rename(path, new_path)
        else:
            print('picture')
            print(object)
            path = parent_dir+'/'+object
            new_path = path2+'/'+object
            os.rename(path, new_path)

def select():
    root.foldername = filedialog.askdirectory(initialdir="/")
    global folder
    folder = root.foldername
    global objects
    objects = os.listdir(folder)

    my_entry.insert(0, folder)


My_Label = Label(root, text='File Sorter', font=('Helvetica', 24))
My_Label.pack()

select_folder = Button(root, text='Selcet a folder to sort', font=("Helvetica", 20, "bold"), command=select)
select_folder.pack(padx=10, pady=10, anchor=CENTER)

my_entry = Entry(root, font=('Helvetica', 20))
my_entry.pack(padx=10, pady=10)

my_buton = Button(root, text='Sort Files', font=("Helvetica", 20, "bold"), command=sort)
my_buton.pack(padx=10, pady=10, anchor=CENTER)

root.mainloop()