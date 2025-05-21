from tkinter import *
from tkinter import ttk

from bext import height

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
    label_term.grid(row=3, column=0, sticky=NE)

    lb_term = Listbox(win, width=31)
    lb_term.grid(row=3, column=1, sticky=W)

    frame_btn_term = Frame(win, background='black', width=50, height=100)
    frame_btn_term.grid(row=3, column=1, sticky=NE, pady=7)

    photo_add = PhotoImage(file='icons/add_icon.png')

    btn_add_term = Button(frame_btn_term, image=photo_add, activebackground='green')
    btn_add_term.image = photo_add
    btn_add_term.pack()

    photo_delete = PhotoImage(file='icons/delete_icon.png')

    btn_delete_term = Button(frame_btn_term, image=photo_delete, activebackground='red')
    btn_delete_term.image = photo_delete
    btn_delete_term.pack()

    btn_save = ttk.Button(win, text='Сохранить')
    btn_save.grid(row=4, column=1, sticky=SE)

    btn_cancel = ttk.Button(win, text='Отмена')
    btn_cancel.grid(row=5, column=1, sticky=NE)


def win_add_edit_pr():
    win = Tk()

    win.title('TaskMain')
    win.geometry('400x500+650+300')
    win.resizable(width=False, height=False)

    win_widget_pr(win)

    win.mainloop()

win_add_edit_pr()
