from tkinter import *
from  tkinter import ttk
from config_widget import *

def window(win:Tk):
    win.title('TaskMaster')
    win.geometry('700x400+650+300')
    win.config(menu=main_menu())

    configurate_grid(win, 2, 1)
    frame_list_project(win)
    frame_list_task(win)

def frame_list_project(win:Tk|Frame):
    frame_project = Frame(win)
    frame_project.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5)

    configurate_grid(frame_project, 2, 1)
    frame_project.rowconfigure(index=0, weight=0)

    label_list_project = ttk.Label(frame_project, text='Список проектов')
    label_list_project.grid(row=0, column=0, sticky=NW)

    columns_table = {
        'number': ['№', 50, False],
        'name': ['Название проекта', 200, True],
        'description': ['Описание', 300, True],
        'participants': ['Участники', 150, True]
    }

    configurate_table(frame_project, columns_table).grid(row=1, column=0, sticky=NSEW)

def frame_list_task(win:Tk|Frame):
    frame_task = Frame(win, background='light gray')
    frame_task.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)

    configurate_grid(frame_task, 2, 8)
    frame_task.rowconfigure(index = 0, weight=0)

    label_list_task = Label(frame_task, text='Список задач')
    label_list_task.grid(row=0, column=0, sticky=NW)

    label_search_task = Label(frame_task, text = 'Поиск')
    label_search_task.grid(row=0, column=2, sticky=E)

    text_search = ttk.Entry(frame_task)
    text_search.grid(row=0, column=3, sticky=W)

    btn_add = ttk.Button(frame_task, text='Добавить')
    btn_add.grid(row=0, column=5, sticky=NSEW)

    btn_edit = ttk.Button(frame_task, text='Редактировать')
    btn_edit.grid(row=0, column=6, sticky=NSEW)

    btn_delete = ttk.Button(frame_task, text='Удалить')
    btn_delete.grid(row=0, column=7, sticky=NSEW)

    columns_table = {
        'number': ['№', 30, False],
        'name': ['Название проекта', 150, True],
        'description': ['Описание', 200, True],
        'term': ['Срок выполнения', 120, True],
        'priority': ['Приоритет', 100, True],
        'status': ['Статус', 100, True]
    }

    table=configurate_table(frame_task, columns_table)
    table.grid(row=1, column=0, columnspan=8, sticky=NSEW)

def main_menu():
    menu = Menu()

    file_menu = Menu(tearoff=0)
    file_menu.add_command(label = 'Создать проект')
    file_menu.add_command(label = 'Импорт')
    file_menu.add_command(label = 'Экспорт')

    edit_menu = Menu(tearoff=0)
    edit_menu.add_command(label = 'Создать задачу')
    edit_menu.add_command(label='Удалить задачу')

    view_menu = Menu(tearoff=0)
    view_menu.add_command(label='Список задач')
    view_menu.add_command(label='Календарь')

    menu.add_cascade(label='Файл', menu=file_menu)
    menu.add_cascade(label='Правка', menu=edit_menu)
    menu.add_cascade(label='Вид', menu=view_menu)
    menu.add_cascade(label='Помощь')

    return menu