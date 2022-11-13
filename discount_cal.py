import sqlite3
from tkinter import *
from tkinter import messagebox
import datetime as dt
from tkinter import ttk

root = Tk()

root.geometry('1000x800+200+100')
root.title('Daily Sales Accounting')

frame3 = Frame(root,relief=FLAT,bg='#47BABA',bd=4)
frame3.place(relx=0.5,rely=0.03,anchor='center')

<<<<<<< Updated upstream
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
=======
head_lbl = Label(frame3,text='Company Discount Sales Calculations',font=('Microsoft Himalaya',24,'bold','italic'),fg='#D0B2D9')
head_lbl.pack()# pack(side=TOP,fill=X)

def check():
    if employe_id_entry.get()=='' or  orginal_sale_entr.get() == '' or item_entry.get()=='':
        messagebox.showerror( 'Error', 'Required field is empty' )
    else:
        #curr.execute('SHOW DATABASES')
        #print(curr)

        WideDisAmt = float(ActualPrice.get())*0.1
        v1=round(WideDisAmt,2)
        WidDiscPrice.set(str(v1))
###Over$2000 Discount amount
        if float(ActualPrice.get())> 2000:
            over2000DiscountAmt = float(ActualPrice.get())*0.1
            v2=round(over2000DiscountAmt,2)
            Overdiscount.set(str(v2))
        else:
            over2000DiscountAmt = 0
            Overdiscount.set( str( over2000DiscountAmt ) )
>>>>>>> Stashed changes

### Total Discount Amount
        TotalDiscount = WideDisAmt + over2000DiscountAmt
        v3 =round(TotalDiscount,2)
        totalDisAmt.set(str(v3))
### Discounted Sale Price
<<<<<<< Updated upstream
        discountSalePrice = float(OrgPrice.get())-TotalDiscount
        v4 = round(discountSalePrice,2)
        DiscPrice.set(str(v4))
=======
        discountSalePrice = float(ActualPrice.get())-TotalDiscount
        v4 = round(discountSalePrice,2)
        DiscountPrice.set(str(v4))

>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
                    'prod_id': prod_code_entry.get(),
=======
                    'prod_id': item_entry.get(),
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
            prod_code_entry.delete( 0, END )
=======
            item_entry.delete( 0, END )
>>>>>>> Stashed changes
            wideDisc_Entry.delete( 0, END )
            Over200_Entry.delete( 0, END )
            TotalDis_Entry.delete( 0, END )
            DiscountPrice_Entry.delete( 0, END )
            messagebox.showinfo( '', 'All record are added successfully' )

<<<<<<< Updated upstream
def search():
    conn = sqlite3.connect( 'abcompany.db' )
    curr = conn.cursor()
    curr.execute("SELECT * FROM salesinfo WHERE emp_id =? ",[search_entry.get()])
    records=curr.fetchmany()
    print(records)
=======
def Search():
    conn = sqlite3.connect( 'abcompany.db' )
    curr = conn.cursor()
    curr.execute("SELECT * FROM salesinfo WHERE emp_id like ? ",[search_entry.get()])
    records=curr.fetchall()
    if len(records)!=0:
       detail_table.delete(*detail_table.get_children()) #get_children():Returns the list of children belonging to item
    for record in records:
        detail_table.insert('',5,values=record) #Creates a new item and returns the item identifier of the newly created item.
        conn.commit()
    conn.close()

>>>>>>> Stashed changes

def idelete():
        pass
def iupdate():
    pass

def logout():
    logout = messagebox.askyesno('info','Do you want to exit')  # (‘validate Entry Widget’,Confirm if you want to exit’)
    if logout > 0:
        root.destroy()
        return

def refresh():
    EmployeeID.set('')
    ItemCode.set('')
    ActualPrice.set('')
    WidDiscPrice.set('')
    Overdiscount.set('')
    totalDisAmt.set('')
    totalDisAmt.set('')
    DiscountPrice.set('')
    SearchRecord.set('')

EmployeeID=StringVar()
ItemCode=StringVar()
ActualPrice = StringVar()
WidDiscPrice = StringVar()
Overdiscount = StringVar()
totalDisAmt= StringVar()
DiscountPrice = StringVar()
SearchRecord = StringVar()

date = dt.datetime.now()
date_lbl = Label(root, text=f"{date:%A %B %d, %Y}", font=('Calibri',12))
date_lbl.place(relx=0.5,rely=0.08,anchor='center')

<<<<<<< Updated upstream
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
=======
#====================================Frame============
frame1 = Frame(root,relief=GROOVE,bg='#47BABA',bd=3)
frame1.place(x=650,y=100,width=320,height=350)
frame2 = Frame(root,relief=GROOVE,bg='#DEABCE',bd=3)
frame2.place(x=20,y=100,width=630,height=350)

employe_id =Label(frame1, text='Employe ID',bg='#47BABA',font=('Cambria',18))
employe_id.place(x=10,y=50)
employe_id_entry = Entry(frame1,textvariable=EmployeeID, bd=3,font=('Cambria',18))
employe_id_entry.place(x=150,y=50,width=150,height=30)

item_lbl =Label(frame1,text='Item Code',bg='#47BABA',font=('Cambria',18))
item_lbl.place(x=10,y=100)
item_entry = Entry(frame1,textvariable=ItemCode ,bd=3,fg='blue',font=('Cambria',18))
item_entry.place(x=150,y=100,width=150,height=30)

orginal_sale_lbl =Label(frame1,text='Actual price',bg='#47BABA',font=('Cambria',18))
orginal_sale_lbl.place(x=10,y=150)
orginal_sale_entr = Entry(frame1,textvariable=ActualPrice,bd=3,fg='blue',font=('Cambria',18))
orginal_sale_entr.place(x=150,y=150,width=150,height=30)

wide_discount = Label(frame2,text='Wide Discount Amount',font=('Calibri',18),bg='#DEABCE')
wide_discount.place(x=50,y=50)
wideDisc_Entry =Entry(frame2,textvariable=WidDiscPrice,font=('Times New Roman',18))
wideDisc_Entry.place(x=350,y=50, width=250,height=30)

Ovr2000_discount = Label(frame2,text='Over$2000 Discount Amount',font=('Calibri',18),bg='#DEABCE')
Ovr2000_discount.place(x=50,y=100)
Over200_Entry =Entry(frame2,textvariable=Overdiscount,font=('Times New Roman',18))
Over200_Entry.place(x=350,y=100, width=250,height=30)

Total_discount = Label(frame2,text='Total Discount Amount',font=('Calibri',18),bg='#DEABCE')
Total_discount.place(x=50,y=150)
TotalDis_Entry =Entry(frame2,textvariable=totalDisAmt,font=('Times New Roman',18))
TotalDis_Entry.place(x=350,y=150, width=250,height=30)

DisSale_Price = Label(frame2,text='Discounted Sale Price',font=('Calibri',18),bg='#DEABCE')
DisSale_Price.place(x=50,y=200)
DiscountPrice_Entry =Entry(frame2,textvariable=DiscountPrice,font=('Times New Roman',18))
DiscountPrice_Entry.place(x=350,y=200, width=250,height=30)

Refresh_btn =Button(frame1,text='Refresh',font=('Cambria',18),command=refresh,relief=FLAT,bd=0)
Refresh_btn.place(x=30,y=250,width=80,height=30)
OrgSal_btn =Button(frame1,text='Check',font=('Cambria',18),command=check,relief=FLAT,bd=0)
OrgSal_btn.place(x=200,y=250,width=80,height=30)
Logout_btn =Button(frame1,text='Logout',font=('Cambria',18),command=logout,relief=FLAT,bd=0)
Logout_btn.place(x=30,y=300,width=250,height=25)

search_btn =Button(frame1,text='Search',command=Search,font=('Cambria',18),fg='blue',relief=FLAT,bd=0)
search_btn.place(x=200,y=200,width=80,height=30)
search_entry =Entry(frame1,bd=3,textvariable=SearchRecord, fg='blue',font=('Cambria',18))
search_entry.place(x=20,y=200,width=150,height=30)

submit_btn =Button(frame2,text='Submit',font=('Cambria',18),command=submit,relief=FLAT,bd=0)
submit_btn.place(x=500,y=250,width=80,height=30)
delete_btn =Button(frame2,text='Update',font=('Cambria',18),command=iupdate,relief=FLAT,bd=0)
delete_btn.place(x=400,y=250,width=80,height=30)
delete_btn =Button(frame2,text='Delete',font=('Cambria',18),command=idelete,relief=FLAT,bd=0)
delete_btn.place(x=300,y=250,width=80,height=30)


#==================Table Fram===========
frame3 = Frame(root,relief=GROOVE,bg='#DEDED5',bd=3)
frame3.place(x=20,y=450,width=950,height=300)
#==============Treeview======================
#A Treeview widget allows you to display data in both tabular and hierarchical structures.
# To create a Treeview widget, you use the ttk.Treeview class:
scroll_x =Scrollbar(frame3,orient=HORIZONTAL)
scroll_y =Scrollbar(frame3,orient=VERTICAL)

detail_table = ttk.Treeview(frame3,columns=('prod_id','emp_id','orgi_price','wide_disc','over2000_amt','total_amt','disc_price'),show='headings', xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=detail_table.xview)
scroll_y.config(command=detail_table.yview)
detail_table.heading('prod_id',text='Item Code')
detail_table.heading('emp_id',text='Emp Code')
detail_table.heading('orgi_price',text='Actual Price')
detail_table.heading('wide_disc',text='Wide Discount')
detail_table.heading('over2000_amt',text='Special Disc')
detail_table.heading('total_amt',text='Total Amnt')
detail_table.heading('disc_price',text='Discoont Amnt')
detail_table.column('prod_id',width=100)
detail_table.column('emp_id',width=100)
detail_table.column('orgi_price',width=100)
detail_table.column('wide_disc',width=100)
detail_table.column('over2000_amt',width=100)
detail_table.column('total_amt',width=100)
detail_table.column('disc_price',width=100)
detail_table.pack(fill=BOTH,expand=TRUE)
>>>>>>> Stashed changes



root.mainloop()
