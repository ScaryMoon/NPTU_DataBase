import tkinter as tk


class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('Base page')
        self.root.geometry('1000x1000')

        initface(self.root)


class initface():
    def __init__(self, master):

        self.master = master
        self.master.config(bg='green')
        # 基準介面initface
        self.initface = tk.Frame(self.master,)
        self.initface.pack()
        self.btn = tk.Button(self.initface, text='change', command=self.change)
        self.btn.pack()

    def change(self,):
        self.initface.destroy()
        face1(self.master)


class face1():
    def __init__(self, master):
        self.master = master
        self.master.config(bg='blue')
        self.face1 = tk.Frame(self.master,)
        self.face1.pack()
        btn_back = tk.Button(self.face1, text='face1 back', command=self.back)
        btn_back.place(x=600, y=200)

    def back(self):
        self.face1.destroy()
        initface(self.master)


if __name__ == '__main__':
    root = tk.Tk()
    basedesk(root)
    root.mainloop()


# class SampleApp(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self._frame = None
#         self.switch_frame(StartPage)

#     def switch_frame(self, frame_class):
#         new_frame = frame_class(self)
#         if self._frame is not None:
#             self._frame.destroy()
#         self._frame = new_frame
#         self._frame.pack()


# class StartPage(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(
#             side="top", fill="x", pady=5)
#         tk.Button(self, text="Go to page one",
#                   command=lambda: master.switch_frame(PageOne)).pack()
#         tk.Button(self, text="Go to page two",
#                   command=lambda: master.switch_frame(PageTwo)).pack()


# class PageOne(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self, bg='blue')
#         tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(
#             side="top", fill="x", pady=5)
#         tk.Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()


# class PageTwo(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self, bg='red')
#         tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(
#             side="top", fill="x", pady=5)
#         tk.Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()


# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()
