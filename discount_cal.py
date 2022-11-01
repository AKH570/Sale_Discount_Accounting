import sqlite3
from tkinter import *
from tkinter import messagebox
import datetime as dt

root = Tk()
root.geometry('800x600+200+100')
root.title('Daily Sales Accounting')

head_lbl = Label(root,text='Company Discount Sales Calculations',font=('Microsoft Himalaya',24,'bold','italic'),fg='#FF00BF')
head_lbl.place(relx=0.5,rely=0.03,anchor='center')



def myCalculation():
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
    if sales_manID_entry.get()=='' or  orginal_sale_entr.get() == '' :
        messagebox.showerror( 'Error', 'Invalid Data' )
    else:
        conn= sqlite3.connect('abcompany.db')
        curr = conn.cursor()
        curr.execute(""" CREATE TABLE IF NOT EXISTS salesinfo(
            empid TEXT NOT NULL,
            orgi_price TEXT NOT NULL,
            wide_disc TEXT NOT NULL,
            over2000_amt TEXT NOT NULL,
            total_amt TEXT NOT NULL 
            disc_price TEXT NOT NULL 
        )""")
        messagebox.showinfo('','Good job')
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

sales_manID =Label(root,text='Sales Man ID :', font=('Cambria',20,'bold'),fg='black')
sales_manID.place(x=150,y=150)
sales_manID_entry = Entry(root,bg='light grey',bd=3,fg='blue',font=('Cambria',20))
sales_manID_entry.place(x=300,y=150,width=150,height=40)

search_btn =Button(root,text='', font=('Cambria',20),fg='black',bd=3)
search_btn.place(x=580,y=150,width=50,height=35)
search_entry =Entry(root,bg='light grey',bd=3,fg='blue',font=('Cambria',20))
search_entry.place(x=480,y=150,width=100,height=35)

orginal_sale_lbl =Label(root,text='Original Sale Price $:', font=('Cambria',20,'bold'),fg='black')
orginal_sale_lbl.place(x=100,y=200)
orginal_sale_entr = Entry(root,bg='light grey',bd=3,fg='blue',font=('Cambria',20),textvariable=OrgPrice)
orginal_sale_entr.place(x=300,y=200,width=320,height=35)

Refresh_btn =Button(root,text='Refresh',font=('Cambria',18),fg='blue',command=refresh)
Refresh_btn.place(x=320,y=250,width=80,height=35)
OrgSal_btn =Button(root,text='Check',font=('Cambria',18),fg='blue',command=myCalculation)
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
