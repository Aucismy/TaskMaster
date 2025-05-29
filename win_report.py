from tkinter import *
from tkinter.ttk import Combobox

from config_widget import configurate_grid
from tkcalendar import DateEntry

def widgets():
    configurate_grid(win, 7, 4)

    label_rep = Label(win, text='Отчёт')
    label_rep.grid(row=0, column=1, columnspan=2, sticky=EW)

    frame_date = Frame(win)
    frame_date.grid(row=2, column=0, columnspan=4, sticky=NSEW)
    configurate_grid(frame_date, 1, 5)
    frame_date.columnconfigure(index=2, weight=0)

    data_entry_ot = DateEntry(frame_date)
    data_entry_ot.grid(row=0, column=1, sticky=E)

    label_do = Label(frame_date, text='-')
    label_do.grid(row=0, column=2, sticky=EW)

    data_entry_do = DateEntry(frame_date)
    data_entry_do.grid(row=0, column=3, sticky=W)

    label_type_report = Label(win, text='Тип отчёта')
    label_type_report.grid(row=3, column=1, sticky=E)

    type_report = Combobox(win, values=['По проектам', 'По приоритетам'])
    type_report.grid(row=3, column=2, sticky=EW)

    canvas_grap = Canvas(win, background='red', height=1)
    canvas_grap.grid(row=4, column=0, columnspan=2, padx=2.5, pady=5, sticky=NSEW)

    canvas_diag = Canvas(win, background='blue')
    canvas_diag.grid(row=4, column=2, columnspan=2, padx=2.5, pady=5, sticky=NSEW)

    button_export = Button(win, text='Экспорт')
    button_export.grid(row=5, column=2, sticky=E, padx=5)

    combo_export = Combobox(win, values=['PDF', 'CSV'], width=10)
    combo_export.grid(row=5, column=3, sticky=W, padx=5)

win = Tk()
win.title('TaskMaster')
win.geometry('600x500+650+300')

widgets()

win.mainloop()