import os
import shutil
from tkinter import *

def error():
    lable5 = Label(root,font="Cambria", bg="#86F6AE",fg='red', text="Please make sure the directory is correct!!!!")
    lable5.grid(row=6, column=0)


def file_arranger():
    a=field.get()
    print(a)
    try:
        os.chdir(a)
        print(os.getcwd())
        print(os.listdir())
        for i in os.listdir():
            p, q = os.path.splitext(i)
            if q == '.jpg' or q=='.JPG'or q == '.ico':
                # os.makedirs('JPEGs')
                print(os.getcwd() + '\JPEGs')
                shutil.move(i, os.getcwd() + '\Photos')
            elif q == '.pdf':
                # os.makedirs('PDFs')
                shutil.move(i, os.getcwd() + '\PDFs')
            elif q == '.txt':
                # os.makedirs('TEXTs')
                shutil.move(i, os.getcwd() + '\TEXTs')
            elif q == '.exe' or q == '.msi':
                shutil.move(i, os.getcwd()+'\Programmes')
            elif q == '.mp4' or q == '.mkv':
                # os.makedirs('Videos')
                shutil.move(i, os.getcwd() + '\Videos')
    except:
        error()

root=Tk()
root.title('File Arranger App')
root.iconbitmap('1.ico')
root.geometry('467x300')
root.configure(background='#86F6AE')

#creating labels for the entry of the dir
lable1=Label(root,text='Enter the dir of the file you want to re-arrange: ',font="Cambria")
lable1.grid(row=0,column=0)

lable2=Label(root,bg="#86F6AE")
lable2.grid(row=1,column=0)

#creating the entry field for dir input
field=Entry(root,bg='#D4E8F2',fg='black',width=50,font="Cambria")
field.grid(row=2,column=0,padx=5,pady=5)

lable3=Label(root,bg="#86F6AE")
lable3.grid(row=3,column=0)

#creating the buttons
button_1=Button(root,bg='#8DCFED',text="Click to rearrange your files", command=file_arranger,padx=10,pady=10,font="Cambria")
button_1.grid(row=4,column=0)

lable4=Label(root,bg="#86F6AE")
lable4.grid(row=5,column=0)




root.mainloop()