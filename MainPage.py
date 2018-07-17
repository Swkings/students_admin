from tkinter import *
from tkinter.messagebox import *
from AdminLogin import *
from UserLogin import *
from Register import *
import sys
sys.path.append(r'D:\Swk\CodeSpace\Python\tedu\07.12\3-UI版学员管理系统')


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
