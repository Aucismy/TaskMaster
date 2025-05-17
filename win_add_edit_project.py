from tkinter import *
from tkinter import ttk
from config_widget import configurate_grid

def win_widget_pr(win:Tk|Frame):
    configurate_grid(win, 6, 3)
    label_title = ttk.Label(win, text='Добавление проекта', anchor=CENTER)
    label_title.grid(row=0, column=0, columnspan=2)

    label_name = ttk.Label(win, text='Название проекта')
    label_name.grid(row=1, column=0, sticky=E)

    entry_name = ttk.Entry(win)
    entry_name.grid(row=1, column=1, sticky=EW)
#
    label_description = ttk.Label(win, text='Описание проекта')
    label_description.grid(row=2, column=0, sticky=NE, pady=10)

    entry_description = Text(win, height=10, width=25)
    entry_description.grid(row=2, column=1, sticky=EW)

    label_term = ttk.Label(win, text='Участники проекта')
    label_term.grid(row=3, column=0, sticky=E)



    btn_save = ttk.Button(win, text='Сохранить')
    btn_save.grid(row=4, column=1, sticky=SE)

    btn_cancel = ttk.Button(win, text='Отмена')
    btn_cancel.grid(row=5, column=1, sticky=NE)


def win_add_edit_pr():
    win = Tk()

    win.title('TaskMain')
    win.geometry('400x400+650+300')
    win.resizable(width=False, height=False)

    win_widget_pr(win)

    win.mainloop()

win_add_edit_pr()
