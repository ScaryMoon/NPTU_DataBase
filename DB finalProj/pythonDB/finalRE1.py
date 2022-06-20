from tkinter import ttk
import tkinter as tk
import mysql.connector as mysql
import tkinter.font as tkFont


account = mysql.connect(user="root", password="123456789",
                        host="localhost", database="test123")
cursor = account.cursor()


# ------------------------------------function-----------------------------------------
class window():
    def __init__(self, win):
        self.win = win
        self.win.title("test")
        self.win.geometry("1920x1080")
        self.win.config(bg="#e2e2e2")
        desktop(self.win)


class desktop():
    def __init__(self, win):
        self.win = win
        self.frame = tk.Frame(self.win)
        self.frame.place(x=57, y=100, width=1800, height=1080)

        self.table = ttk.Treeview(self.frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9),  # 幾行 (直行橫列)
                                  show="headings", height=45)  # 只有tree / headings  # height=1次顯示幾行
        self.table.pack()
        self.headInitial()

        self.btn1 = tk.Button(self.win, height=1, width=10, text="Search1",
                              command=lambda: self.change(1))
        self.btn1.place(x=50, y=0)
        self.btn2 = tk.Button(self.win, height=1, width=10, text="Search2",
                              command=lambda: self.change(2))
        self.btn2.place(x=170, y=0)
        self.btn3 = tk.Button(self.win, height=1, width=10, text="Search3",
                              command=lambda: self.change(3))
        self.btn3.place(x=290, y=0)
        self.btn4 = tk.Button(self.win, height=1, width=10, text="Search4",
                              command=lambda: self.change(4))
        self.btn4.place(x=410, y=0)
        self.btn5 = tk.Button(self.win, height=1, width=10, text="Search5",
                              command=lambda: self.change(5))
        self.btn5.place(x=530, y=0)
        self.btn6 = tk.Button(self.win, height=1, width=10, text="Search6",
                              command=lambda: self.change(6))
        self.btn6.place(x=650, y=0)
        self.btn0 = tk.Button(self.win, height=1, width=15, text="SQL Language",
                              command=lambda: self.change(0))
        self.btn0.place(x=770, y=0)

    def headInitial(self,):
        self.heads = ['a', 'b', 'c', 'd', 'e',
                      'f', 'g', 'h', 'i']  # heading initial
        self.count = 1
        for self.head in self.heads:
            self.table.heading(self.count, text=self.head)
            self.count = self.count+1

    def change(self, btnNomber):
        self.destroyBTN()
        self.frame.destroy()
        Search(self.win, btnNomber)

    def destroyBTN(self,):
        self.btn0.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.btn4.destroy()
        self.btn5.destroy()
        self.btn6.destroy()

# tab


class Search():
    def __init__(self, win, btnNomber):
        self.win = win
        self.frame = tk.Frame(self.win)
        self.frame.place(x=57, y=100, width=1800, height=1080)

        self.table = ttk.Treeview(self.frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9),  # 幾行 (直行橫列)
                                  show="headings", height=45)  # 只有tree / headings  # height=1次顯示幾行
        self.table.pack()
        desktop.headInitial(self)

        if btnNomber == 0:
            self.lb = tk.Label(self.win, text="SQL Search")
            self.lb2 = tk.Label(self.win, text="head")
            self.lb2.place(x=167, y=0)
        elif btnNomber == 1:
            self.lb = tk.Label(self.win, text="Grade")
        elif btnNomber == 2:
            self.lb = tk.Label(self.win, text="Level")
        elif btnNomber == 3:
            self.lb = tk.Label(self.win, text="daystime")
        elif btnNomber == 4:
            self.lb = tk.Label(self.win, text="DName")
        elif btnNomber == 5:
            self.lb = tk.Label(self.win, text="Credits")
        elif btnNomber == 6:
            self.lb = tk.Label(self.win, text="Year")
        self.lb.place(x=57, y=0)

        self.text = tk.Text(self.win, height=10, bg="#f1f1f1")  # SQL
        self.text.place(x=57, y=30, width=600, height=63)

        self.font = tkFont.Font(family="Arial", size=16, weight="bold")
        self.text.configure(font=self.font)
        if btnNomber == 0:
            self.text2 = tk.Text(self.win, height=10, bg="#f1f1f1")
            self.text2.place(x=207, y=0, width=200, height=30)
            self.text2.configure(font=self.font)

        self.btnBack = tk.Button(self.win, height=1, width=10, text="back",
                                 command=lambda: self.change())
        self.btnBack.place(x=1690, y=0)
        self.btn = tk.Button(self.win, height=1, width=10,
                             text="Search", command=lambda: self.find(btnNomber))
        self.btn.place(x=658, y=30)

    def find(self, btnNomber):
        self.getText = self.text.get("1.0", "end")
        if btnNomber == 0:
            text1 = self.getText
            h = self.text2.get("0.0", "end")
            if h != '\n':
                heads = h.split(",")
                print("i am a head and:", h, " and:", heads)
            else:
                heads = []

        elif btnNomber == 1:
            text1 = "select SId,Grade from takes where Grade "+self.getText
            heads = ['SId', 'Grade', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        elif btnNomber == 2:
            text1 = "select CoName,level from course where Level "+self.getText
            heads = ['CoName', 'level', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        elif btnNomber == 3:
            text1 = "select daystime,year,secid from section  where daystime "+self.getText
            heads = ['daystime', 'year',
                     'secid', 'd', 'e', 'f', 'g', 'h', 'i']
        elif btnNomber == 4:
            text1 = "select SId,Major,DName from student,dept where student.HAS=DName and DName "+self.getText
            heads = ['SId', 'Major', 'DName', 'd', 'e', 'f', 'g', 'h', 'i']
        elif btnNomber == 5:
            text1 = "select CoName,Credits,OFFERS,DPhone from dept,course where OFFERS=DName and Credits "+self.getText
            heads = ['CoName', 'Credits', 'OFFERS',
                     'DPhone', 'e', 'f', 'g', 'h', 'i']
        elif btnNomber == 6:
            text1 = "select FName,LName,Major,Section.SecId,Grade,year from student,section,takes where student.SId=takes.SId and takes.SecID=section.SecId and Year "+self.getText
            heads = ['FName', 'LName', 'Major',
                     'Section.SecId', 'Grade', 'year', 'g', 'h', 'i']
        self.headAdjust(heads)
        cursor.execute(text1)

        for i in self.table.get_children():
            self.table.delete(i)
        X = cursor.fetchall()
        for value in X:
            self.table.insert('', 'end', values=value)

    def headAdjust(self, heads):
        if heads != []:
            count = 1
            for head in heads:
                self.table.heading(count, text=head)
                count = count+1

    def change(self,):
        try:
            self.lb2.destroy()
            self.text2.destroy()
        except:
            pass
        self.btn.destroy()
        self.btnBack.destroy()
        self.text.destroy()
        self.lb.destroy()
        self.frame.destroy()
        desktop(self.win)


win = tk.Tk()
window(win)

style = ttk.Style()
style.theme_use("default")
win.mainloop()


account.close()


# 1. 符合輸入分數的學生 顯示學生id , 課程id , 得到分數
# select SId,Grade from takes where Grade
# {ex:>/=/< 60}

# 2. 符合輸入Level的課程 顯示課程的名字, 課程的等級
# select CoName,level from course where Level
# {ex: = / != 'L1'}

# 3. 符合輸入時間的課程  顯示年分,下午,課程id
# select daystime,year,secid from section  where year>=2012 and daystime
# {ex:=/!= '下午'}

# 4. 符合輸入某系辦 顯示某系辦內所有學生id ,學生的專業 , 輸入的某系辦
# select SId,Major,DName from student,dept where student.HAS=DName and DName
# {ex:=/!= '工系辦'}

# 5. 符合輸入學分的課有哪些? 顯示課程名稱、學分、所屬的系辦、系辦的電話
# select CoName,Credits,OFFERS,DPhone from dept,course where OFFERS=DName and Credits
# {ex:=/!= 2}

# 6. 輸入年份X  顯示學生的前名字、後名字、專業,在X年開的課程Id、得到成績、開設課程的年份
# select FName,LName,Major,Section.SecId,Grade,year from student,section,takes
# where student.SId=takes.SId and takes.SecID=section.SecId and Year
# {ex:=/!= 2000}
