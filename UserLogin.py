from tkinter import *
from tkinter.messagebox import *
# from adminLogin import *
# from userLogin import *
# from register import *
import dbconn
import sys
sys.path.append(r'D:\Swk\CodeSpace\Python\tedu\07.12\3-UI版学员管理系统')

cursor = dbconn.cursor
conn = dbconn.conn


class UserLogin(object):
	def __init__(self, master=None):
		self.root = master
		self.root.geometry('%dx%d' % (600, 400))
		self.userName = StringVar()
		self.userPass = StringVar()
		self.createPage()

	def createPage(self):
		self.page = Frame(self.root)
		self.page.pack()
		Label(self.page).grid(row=0, stick=W)

		Label(self.page).grid(row=0, stick=W)
		Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
		Entry(self.page, textvariable=self.userName).grid(row=1, column=1, stick=E)
		Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
		Entry(self.page, textvariable=self.userPass, show='*').grid(row=2, column=1, stick=E)
		Button(self.page, text='登录', command=self.login).grid(row=3, stick=W, pady=10)
		Button(self.page, text='返回', command=self.back).grid(row=3, column=1, stick=E)

	def login(self):
		userName = self.userName.get()
		userPass = self.userPass.get()
		cursor.execute('SELECT * FROM students WHERE name = "%s"' % userName)
		data = cursor.fetchone()
		if data is None:
			showinfo(title="错误", message="请输入正确的用户名！")
		else:
			if data[2] != userPass:
				showinfo(title="错误", message="密码错误！")
			else:
				showinfo(title="提示", message="登录成功！")
				self.page.destroy()
				UserPage(self.root)

	def back(self):
		showinfo(title="提示", message="返回！")
		self.page.destroy()
		MainPage(self.root)


class MainPage(object):
	def __init__(self, master=None):
		self.root = master
		self.root.geometry('%dx%d' % (600, 400))
		self.createPage()

	def createPage(self):
		self.page = Frame(self.root)
		self.page.pack()
		Label(self.page).grid(row=0, stick=W)

		Button(self.page, text='Administrator', command=self.admin).grid(row=1, stick=W, pady=20)
		Button(self.page, text='General  User', command=self.user).grid(row=2, stick=W, pady=20)
		Button(self.page, text=' Registration ', command=self.reg).grid(row=3, stick=W, pady=20)
		Button(self.page, text='Quit The Page', command=self.page.quit).grid(row=4, stick=W, pady=20)

	def admin(self):
		self.page.destroy()
		AdminLogin(self.root)

	def user(self):
		self.page.destroy()
		UserLogin(self.root)

	def reg(self):
		self.page.destroy()
		Register(self.root)

class UserPage(object):
	def __init__(self, master=None):
		self.root = master
		self.root.geometry('%dx%d' % (600, 400))
		self.userName = StringVar()
		self.userPass = StringVar()
		self.createPage()

	def createPage(self):
		self.page = Frame(self.root)
		self.page.pack()
		Label(self.page).grid(row=0, stick=W)
		Label(self.page, text='id').grid(row=1, column=0, stick=W, pady=10)
		Label(self.page, text='name').grid(row=1, column=1, stick=W, pady=10)
		Label(self.page, text='pass').grid(row=1, column=2, stick=W, pady=10)
		Label(self.page, text='level').grid(row=1, column=3, stick=W, pady=10)