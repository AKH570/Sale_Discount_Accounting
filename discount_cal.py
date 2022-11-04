import sqlite3
from tkinter import *
from tkinter import messagebox
import datetime as dt

root = Tk()
root.geometry('800x600+200+100')
root.title('Daily Sales Accounting')

head_lbl = Label(root,text='Company Discount Sales Calculations',font=('Microsoft Himalaya',24,'bold','italic'),fg='#FF00BF')
head_lbl.place(relx=0.5,rely=0.03,anchor='center')
'''
try:
    conn= sqlite3.connect('abcompany.db')
    curr = conn.cursor()
    curr.execute(""" CREATE TABLE IF NOT EXISTS salesinfo(
                prod_id TEXT PRIMARY KEY,
                emp_id TEXT NOT NULL,
                orgi_price TEXT NOT NULL,
                wide_disc TEXT,
                over2000_amt TEXT NOT NULL,
                total_amt TEXT NOT NULL,
                disc_price TEXT NOT NULL
                )""")
    conn.commit()
except Exception as e:
    print(e)
'''
def check():
    if employe_id_entry.get()=='' or  orginal_sale_entr.get() == '' or prod_code_entry.get()=='':
        messagebox.showerror( 'Error', 'Required field is empty' )
    else:
        #curr.execute('SHOW DATABASES')
        #print(curr)

        WideDisAmt = float(OrgPrice.get())*0.1
        v1=round(WideDisAmt,2)
        WidDisc.set(str(v1))
###Over$2000 Discount amount
        if float(OrgPrice.get())> 2000:
            over2000DiscountAmt = float(OrgPrice.get())*0.1
            v2=round(over2000DiscountAmt,2)
            Ovr2000.set(str(v2))
        else:
            over2000DiscountAmt = 0
            Ovr2000.set( str( over2000DiscountAmt ) )

### Total Discount Amount
        TotalDiscount = WideDisAmt + over2000DiscountAmt
        v3 =round(TotalDiscount,2)
        totalDisAmt.set(str(v3))
### Discounted Sale Price
        discountSalePrice = float(OrgPrice.get())-TotalDiscount
        v4 = round(discountSalePrice,2)
        DiscPrice.set(str(v4))

def submit():
            conn = sqlite3.connect( 'abcompany.db' )
            curr = conn.cursor()
            curr.execute( """ CREATE TABLE IF NOT EXISTS salesinfo(
                            prod_id TEXT PRIMARY KEY,
                            emp_id TEXT NOT NULL,
                            orgi_price TEXT NOT NULL,
                            wide_disc TEXT,
                            over2000_amt TEXT NOT NULL,
                            total_amt TEXT NOT NULL,
                            disc_price TEXT NOT NULL
                            )""" )
            curr.execute("INSERT INTO salesinfo VALUES (:prod_id,:emp_id,:orgi_price,:wide_disc,:over2000_amt,:total_amt,:disc_price)",
                {
                    'prod_id': prod_code_entry.get(),
                    'emp_id': employe_id_entry.get(),
                    'orgi_price': orginal_sale_entr.get(),
                    'wide_disc': wideDisc_Entry.get(),
                    'over2000_amt': Over200_Entry.get(),
                    'total_amt': TotalDis_Entry.get(),
                    'disc_price': DiscountPrice_Entry.get()
                } )
            conn.commit()
            conn.close()

            employe_id_entry.delete( 0, END )
            orginal_sale_entr.delete( 0, END )
            prod_code_entry.delete( 0, END )
            wideDisc_Entry.delete( 0, END )
            Over200_Entry.delete( 0, END )
            TotalDis_Entry.delete( 0, END )
            DiscountPrice_Entry.delete( 0, END )
            messagebox.showinfo( '', 'All record are added successfully' )

def search():
    conn = sqlite3.connect( 'abcompany.db' )
    curr = conn.cursor()
    curr.execute("SELECT * FROM salesinfo WHERE emp_id =? ",[search_entry.get()])
    records=curr.fetchmany()
    print(records)

def idelete():
        pass

def logout():
    logout = messagebox.askyesno('info','Do you want to exit')  # (‘validate Entry Widget’,Confirm if you want to exit’)
    if logout > 0:
        root.destroy()
        return
def refresh():
    OrgPrice.set('')
    WidDisc.set('')
    Ovr2000.set('')
    totalDisAmt.set('')
    DiscPrice.set('')

OrgPrice = StringVar()
WidDisc = StringVar()
Ovr2000 = StringVar()
totalDisAmt= StringVar()
DiscPrice = StringVar()

date = dt.datetime.now()
date_lbl = Label(root, text=f"{date:%A %B %d, %Y}", font=('Calibri',12))
date_lbl.place(relx=0.5,rely=0.08,anchor='center')

employe_id =Label(root,text='Emp ID :', font=('Cambria',16,'bold'),fg='black')
employe_id.place(x=100,y=150)
employe_id_entry = Entry(root,bg='light grey',bd=3,fg='blue',font=('Cambria',16))
employe_id_entry.place(x=200,y=150,width=150,height=30)

prod_lbl =Label(root,text='Product code', font=('Cambria',16,'bold'),fg='black')
prod_lbl.place(x=400,y=200)
prod_code_entry = Entry(root,bg='light grey',bd=3,fg='blue',font=('Cambria',16))
prod_code_entry.place(x=550,y=200,width=100,height=30)

search_btn =Button(root,text='Search', font=('Cambria',16),fg='black',bd=3,command=search)
search_btn.place(x=500,y=150,width=100,height=30)
search_entry =Entry(root,bg='light grey',bd=3,fg='blue',font=('Cambria',16))
search_entry.place(x=400,y=150,width=100,height=30)

orginal_sale_lbl =Label(root,text='Original Sale Price $:', font=('Cambria',16,'bold'),fg='black')
orginal_sale_lbl.place(x=50,y=200)
orginal_sale_entr = Entry(root,bg='light grey',bd=3,fg='blue',font=('Cambria',16),textvariable=OrgPrice)
orginal_sale_entr.place(x=220,y=200,width=150,height=30)

Refresh_btn =Button(root,text='Refresh',font=('Cambria',18),fg='blue',command=refresh)
Refresh_btn.place(x=320,y=250,width=80,height=35)
OrgSal_btn =Button(root,text='Check',font=('Cambria',18),fg='blue',command=check)
OrgSal_btn.place(x=410,y=250,width=80,height=35)
delete_btn =Button(root,text='Delete',font=('Cambria',18),fg='blue',command=idelete)
delete_btn.place(x=500,y=250,width=80,height=35)


wide_discount = Label(root,text='Company Wide Discount Amount $:',font=('Calibri',18))
wide_discount.place(x=70,y=310)
wideDisc_Entry =Entry(root,textvariable=WidDisc,font=('Cambria',20))
wideDisc_Entry.place(x=370,y=310, width=250,height=30)

Ovr2000_discount = Label(root,text='Over$2000 Discount Amount $:',font=('Calibri',18))
Ovr2000_discount.place(x=100,y=350)
Over200_Entry =Entry(root,textvariable=Ovr2000,font=('Cambria',20))
Over200_Entry.place(x=370,y=350, width=250,height=30)

Total_discount = Label(root,text='Total Discount Amount $:',font=('Calibri',18))
Total_discount.place(x=150,y=390)
TotalDis_Entry =Entry(root,textvariable=totalDisAmt,font=('Cambria',20))
TotalDis_Entry.place(x=370,y=390, width=250,height=30)

DisSale_Price = Label(root,text='Discounted Sale Price $:',font=('Calibri',18))
DisSale_Price.place(x=160,y=430)
DiscountPrice_Entry =Entry(root,textvariable=DiscPrice,font=('Cambria',20))
DiscountPrice_Entry.place(x=370,y=430, width=250,height=30)

submit_btn =Button(root,text='Submit',font=('Cambria',18),fg='blue',command=submit)
submit_btn.place(x=400,y=500,width=80,height=35)
Logout_btn =Button(root,text='Logout',font=('Cambria',18),fg='blue',command=logout)
Logout_btn.place(x=500,y=500,width=80,height=35)



root.mainloop()
