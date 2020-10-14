import webbrowser
import tkinter
from tkinter import * 
from tkinter import messagebox

top = tkinter.Tk()
top.geometry('300x300')
top.title('What Happened on Your Birthday')

'''Label Logic for Year, Month, Day '''
YearLabel = Label(top, fg='light blue',
                     bg='dark blue', 
                    text='What Year Were You Born In?'
                    ).pack()

Years = ['1980','1981','1982','1983','1984','1985','1986','1987','1988','1989',
    '1981','1982','1983','1984','1985','1986','1987','1988','1989','1990',
    '1991','1992','1993','1994','1995','1996','1997','1998','1999',
'2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010',
'2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'] # Year drop down choices

Yearsvari = StringVar(top)
Yearsvari.set(Years[0]) #default value

w = OptionMenu(top, Yearsvari, *Years)
w.pack()

MonthLabel = Label(top, fg='light blue',
                     bg='dark blue', 
                    text='What Month Were You Born In?',
                    ).pack()

Months = ['January','February','March',
            'April','May','June',
            'July','August','September',
            'October','November','December'] # Year drop down choices

Monthsvari = StringVar(top)
Monthsvari.set(Months[0]) #default value

w = OptionMenu(top, Monthsvari, *Months)
w.pack()

DayLabel = Label(top, fg='light blue',
                     bg='dark blue', 
                    text='What Day Were You Born On?'
                    ).pack()

Days = ['1','2','3','4','5','6','7','8','9','10',
        '11','12','13','14','15','16','17','18','19',
        '20','21','22','23','25','26','27','28','29','30','31'] # Year drop down choices

Daysvari = StringVar(top)
Daysvari.set(Days[0]) #default value

w = OptionMenu(top, Daysvari, *Days)
w.pack()

'Logic for saving the year,month,day and creating the link'

def BirthdayChoice():
    year = Yearsvari.get()
    month = Monthsvari.get()
    day = Daysvari.get()
    new = 1
    birthday = 'www.onthisday.com/date/'+year+'/'+month+'/'+day
    webbrowser.open(birthday,new=new)

BirthdayButton = tkinter.Button(top, text='What Happened!', command = BirthdayChoice)
BirthdayButton.pack()

top.mainloop()
BirthdayChoice()
