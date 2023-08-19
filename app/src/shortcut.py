# import tkinter as tk
# from tkinter import Menu, simpledialog
# import subprocess

# #AttributeError: module 'tkinter' has no attribute 'simpledialog'

# class ShortcutOrganizerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Shortcut Organizer")

#         # Dicionário para armazenar os grupos de atalhos
#         self.shortcut_groups = {}

#         self.create_menu()
#         self.create_listbox()

#     def create_menu(self):
#         menubar = Menu(self.root)
#         self.root.config(menu=menubar)

#         file_menu = Menu(menubar, tearoff=0)
#         file_menu.add_command(label="Exit", command=self.root.quit)

#         menubar.add_cascade(label="File", menu=file_menu)

#         # Menu para atalhos
#         shortcut_menu = Menu(menubar, tearoff=0)
#         shortcut_menu.add_command(label="Create New Shortcut", command=self.create_new_shortcut)
#         shortcut_menu.add_separator()

#         menubar.add_cascade(label="Shortcuts", menu=shortcut_menu)

#     def create_listbox(self):
#         self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50)
#         self.listbox.pack(fill=tk.BOTH, expand=True)
#         self.listbox.bind("<Double-Button-1>", self.open_shortcut_group)

#     def create_new_shortcut(self):
#         new_shortcut = simpledialog.askstring("Create New Shortcut", "Enter the name of the new shortcut:")
#         if new_shortcut:
#             self.shortcut_groups[new_shortcut] = []
#             self.update_shortcuts_list()

#     def open_shortcut_group(self, event):
#         selected_index = self.listbox.curselection()
#         if selected_index:
#             selected_shortcut = self.listbox.get(selected_index[0])
#             for app in self.shortcut_groups[selected_shortcut]:
#                 subprocess.Popen(app)

#     def update_shortcuts_list(self):
#         self.listbox.delete(0, tk.END)
#         for shortcut in self.shortcut_groups:
#             self.listbox.insert(tk.END, shortcut)


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ShortcutOrganizerApp(root)
#     root.mainloop()


import PySimpleGUI as sg
import subprocess

class ShortcutOrganizerApp:
    def __init__(self):
        self.shortcut_groups = {}

    def create_new_shortcut(self):
        layout = [
            [sg.Text('Enter the name of the new shortcut:')],
            [sg.InputText(key='shortcut_name')],
            [sg.Button('Create'), sg.Button('Cancel')]
        ]

        window = sg.Window('Create New Shortcut', layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                break
            elif event == 'Create':
                new_shortcut = values['shortcut_name']
                if new_shortcut:
                    self.shortcut_groups[new_shortcut] = []
                    window.close()
                    break

        window.close()

    def open_shortcut_group(self, shortcut_name):
        for app in self.shortcut_groups[shortcut_name]:
            subprocess.Popen(app)

    def run(self):
        sg.theme('DefaultNoMoreNagging')

        layout = [
            [sg.Text('Shortcuts')],
            [sg.Listbox(list(self.shortcut_groups.keys()), size=(30, 6), key='shortcuts')],
            [sg.Button('Open Shortcut Group'), sg.Button('Create New Shortcut'), sg.Button('Exit')]
        ]

        window = sg.Window('Shortcut Organizer', layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Exit':
                break
            elif event == 'Open Shortcut Group':
                selected_shortcut = values['shortcuts'][0]
                if selected_shortcut:
                    self.open_shortcut_group(selected_shortcut)
            elif event == 'Create New Shortcut':
                self.create_new_shortcut()
                window['shortcuts'].update(list(self.shortcut_groups.keys()))

        window.close()

if __name__ == "__main__":
    app = ShortcutOrganizerApp()
    app.run()
