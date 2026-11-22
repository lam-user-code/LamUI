import customtkinter as ctk
import os
import platform

root = ctk.CTk()
root.title('LamUI')
root.geometry('1280x720')
root.configure(fg_color='#202020')
root.resizable(False, False)

label = ctk.CTkLabel(
    root,
    text='Welcome to LamUI\n1.0',
    font=("Comic Sans MS", 20, 'italic'),
    fg_color='orange',
    text_color='black'
)
label.pack()

label = ctk.CTkLabel(
    root,
    text="This doesn't replace a real operating system, and it's made just for fun :p",
    font=("Comic Sans MS", 10, 'bold'),
    fg_color='white',
    text_color='black'
)
label.place(x=0, y=695)

cpu = platform.processor()

def open_cmd():
    os.system('start cmd')

def open_notepad():
    os.system('start notepad')

def open_explorer():
    os.system('start explorer')

def open_paint():
    os.system('start mspaint')

def open_task():
    os.system('start taskmgr')

def show_cpu():
    cpu
    label = ctk.CTkLabel(root, text=cpu, fg_color='orange', text_color='black')
    label.pack()

btn1 = ctk.CTkButton(root, text='cmd', command=open_cmd, font=("Comic Sans MS", 20, 'italic'), fg_color='#C0C0C0', text_color='#000000')
btn1.pack(pady=10)

btn2 = ctk.CTkButton(root, text='notepad', command=open_notepad, font=("Comic Sans MS", 20, 'italic'), fg_color='#C0C0C0', text_color='#000000')
btn2.pack(pady=10)

btn2 = ctk.CTkButton(root, text='explorer', command=open_explorer, font=("Comic Sans MS", 20, 'italic'), fg_color='#C0C0C0', text_color='#000000')
btn2.pack(pady=10)

btn2 = ctk.CTkButton(root, text='paint', command=open_paint, font=("Comic Sans MS", 20, 'italic'), fg_color='#C0C0C0', text_color='#000000')
btn2.pack(pady=10)

btn2 = ctk.CTkButton(root, text='task manager', command=open_task, font=("Comic Sans MS", 20, 'italic'), fg_color='#C0C0C0', text_color='#000000')
btn2.pack(pady=10)

btn3 = ctk.CTkButton(root, text='show cpu', command=show_cpu)
btn3.pack(pady=10)

root.mainloop()