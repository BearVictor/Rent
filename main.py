from tkinter import *
import datetime
import tkinter.messagebox as box
import pickle

#Оголосимо постійні змінні
window=Tk()
window.title("Податки")
window.resizable( 0, 0 )#розмір вікна деактивний
window.configure( bg = 'Snow1' )
mas=[]
for ii in range(5):
    i=DoubleVar()
    mas.append(i)

#оголошення усіх віджетів програми
label1 = Label( window,bg="Snow1", font=14 )
label2 = Label( window,bg="Snow1", font=14 )
label3 = Label( window,bg="Snow1", font=14  )
label4 = Label( window,bg="Snow1", font=14 )
label5 = Label( window,bg="Snow1", font=14 )

entry1=Entry(window,textvariable=mas[0])
entry2=Entry(window,textvariable=mas[1])
entry3=Entry(window,textvariable=mas[2])
entry4=Entry(window,textvariable=mas[3])
entry5=Entry(window,textvariable=mas[4])

btn1=Button(window,bg="DarkCyan", font=14)
btn2=Button(window,bg="DarkCyan", font=14)
btn3=Button(window,bg="DarkCyan", font=14)
btn4=Button(window,bg="DarkCyan", font=14)
btn5=Button(window,bg="DarkCyan", font=14)

#розташування
label1.grid(row=1,column=2)
label2.grid(row=2,column=2)
label3.grid(row=3,column=2)
label4.grid(row=4,column=2)
label5.grid(row=5,column=2)

entry1.grid(row=1,column=3)
entry2.grid(row=2,column=3)
entry3.grid(row=3,column=3)
entry4.grid(row=4,column=3)
entry5.grid(row=5,column=3)

btn1.grid(row=1,column=1,rowspan=2)
btn2.grid(row=3,column=1,rowspan=2)
btn3.grid(row=6,column=2,rowspan=2,columnspan=2,pady=10)
btn4.grid(row=1,column=4,rowspan=2,padx=10)
btn5.grid(row=3,column=4,rowspan=2,padx=10)

#оголошення постійних змінних
label1.configure(text="Газ: ")
label2.configure(text="Світло: ")
label3.configure(text="Опалення/гаряча вода: ")
label4.configure(text="Прибирання будинку: ")
label5.configure(text="Холодна вода: ")
btn1.configure(text="Максимальна сума ")
btn2.configure(text="Вивести усі дані ")
btn3.configure(text="Зберегти ")
btn4.configure(text="Мінімальна сума ")
btn5.configure(text="Середня за усі роки сума ")



now = datetime.datetime.now()

#Функції
def Sum():
    return float(entry1.get())+float(entry2.get())+float(entry3.get())+float(entry4.get())+float(entry5.get())
def Zapus(str,file,value):
    file.write(str+ " %15s:" % value+"\n")

def SaveinFile():
    file=open("AllDani.txt","a")
    file.write("*"*50)
    file.write("\n\t"+now.strftime("%d-%B-%Y")+"\n\n")
    Zapus("Газ", file,  entry1.get())
    Zapus("Світло", file, entry2.get())
    Zapus("Опалення/гаряча вода", file, entry3.get())
    Zapus("Прибирання будинку", file, entry4.get())
    Zapus("Холодна вода", file, entry5.get())
    file.write("\n\tСума:\t"+ str(Sum())+"\n")
    file.close()
    dani = {}
    try:
        with open('DANI', 'rb') as f:
            dani=pickle.load(f)
    except IOError :
        open('DANI', 'wb')
    dani[Sum()] = now.strftime("%d-%B-%Y")
    with open('DANI', 'wb') as f:
        pickle.dump(dani, f)

    box.showinfo('Result', 'Дані збережено')

def ReadDigits():
    with open('DANI', 'rb') as f:
            slovnuk = pickle.load(f)
    return slovnuk

def Bmax():
    sl=ReadDigits()
    max=0
    for su in sl.keys():
        if su>max:
            max=su
        continue
    box.showinfo('Максимальна сума була ', str(max)+"UAH  y "+sl[max])
def Bmin():
    sl=ReadDigits()
    min=9999999
    for su in sl.keys():
        if su<min:
            min=su
        continue
    box.showinfo('Мінімальна сума була ', str(min)+"UAH  y "+sl[min])
def ShowALL():
    sl = ReadDigits()
    string=""
    for vv, ww in sl.items():
        string+= ww+": "+str(vv)+"UAH\n"
    box.showinfo("RESULt",string)

def SerAr():
    sl = ReadDigits()
    sum=0
    for i in sl.keys():
        sum+=i

    box.showinfo("Середня сума ",str(sum/len(sl)))

#основна програма

btn1.configure(command=Bmax)
btn4.configure(command=Bmin)
btn3.configure(command=SaveinFile)
btn2.configure(command=ShowALL)
btn5.configure(command=SerAr)
window.mainloop()
