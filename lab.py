'''
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона),
сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие
минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
На плоскости задано К точек. Сформировать все возможные варианты
выбора множества точек из них для формирования всех возможных треугольников.
Только равнобедренные
'''
import itertools
import math
from tkinter import *
from tkinter import ttk

c = 0
strdots = []
dots = []

strtriangles = []
triangles = []

def checkTriangle(l):
    a = math.sqrt((l[0][0] - l[1][0])**2 + (l[0][1] - l[1][1])**2)
    b = math.sqrt((l[2][0] - l[1][0])**2 + (l[2][1] - l[1][1])**2)
    c = math.sqrt((l[0][0] - l[2][0])**2 + (l[0][1] - l[2][1])**2)
    if a >= (b + c): return False
    if b >= (a + c): return False
    if c >= (b + a): return False
    if a == b or b == c or c == a: return True
    return False


root = Tk()
root.geometry('720x480')
root.resizable(False, False)
root.title("Поиик равобедренных треугольников")

labelx = ttk.Label(text="x:")
labelx.place(anchor=NW, x = 15, y = 20, height = 25)
entryx = ttk.Entry()
entryx.place(anchor=NW, x = 30, y = 20, height = 25, width = 80)

labelx = ttk.Label(text="y:")
labelx.place(anchor=NW, x = 125, y = 20, height = 25)
entryy = ttk.Entry()
entryy.place(anchor=NW, x = 140, y = 20, height = 25, width = 80)

labelc = ttk.Label(text="Количество точек : ")
labelc.place(anchor=NW, x = 540, y = 20, height = 25, width = 240)

labelka = ttk.Label(text="Количество треугольников (алгоритм) : ")
labelka.place(anchor=NW, x = 380, y = 400, height = 25, width = 480)

labelkit = ttk.Label(text="Количество треугольников (itertools) : ")
labelkit.place(anchor=NW, x = 380, y = 420, height = 25, width = 480)

dotslist = StringVar(value=strdots)
listboxd = Listbox(listvariable=dotslist)
listboxd.place(anchor=NW, x = 30, y = 65, width = 320, height = 320)

scrollbar = ttk.Scrollbar(orient="vertical", command=listboxd.yview)
scrollbar.place(anchor=NW, y = 65, x = 330, width = 20, height = 320)
listboxd["yscrollcommand"] = scrollbar.set

trianglelist = StringVar(value=strtriangles)
listboxt = Listbox(listvariable=trianglelist)
listboxt.place(anchor=NW, x = 380, y = 65, width = 320, height = 320)

scrollbar = ttk.Scrollbar(orient="vertical", command=listboxt.yview)
scrollbar.place(anchor=NW, y = 65, x = 680, width = 20, height = 320)
listboxt["yscrollcommand"] = scrollbar.set

def addDot():
    global dots, c, entryx, entryy
    c += 1
    dots.append([float(entryx.get()), float(entryy.get())])
    strdots.append("Точка №{:1} : {:2}, {:3}".format(c, dots[-1][0], dots[-1][1]))
    labelc["text"] = "Количество точек : " + str(c)

    dotslist = StringVar(value=strdots)
    listboxd = Listbox(listvariable=dotslist)
    listboxd.place(anchor=NW, x=30, y=65, width=320, height=320)

    scrollbar = ttk.Scrollbar(orient="vertical", command=listboxd.yview)
    scrollbar.place(anchor=NW, y=65, x=330, width=20, height=320)

    listboxd["yscrollcommand"] = scrollbar.set


btn = ttk.Button(text="Добавить точку", command=addDot)
btn.place(anchor=NW, x = 250, y = 20, height = 25, width = 100)

def triangleFunc():
    global triangles
    for i in range(len(dots)):
        for j in range(i+1, len(dots)):
            for k in range(j+1, len(dots)):
                triangles.append([dots[i], dots[j], dots[k]])
    print(*triangles, sep='\n')

    k = 0
    for t in triangles:
        if(checkTriangle(t)):
            k += 1
    labelka["text"] = "Количество треугольников (алгоритм) : " + str(k)

    triangles = list(itertools.combinations(dots, 3))

    print(*triangles, sep='\n')

    k = 0
    for t in triangles:
        if(checkTriangle(t)):
            k += 1
            strtriangles.append("Треугольник №{:1} : {:2}, {:3} ; {:4}, {:5} ; {:6}, {:7}".format(k, t[0][0], t[0][1],
                                                                                                t[1][0], t[1][1],
                                                                                                t[2][0], t[2][1]))
            trianglelist = StringVar(value=strtriangles)
            listboxt = Listbox(listvariable=trianglelist)
            listboxt.place(anchor=NW, x=380, y=65, width=320, height=320)

            scrollbar = ttk.Scrollbar(orient="vertical", command=listboxt.yview)
            scrollbar.place(anchor=NW, y=65, x=680, width=20, height=320)

            listboxt["yscrollcommand"] = scrollbar.set
    labelkit["text"] = "Количество треугольников (itertools) : " + str(k)


btn = ttk.Button(text="Проверить треугольники", command=triangleFunc)
btn.place(anchor=NW, x = 30, y = 400, height = 25, width = 160)

root.mainloop()
