import datetime
from tkinter import *
from tkinter import font, StringVar
from main_win_widget import frame_list_task

from selenium.webdriver.common.devtools.v85.dom import focus
from tkcalendar import Calendar
from config_widget import configurate_grid

def check_entry_data(e : StringVar, x:int):
    pattern = '0123456789'

    if len(e.get())>x:
        e.set(e.get()[0:x])
    if not e.get().isdigit():
        res = ''.join(list(filter(lambda a: a in pattern, e.get())))
        e.set(res)
    else:
        if int(e.get())>31 and e == d:
            e.set('')
        elif int(e.get())>12 and e == m:
            e.set('')


def check_data_focus_out(e : StringVar):
    if e.get() == '' or int(e.get())==0:
        if e == d:
            e.set(str(datetime.date.today().day))
        elif e == m:
            e.set(str(datetime.date.today().month))
        elif e == y:
            e.set(str(datetime.date.today().year))
    global dateCal
    dateCal.set(f'{int(d.get())}.{int(m.get())}.{int(y.get())}')

def entry_data(win):
    frame_data_entry = Frame(win)
    frame_data_entry.pack()

    configurate_grid(frame_data_entry, 1, 5, 0)

    custom_font = font.Font(size=18, weight='bold')
    entry_day = Entry(frame_data_entry, font=custom_font, width=3, justify='center', textvariable=d)
    entry_day.grid(row=0, column=0)
    entry_day.bind('<KeyRelease>', lambda x :check_entry_data(d, 2))
    entry_day.bind('<FocusOut>', lambda x : check_data_focus_out(d))
    entry_day.bind('<Return>', lambda x : entry_month.focus())

    label_sep1 = Label(frame_data_entry, text='/', font=custom_font)
    label_sep1.grid(row=0, column=1)

    entry_month = Entry(frame_data_entry, font=custom_font, width=3, justify='center', textvariable=m)
    entry_month.grid(row=0, column=2)
    entry_month.bind('<KeyRelease>', lambda x : check_entry_data(m, 2))
    entry_month.bind('<FocusOut>', lambda x : check_data_focus_out(m))
    entry_month.bind('<Return>', lambda x : entry_year.focus())

    label_sep2 = Label(frame_data_entry, text='/', font=custom_font)
    label_sep2.grid(row=0, column=3)

    entry_year = Entry(frame_data_entry, font=custom_font, width=6, justify='center', textvariable=y)
    entry_year.grid(row=0, column=4)
    entry_year.bind('<KeyRelease>', lambda x : check_entry_data(y, 4))
    entry_year.bind('<FocusOut>', lambda x : check_data_focus_out(y))
    entry_year.bind('<Return>', lambda x : entry_day.focus())

def calendar_select(event):
    date = datetime.datetime.strptime(dateCal.get(), '%d.%m.%Y').date()
    d.set(str(date.day))
    m.set(str(date.month))
    y.set(str(date.year))

def cal(win):
    frame_calendar = Frame(win)
    frame_calendar.pack(fill=BOTH, expand=True)

    entry_data(frame_calendar)
    calen = Calendar(frame_calendar, locale='ru', textvariable=dateCal)
    calen.pack(fill=BOTH, expand=True)
    calen.bind('<<CalendarSelected>>', calendar_select)


def task(win):
    frame_task = Frame(win, background='red')
    frame_task.pack(fill=BOTH, expand=True)
    configurate_grid(frame_task, 1, 1)
    frame_list_task(frame_task, 0)


win = Tk()
win.title('TaskMaster')
win.geometry('700x500+650+300')
win.minsize(width=700, height=500)

d = StringVar(value=str('%02d' % (datetime.date.today().day)))
m = StringVar(value=str('%02d' % (datetime.date.today().month)))
y = StringVar(value=str('%04d' % (datetime.date.today().year)))
dateCal = StringVar(value=str(f'{int(d.get())}.{int(m.get())}.{int(y.get())}'))


cal(win)
task(win)

win.mainloop()