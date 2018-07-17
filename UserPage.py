from tkinter import *
from tkinter.messagebox import *
from AdminLogin import *
from Register import *
import dbconn
import sys
sys.path.append(r'D:\Swk\CodeSpace\Python\tedu\07.12\3-UI版学员管理系统')

cursor = dbconn.cursor
conn = dbconn.conn


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


