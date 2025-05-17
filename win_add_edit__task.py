from tkinter import *
from tkinter import ttk
from config_widget import configurate_grid

def win_widget(win:Tk|Frame):
    configurate_grid(win, 8, 3)

    label_title = ttk.Label(win, text='Добавление задачи', anchor=CENTER)
    label_title.grid(row=0, column=0, columnspan=2)

    label_name = ttk.Label(win, text='Название задачи')
    label_name.grid(row=1, column=0, sticky=E)

    entry_name = ttk.Entry(win)
    entry_name.grid(row=1, column=1, sticky=EW)

    label_description = ttk.Label(win, text='Описание задачи')
    label_description.grid(row=2, column=0, sticky=NE, pady=10)

    entry_description = Text(win, height=10, width=25)
    entry_description.grid(row=2, column=1, sticky=EW)

    label_term = ttk.Label(win, text='Срок выполнения')
    label_term.grid(row=3, column=0, sticky=E)

    label_priority = ttk.Label(win, text='Приоритет')
    label_priority.grid(row=4, column=0, sticky=E)

    list_priority = ['Низкий', 'Средний', 'Высокий']
    cb_priority = ttk.Combobox(win, values=list_priority, state='readonly')
    cb_priority.current(0)
    cb_priority.grid(row=4, column= 1, sticky=EW)

    label_status = ttk.Label(win, text='Статус')
    label_status.grid(row=5, column=0, sticky=E)

    list_status = ['В процессе', 'Завершена', 'Отложена']
    cb_status = ttk.Combobox(win, values=list_status, state='readonly')
    cb_status.current(0)
    cb_status.grid(row=5, column= 1, sticky=EW)

    btn_save = ttk.Button(win, text='Сохранить')
    btn_save.grid(row=6, column=1, sticky=SE)

    btn_cancel = ttk.Button(win, text='Отмена')
    btn_cancel.grid(row=7, column=1, sticky=NE)


def win_add_edit():
    win = Tk()

    win.title('TaskMain')
    win.geometry('400x500+650+300')
    win.resizable(width=False, height=False)

    win_widget(win)

    win.mainloop()

win_add_edit()
