from tkinter import *
from tkinter import messagebox
import sqlite3


def new_registration():
    root.destroy()
    import registration_form

def login():
    if user_ent.get()=='' or pwd_ent.get()=='':
        messagebox.showerror('Error','Empty field not allow')
        root.destroy()
        import registration_form
    else:
        try:
            con = sqlite3.connect( 'registration.db' )
            cur = con.cursor()
            cur.execute( "SELECT email,password FROM userinfo where email=? and password=?", [user_ent.get(),pwd_ent.get()] )
            iteam = cur.fetchone()
            print(iteam)
            if iteam==None:
                    messagebox.showerror( 'Error', 'Wrong ID or Password,Please try again' )
                    user_ent.delete( 0, END )
                    pwd_ent.delete( 0, END )
            else:
                root.destroy()
                import discount_cal

            con.close()
        except Exception as e:
            messagebox.showerror('','Somthing with wrong')

root = Tk()
root.title('Login Page')
root.geometry('500x400+100+100')

login_lbl =Label(root,text='\nLOGIN HERE',font=('Vrinda',20,'underline'),fg='#9042B8',anchor=N)
login_lbl.pack()

user_lbl =Label(root,text='Email ID',font=('Angsana New',20))
user_lbl.place(x=50,y=100)
pwd_lbl = Label(root,text='Password',font=('Angsana New',20))
pwd_lbl.place(x=50,y=180)


user_ent= Entry(root, width=20,font=('Calibri',14),relief=FLAT,highlightthickness=2,bd=2,bg='#9EDBCC',fg='#2B75F0')
user_ent.place(x=150, y=100,width=300,height=30)
pwd_ent= Entry(root, width=20,font=('Calibri',14),show='*',relief=FLAT,highlightthickness=2,bd=2,bg='#9EDBCC',fg='#2B75F0')
pwd_ent.place(x=150, y=180,width=300,height=30)

login_btn = Button(root,text='Login',command=login,font=('Angsana New',15),fg='blue')
login_btn.place(x=320,y=220,height=30)

regi_btn = Button(root,text= 'Registration',command=new_registration,font=('Angsana New',15),fg='blue')
regi_btn.place(x=190,y=220)




chk_var = IntVar()
def chk_pwd():
    if chk_var.get()==1:
        pwd_ent.config(show='')
    else:
        pwd_ent.config(show='*')

chk_butt = Checkbutton(onvalue=1,offvalue=0,command=chk_pwd,variable=chk_var)
chk_butt.place(x=330,y=150)
chk_lbl = Label(root,text='Show Password',font=('Annai MN',10),fg='black')
chk_lbl.place(x=350,y=150)


root.mainloop()
