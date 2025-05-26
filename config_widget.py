from tkinter import *
from tkinter import ttk

def configurate_grid(win:Tk|Frame, row_count:int, column_count:int, wei:int = 1):
    for r in range(row_count): win.rowconfigure(index=r, weight=wei)
    for c in range(column_count): win.columnconfigure(index=c, weight=wei)

def configurate_table(win: Tk|Frame, dict_columns):
    table = ttk.Treeview(win, columns=list(dict_columns.keys()), show='headings')
    for k, v in dict_columns.items():
        table.heading(k, text=v[0])
        table.column(k, minwidth=v[1], width=v[1], stretch=v[2])

    return table