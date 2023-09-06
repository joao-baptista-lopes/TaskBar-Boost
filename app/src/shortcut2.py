# import tkinter
# import customtkinter

# customtkinter.enable_macos_darkmode()
# customtkinter.set_appearance_mode("System")
# root_tk = tkinter.Tk()
# # janela normal de tkinter
# root_tk.geometry("400x240")
# root_tk.title("Shortcut manages")
# root_tk.mainloop()


# from tkinter import *
# root = Tk()
# root.geometry('300x400')
# mybutton = Button(root, text='Hello world ', font=("Montserrat", 16))

# mybutton.place(relx=0.5, rely=0.5,  anchor=CENTER)
# root.mainloop()

from tkinter import*
import customtkinter

root = customtkinter.tkinter()
Tk.geometry('300x400')

botao = customtkinter.CTkButton(master= root, text='Hello world', text_font="Montserrat, 16")
botao.place(relx=0.5, rely=0.5,  anchor=CENTER)
root.mainloop()
