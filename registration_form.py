from tkinter import *
from tkinter import messagebox
import sqlite3

window=Tk()
window.geometry('750x500+300+150')
window.title('Registration Form')

registration_lbl =Label(window,text='\nREGISTAR HERE',font=('Vrinda',20,'underline'),fg='#9042B8',anchor=N)
registration_lbl.pack()

def save():

    Sp_ch = ['$', '@', '#', '%']
    if fname_ent.get()=='' or entry_emil.get()=='' or pwd_entr=='' or c_pwd=='' :
        messagebox.showerror('Error','All fields are required')
    elif len( pwd_entr.get() ) < 6 or len( pwd_entr.get() ) > 10:
        messagebox.showerror( 'Error', 'Password must be more than 6 ch and less than 10 Ch' )
    elif not any( i.isdigit() for i in pwd_entr.get() ):
        messagebox.showerror( 'Error', 'Password must have a numeric value' )
    elif not any( i.isupper() for i in pwd_entr.get() ):
        messagebox.showerror( 'Error', 'Password must have a upper Char' )
    elif not any( i.islower() for i in pwd_entr.get() ):
        messagebox.showerror( 'Error', 'Password must have a lower Char' )
    elif not any( i in Sp_ch for i in pwd_entr.get() ):
        messagebox.showerror( 'Error', 'Password must have a special Char' )
    elif pwd_entr.get()!= c_pwd.get():
        messagebox.showerror('Error', 'Password should be matched' )
        pwd_entr.delete( 0, END )
        c_pwd.delete( 0, END )
    else:
        try:
            con = sqlite3.connect( 'registration.db' )
            cur = con.cursor()
            cur.execute( """ CREATE TABLE IF NOT EXISTS userinfo(
                                fname TEXT NOT NULL,
                                lname TEXT,
                                email TEXT NOT NULL,
                                password TEXT NOT NULL,
                                c_password TEXT NOT NULL )""" )

            cur.execute( "SELECT * FROM userinfo WHERE email=?", [entry_emil.get()])
            item = cur.fetchone()
            print(item)
            if item != None:
                    messagebox.showerror('Error','Record already exist')
                    window.destroy()
                    import login
            else:
                cur.execute( "INSERT INTO userinfo VALUES(:fname,:lname,:email,:password,:c_password)",
                             {'fname': fname_ent.get(),
                              'lname': lname_ent.get(),
                              'email': entry_emil.get(),
                              'password': pwd_entr.get(),
                              'c_password': c_pwd.get(),

                              } )
            con.commit()
            con.close()
            messagebox.showinfo('Success','Records Added')
            window.destroy()
            import login
        except:
            messagebox.showerror('Error','Something went wrong')

    fname_ent.delete(0,END)
    lname_ent.delete(0,END)
    entry_emil.delete(0,END)
    pwd_entr.delete(0,END)
    c_pwd.delete(0,END)
    #chk_butt1.deletecommand(0,)
    #window.destroy()



f_name = Label(window,text='First Name:',font=('Times New Roman',20))
f_name.place(x=80,y=100)
fname_ent =Entry(window,font=('Times New Roman',20),relief=FLAT,highlightthickness=2,bd=2,bg='#9EDBCC',fg='#2B75F0')
fname_ent.place(x=250,y=100,width=300,height=35)

l_name = Label(window,text='Last Name:',font=('Times New Roman',20))
l_name.place(x=80,y=150)
lname_ent =Entry(window,font=('Times New Roman',20),relief=FLAT,highlightthickness=2,bd=2,bg='#9EDBCC',fg='#2B75F0')
lname_ent.place(x=250,y=150,width=300,height=35)

email = Label(window,text='Email:',font=('Times New Roman',20))
email.place(x=80,y=200)
entry_emil =Entry(window,font=('Times New Roman',20),relief=FLAT,highlightthickness=2,bd=2,bg='#9EDBCC',fg='#2B75F0')
entry_emil.place(x=250,y=200,width=300,height=35)

password = Label(window,text='Password:',font=('Times New Roman',20))
password.place(x=80,y=250)
pwd_entr =Entry(window,font=('Times New Roman',20),show='*',relief=FLAT,highlightthickness=2,bd=2,bg='#9EDBCC',fg='#2B75F0')
pwd_entr.place(x=250,y=250,width=300,height=35)

chk1_var = IntVar()
def chk1_pwd():
    if chk1_var.get()==1:
        pwd_entr.config(show='')
    else:
        pwd_entr.config(show='*')
c_password = Label(window,text='Confirm password:',font=('Times New Roman',20))
c_password.place(x=80,y=300)
c_pwd =Entry(window,font=('Times New Roman',20),show='*',relief=FLAT,highlightthickness=2,bd=2,bg='#9EDBCC',fg='#2B75F0')
c_pwd.place(x=250,y=300,width=300,height=35)

# password matching
#=======================
password_rule =Text(window,fg='red',font=('Angsana New',13),bg='white')
password_rule.place(x=20,y=400,height=40)
password_rule.insert(INSERT,' Password should be : * One lowercase character \t* One special character\t* One uppercase character \n * 8 characters minimum \t * One number')
'''
lbl_date =Label(window,text='Registration Date:',font=('Times New Roman',20))
lbl_date.place(x=80,y=350,)
cal = DateEntry(window,selectmode='day')
cal.place(x=250,y=350,height=35)
#regi_date =
'''

def iExit():
    iExit = messagebox.askyesno('info','Do you want to exit')  # (‘validate Entry Widget’,Confirm if you want to exit’)
    if iExit > 0:
        window.destroy()
        return

chk_butt1 = Checkbutton(text='',onvalue=1,offvalue=0,command=chk1_pwd,variable=chk1_var)
chk_butt1.place(x=550,y=250)

sub_button = Button(window,text='Save',fg='blue',command=save)
sub_button.place(x=300,y=350, width=100,height=35)

exit_btn = Button(text='Exit',command=iExit,fg='blue')
exit_btn.place(x= 400,y=350, width=100,height=35)

window.mainloop()