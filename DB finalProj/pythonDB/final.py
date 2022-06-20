from tkinter import ttk
import tkinter as tk
import mysql.connector as mysql
import tkinter.font as tkFont

account = mysql.connect(user="root", password="123456789",
                        host="localhost", database="MidProj")

cursor = account.cursor()


win = tk.Tk()
win.title("test")
win.geometry("1920x1080")
win.config(bg="#e2e2e2")

frame = tk.Frame(win)
frame.place(x=57, y=100, width=1800, height=1080)
table = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9),  # 幾行 (直行橫列)
                     show="headings", height=45)  # 只有tree / headings  # height=1次顯示幾行

# color
style = ttk.Style()
# theme主題可以把資料以外的空個改顏色
style.theme_use("default")  # default alt clam
# style.configure("Treeview",
#                 background="#d3d3d3",
#                 foreground='black',
#                 rowheight=35,  # 每個資料的高度
#                 fieldbackground="#d3d3d3"
#                 )
table.pack()

# table.heading(1, text="student")
# table.heading(2, text="ID")
# table.heading(3, text="country")


def headInitial():
    heads = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']  # heading initial
    count = 1
    for head in heads:
        table.heading(count, text=head)
        count = count+1


textExample = tk.Text(win, height=10, bg="#f1f1f1")  # SQL
textExample1 = tk.Text(win, height=10, bg="#f1f1f1")  # head

textExample.place(x=57, y=0, width=800, height=90)
textExample1.place(x=1300, y=0, width=556, height=90)

fontExample = tkFont.Font(family="Arial", size=16, weight="bold")
textExample.configure(font=fontExample)
textExample1.configure(font=fontExample)

btnRead = tk.Button(win, height=1, width=10,
                    text="GetText", command=lambda: btnSearch(textExample.get("1.0", "end"), textExample1.get("0.0", "end")))
btnRead.place(x=860, y=0)


def btnSearch(text, headiiing):
    headInitial()
    if(headiiing != '\n'):
        count = 1
        print("headiiing:", headiiing)
        headsplit = headiiing.split(",")
        for head in headsplit:
            table.heading(count, text=head)
            count = count+1
    for i in table.get_children():
        table.delete(i)
    cursor.execute(text)
    X = cursor.fetchall()
    for value in X:
        table.insert('', 'end', values=value)


# --------------------------------------------------------------------------------
# search 1
text1 = "select SId,Grade from takes where Grade>=60"
head1 = "SId,Grade"
btn1 = tk.Button(win, height=1, width=10, text="Search1",
                 command=lambda: btnSearch(text1, head1))

# search 2
text2 = "select CoName,level from course where Level='L1'"
head2 = "CoName,level"
btn2 = tk.Button(win, height=1, width=10, text="Search2",
                 command=lambda: btnSearch(text2, head2))

# search 3
text3 = "select daystime,year,secid from section  where year>=2012 and daystime='下午'"
head3 = "daystime,year,secid"
btn3 = tk.Button(win, height=1, width=10, text="Search3",
                 command=lambda: btnSearch(text3, head3))

# search 4
text4 = "select SId,Major,DName from student,dept where student.HAS=DName and DName='工系辦'"
head4 = "SId,Major,DName"
btn4 = tk.Button(win, height=1, width=10, text="Search4",
                 command=lambda: btnSearch(text4, head4))

# search 5
text5 = "select CoName,Credits,OFFERS,DPhone from dept,course where OFFERS=DName and Credits=3"
head5 = "CoName,Credits,OFFERS,DPhone"
btn5 = tk.Button(win, height=1, width=10, text="Search5",
                 command=lambda: btnSearch(text5, head5))

# search 6
text6 = "select FName,LName,Major,Section.SecId,Grade,year from student,section,takes where student.SId=takes.SId and takes.SecID=section.SecId and Year='2000'"
head6 = "FName,LName,Major,Grade,year"
btn6 = tk.Button(win, height=1, width=10, text="Search6",
                 command=lambda: btnSearch(text6, head6))


btn1.place(x=980, y=0)
btn2.place(x=980, y=32)
btn3.place(x=980, y=64)
btn4.place(x=1100, y=0)
btn5.place(x=1100, y=32)
btn6.place(x=1100, y=64)
win.mainloop()

account.close()


# ----------------------------------------------------------------------------------------------
# 1
# 顯示有及格的學生的Sid跟分數?
# select SId,Grade from takes where Grade>=60

# 顯示哪些課程是level1?
# select CoName,level from course where Level='L1'

# 顯示在 哪些是下午才上課?
# select daystime,year,secid from section  where year>=2012 and daystime='下午'


# 2
# 工程類內有哪些學生分別是那些系?      (資工 電機 屬於工系)
#  select SId,Major,DName from student,dept where student.HAS=DName and DName="工系辦"

# 所有的系開設哪些課是屬於3學分的?聯絡電話分別?
# select CoName,Credits,OFFERS,DPhone from dept,course where OFFERS=DName and Credits=3


# 3
# 哪些學生在2000年開的哪些課得到成績的成績是多少?
# select FName,LName,Major,Section.SecId,Grade,year from student,section,takes where student.SId=takes.SId and takes.SecID=section.SecId and Year='2000'
