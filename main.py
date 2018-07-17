from tkinter import *
from tkinter.messagebox import *
# from MainPage import *
import dbconn
cursor = dbconn.cursor
conn = dbconn.conn

class AdminPage(object):
	def __init__(self, master=None, id=None):
		self.root = master
		# self.root.geometry('%dx%d' % (600, 400))

		self.id = id
		self.rowNum = 2
		self.editId = StringVar()
		self.editName = StringVar()
		self.editPass = StringVar()
		self.editLevel = StringVar()
		self.deleteId = StringVar()
		self.addName = StringVar()
		self.addPass = StringVar()
		self.createPage()

	def createPage(self):
		self.mainFramePage = Frame(self.root)
		self.mainFramePage.pack()

		self.displayPage = Frame(self.mainFramePage)
		self.editPage = Frame(self.mainFramePage)
		self.buttonPage = Frame(self.mainFramePage)

		self.displayPage.grid(row=0, rowspan=2)
		self.buttonPage.grid(row=0, column=1, sticky=N, rowspan=1)
		self.editPage.grid(row=1, column=1, rowspan=1)

		self.updatePage = Frame(self.editPage)
		self.deletePage = Frame(self.editPage)
		self.addPage = Frame(self.editPage)

		self.page = Frame(self.displayPage)
		self.page.pack()
		self.bPage = Frame(self.buttonPage)
		self.bPage.pack()
		Label(self.page).grid(row=0, stick=W)
		Label(self.page).grid(row=0, stick=W)
		Label(self.page, text='id').grid(row=1, column=0, stick=W, pady=10)
		Label(self.page, text='name').grid(row=1, column=1, stick=W, pady=10)
		Label(self.page, text='pass').grid(row=1, column=2, stick=W, pady=10)
		Label(self.page, text='level').grid(row=1, column=3, stick=W, pady=10)
		Label(self.page, text='\t      |      \t').grid(row=1, column=4, stick=W, pady=10)

		Button(self.bPage, text='增加', command=self.add).grid(row=0, column=0, pady=10, padx=10)
		Button(self.bPage, text='修改', command=self.update).grid(row=0, column=1, pady=10, padx=10)
		Button(self.bPage, text='删除', command=self.delete).grid(row=0, column=2,  pady=10, padx=10)
		Button(self.bPage, text='返回', command=self.back).grid(row=0, column=3, pady=10, padx=10)
		self.getAllUsers()

	def getAllUsers(self):
		cursor.execute('SELECT * FROM students')
		users = cursor.fetchall()
		usersLen = len(users)
		for i in range(usersLen):
			Label(self.page, text=users[i][0]).grid(row=self.rowNum+i, column=0, stick=W, pady=10)
			Label(self.page, text=users[i][1]).grid(row=self.rowNum+i, column=1, stick=W, pady=10)
			Label(self.page, text=users[i][2]).grid(row=self.rowNum+i, column=2, stick=W, pady=10)
			Label(self.page, text=users[i][3]).grid(row=self.rowNum+i, column=3, stick=W, pady=10)
			Label(self.page, text='\t      |      \t').grid(row=self.rowNum+i, column=4, stick=W, pady=10)
		return users

	def add(self):
		self.deletePage.pack_forget()
		self.updatePage.pack_forget()
		self.addPage.pack()
		Label(self.addPage).grid(row=0)

		Label(self.addPage).grid(row=0)
		Label(self.addPage, text='用户名: ').grid(row=1, sticky=W, pady=10)
		Entry(self.addPage, textvariable=self.addName).grid(row=1, column=1, sticky=E)
		Label(self.addPage, text='密码: ').grid(row=2, sticky=W, pady=10)
		Entry(self.addPage, textvariable=self.addPass).grid(row=2, column=1, sticky=E)
		Button(self.addPage, text='添加', command=self.addsubmit).grid(row=3, pady=10)

	def update(self):
		self.addPage.pack_forget()
		self.deletePage.pack_forget()
		self.updatePage.pack()
		Label(self.updatePage).grid(row=0)
		Label(self.updatePage, text='用户ID: ').grid(row=1, sticky=W, pady=10)
		Entry(self.updatePage, textvariable=self.editId).grid(row=1, column=1, sticky=E)
		Label(self.updatePage, text='用户名: ').grid(row=2, sticky=W, pady=10)
		Entry(self.updatePage, textvariable=self.editName).grid(row=2, column=1, sticky=E)
		Label(self.updatePage, text='密码: ').grid(row=3, pady=10, sticky=W)
		Entry(self.updatePage, textvariable=self.editPass, show='*').grid(row=3, column=1, sticky=E)
		Label(self.updatePage, text='权限: ').grid(row=4, pady=10, sticky=W)
		Entry(self.updatePage, textvariable=self.editLevel).grid(row=4, column=1, sticky=E)
		Button(self.updatePage, text='确定修改', command=self.updatesubmit).grid(row=5, pady=10)

	def delete(self):
		self.addPage.pack_forget()
		self.updatePage.pack_forget()
		self.deletePage.pack()
		Label(self.deletePage).grid(row=0)
		Label(self.deletePage, text='用户ID: ').grid(row=1, sticky=W, pady=10)
		Entry(self.deletePage, textvariable=self.deleteId).grid(row=1, column=1, sticky=E)
		Button(self.deletePage, text='确定删除', command=self.deletesubmit).grid(row=5, pady=10)

	def updatesubmit(self):
		id = self.editId.get()
		name = self.editName.get()
		pw = self.editPass.get()
		lev = self.editLevel.get()
		if id is None or id == "":
			showinfo(title='提示', message='请输入要修改用户的ID！')
		else:
			id = int(id)
			cursor.execute('SELECT * FROM students WHERE id = "%d"' %id)
			user = cursor.fetchall()
			if len(user) < 1:
				showinfo(title='提示', message='没有该用户！')
			else:
				if name is None or name == "":
					name = user[0][1]

				if pw is None or pw == "":
					pw = user[0][2]

				if lev is None or lev == "":
					lev = user[0][3]
				else:
					lev = int(lev)

				cursor.execute(
					'UPDATE students SET name = "%s", password = "%s", level = %d WHERE id = %d' % (name, pw, lev, id))
				conn.commit()
				showinfo(title='提示', message='修改成功！')
				self.mainFramePage.pack_forget()
				self.createPage()
				# self.displayPage.destroy()
				# self.buttonPage.destroy()
				# self.editPage.destroy()

	def deletesubmit(self):
		id = self.deleteId.get()
		if id is None or id == "":
			showinfo(title='提示', message='请输入要修改用户的ID！')
		else:
			id = int(id)
			cursor.execute('DELETE FROM students WHERE id = %d' %id)
			conn.commit()
			if cursor.rowcount < 1:
				showinfo(title='提示', message='没有该用户！')
			else:
				showinfo(title='提示', message='删除成功！')
				self.mainFramePage.pack_forget()
				self.createPage()

	def addsubmit(self):
		userName = self.addName.get()
		userPass = self.addPass.get()
		if userName == "" or userPass == "":
			showinfo(title='提示', message='请填入完整信息！')
		else:
			cursor.execute('INSERT INTO students(name, password, level) VALUES("%s", "%s", %d)' % (userName, userPass, 2))
			conn.commit()
			showinfo(title='提示', message='添加成功！')
			self.mainFramePage.pack_forget()
			self.createPage()


	def back(self):
		# self.displayPage.destroy()
		# self.editPage.destroy()
		# self.buttonPage.destroy()
		self.mainFramePage.destroy()
		MainPage(self.root)


class UserPage(object):
	def __init__(self, master=None, id=None):
		self.root = master
		self.id = id
		self.editpage = Frame(self.root)
		self.Name = StringVar()
		self.Pass = StringVar()
		self.data = StringVar()
		self.root.geometry('%dx%d' % (600, 400))
		self.userName = StringVar()
		self.userPass = StringVar()
		self.createPage()

	def createPage(self):
		self.page = Frame(self.root)
		self.page.pack()
		Label(self.page).grid(row=0, stick=W)
		Label(self.page, text='id').grid(row=1, column=0, stick=W, pady=10)
		Label(self.page, text='name').grid(row=1, column=2, stick=W, pady=10)
		Label(self.page, text='pass').grid(row=1, column=4, stick=W, pady=10)
		Label(self.page, text='level').grid(row=1, column=6, stick=W, pady=10)
		self.data = self.getInfo()
		Button(self.page, text='修改信息', command=self.edit).grid(row=3, column=0)
		Button(self.page, text='返回主页面', command=self.back).grid(row=3, column=6)

	def getInfo(self):
		cursor.execute('SELECT * FROM students WHERE id = "%d"' % self.id)
		users = cursor.fetchone()
		Label(self.page, text=users[0]).grid(row=2, column=0, stick=W, pady=10)
		Label(self.page, text=users[1]).grid(row=2, column=2, stick=W, pady=10)
		Label(self.page, text=users[2]).grid(row=2, column=4, stick=W, pady=10)
		Label(self.page, text=users[3]).grid(row=2, column=6, stick=W, pady=10)
		return users[0]

	def edit(self):
		self.editpage.pack()
		Label(self.editpage).grid(row=5, stick=W)

		Label(self.editpage, text='用户名: ').grid(row=1, stick=W, pady=10)
		Entry(self.editpage, textvariable=self.Name).grid(row=1, column=1, stick=E)
		Label(self.editpage, text='密码: ').grid(row=2, stick=W, pady=10)
		Entry(self.editpage, textvariable=self.Pass, show='*').grid(row=2, column=1, stick=E)
		Button(self.editpage, text='确定修改', command=self.submit).grid(row=3, stick=W, pady=10)

	def submit(self):
		name = self.Name.get()
		pw = self.Pass.get()
		if name is None:
			name = self.data[1]
		if pw is None:
			pw = self.data[2]
		cursor.execute('UPDATE students SET name = "%s", password = "%s", level = %d WHERE id = %d' % (name, pw, 2, self.id))
		conn.commit()
		showinfo(title='提示', message='修改成功！')
		self.editpage.pack_forget()
		self.page.pack_forget()
		self.createPage()

	def back(self):
		self.page.destroy()
		self.editpage.destroy()
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


class Register(object):
	def __init__(self, master=None):
		self.root = master
		self.root.geometry('%dx%d' % (600, 400))
		self.adminName = StringVar()
		self.adminPass = StringVar()
		self.createPage()

	def createPage(self):
		self.page = Frame(self.root)
		self.page.pack()
		Label(self.page).grid(row=0, stick=W)

		Label(self.page).grid(row=0, stick=W)
		Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
		Entry(self.page, textvariable=self.adminName).grid(row=1, column=1, stick=E)
		Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
		Entry(self.page, textvariable=self.adminPass, show='*').grid(row=2, column=1, stick=E)
		Button(self.page, text='注册', command=self.regi).grid(row=3, stick=W, pady=10)
		Button(self.page, text='返回', command=self.back).grid(row=3, column=1, stick=E)

	def regi(self):
		regUser = self.adminName.get()
		regPw = self.adminPass.get()
		if regUser == "" or regPw == "":
			showinfo(title='提示', message='请填入完整信息！')
		else:
			cursor.execute('INSERT INTO students(name, password, level) VALUES("%s", "%s", %d)' % (regUser, regPw, 2))
			conn.commit()
			showinfo(title='提示', message='注册成功！')
			self.page.destroy()
			MainPage(self.root)

	def back(self):
		self.page.destroy()
		MainPage(self.root)


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
				UserPage(self.root, data[0])

	def back(self):
		self.page.destroy()
		MainPage(self.root)

class AdminLogin(object):
	def __init__(self, master=None):
		self.root = master
		self.root.geometry('%dx%d' % (600, 400))
		self.adminName = StringVar()
		self.adminPass = StringVar()
		self.createPage()

	def createPage(self):
		self.page = Frame(self.root)
		self.page.pack()
		Label(self.page).grid(row=0, stick=W)
		Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
		Entry(self.page, textvariable=self.adminName).grid(row=1, column=1, stick=E)
		Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
		Entry(self.page, textvariable=self.adminPass, show='*').grid(row=2, column=1, stick=E)
		Button(self.page, text='登录', command=self.login).grid(row=3, stick=W, pady=10)
		Button(self.page, text='返回', command=self.back).grid(row=3, column=1, stick=E)

	def login(self):
		adminName = self.adminName.get()
		adminPass = self.adminPass.get()
		cursor.execute('SELECT * FROM students WHERE name = "%s"' % adminName)
		data = cursor.fetchone()
		if data is None:
			showinfo(title="错误", message="请输入正确的用户名！")
		else:
			if data[2] != adminPass:
				showinfo(title="错误", message="密码错误！")
			else:
				if data[3] != 1:
					showinfo(title="错误", message="您的权限等级过低！")
				else:
					showinfo(title="提示", message="登录成功！")
					self.page.destroy()
					AdminPage(self.root, data[0])

	def back(self):
		self.page.destroy()
		MainPage(self.root)

root = Tk()
root.title("学员管理系统")
MainPage(root)
root.mainloop()