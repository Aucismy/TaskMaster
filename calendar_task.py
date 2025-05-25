from tkinter import *
from tkcalendar import Calendar
from config_widget import configurate_grid

def entry_data(win):
    frame_data_entry = Frame(win)
    frame_data_entry.pack(fill=X)

    configurate_grid(frame_data_entry, 1, 5)

    entry_day = Entry(frame_data_entry)
    entry_day.grid(row=0, column=0)

    label_sep1 = Label(frame_data_entry, text='/')
    label_sep1.grid(row=0, column=1)

    entry_month = Entry(frame_data_entry)
    entry_month.grid(row=0, column=2)

    label_sep2 = Label(frame_data_entry, text='/')
    label_sep2.grid(row=0, column=3)

    entry_year = Entry(frame_data_entry)
    entry_year.grid(row=0, column=4)


def cal(win):
    frame_calendar = Frame(win)
    frame_calendar.pack(fill=BOTH, expand=True)

    entry_data(frame_calendar)

    calen = Calendar(frame_calendar, locale='ru')
    calen.pack(fill=BOTH, expand=True)

def task(win):
    frame_task = Frame(win, background='red')
    frame_task.pack(fill=BOTH, expand=True)


win = Tk()
win.title('TaskMaster')
win.geometry('700x400+650+300')

cal(win)
task(win)

win.mainloop()