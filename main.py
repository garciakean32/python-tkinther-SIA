import tkinter as tk
from tkinter import messagebox
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='garcia'
)
c = connection.cursor()
root = tk.Tk()

def close_window():
    root.destroy()

class loginForm:
    def __init__(self, master):
        self.master = master

        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        self.master.geometry

        self.frame = tk.Frame(self.master, bg='#fff')
        self.btnsFrame = tk.Label(self.frame, bg='#fff', padx=40, pady=15)
        self.windowTitle = tk.Label(self.frame, text='Login Window')
        self.usernameLabel = tk.Label(self.frame, text='Username:')
        self.usernameTextbox = tk.Entry(self.frame)
        self.passwordLabel = tk.Label(self.frame, text='Password:')
        self.passwordTextbox = tk.Entry(self.frame, show='*')
        self.btnLogin = tk.Button(self.btnsFrame, text='Login', command=self.login_func)
        self.btnCancel = tk.Button(self.btnsFrame, text='Cancel', command=close_window)

        self.frame.pack(fill='both')
        self.windowTitle.grid(row=0, column=0, columnspan=2)
        self.usernameLabel.grid(row=1, column=0)
        self.usernameTextbox.grid(row=1, column=1)
        self.passwordLabel.grid(row=2, column=0, pady=(10, 0))
        self.passwordTextbox.grid(row=2, column=1, pady=(10, 0))
        self.btnsFrame.grid(row=3, column=0, columnspan=2, pady=10)
        self.btnLogin.grid(row=0, column=0, padx=(0, 35))
        self.btnCancel.grid(row=0, column=1)

    def login_func(self):
        username = self.usernameTextbox.get()
        password = self.passwordTextbox.get()
        select_query = 'SELECT * FROM user WHERE username = %s and password = %s'
        vals = (username, password)
        c.execute(select_query, vals)

        user = c.fetchone()
        if user is not None:
            messagebox.showinfo('Nice!', 'Access Granted')
        else:
            messagebox.showwarning('Nice Try..', 'Invalid Username/Password')

def main():
    login_window = loginForm(root)
    root.mainloop()

if __name__ == '__main__':
    main()
