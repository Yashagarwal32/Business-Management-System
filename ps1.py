from tkinter import *
import sqlite3
import tkinter.messagebox

conn=sqlite3.connect('databse1.db')
c=conn.cursor()










class Application:
    def __init__(self,master):
        self.master=master


        #Frames=============================
        
        self.mainframe=Frame(self.master,width=1540,height=1000,bg="red")
        self.mainframe.place(x=0,y=0)
        
        self.upperframe=Frame(self.mainframe,width=1540,height=50,bg="#FF6347")
        self.upperframe.place(x=0,y=0)
        
        self.secondframe=Frame(self.mainframe,width=1540,height=150,bg="#FF7F50")
        self.secondframe.place(x=0,y=52)
        
        self.left=Frame(self.mainframe,width=400,height=1000,bg='#FF6347')
        self.left.place(x=0,y=200)

        self.middle=Frame(self.mainframe,width=400,height=1000,bg='#FF6347')
        self.middle.place(x=401,y=200)
        
        self.right=Frame(self.mainframe,width=800,height=1000,bg='#FF6347')
        self.right.place(x=802,y=200)

        self.heading=Label(self.upperframe,text="Hare Krishna Super Mall",font=('arial 30 bold'),fg='black',bg='#FF6347')
        self.heading.place(x=500,y=0)


        #secondframe======================================
        
        self.headingtoday=Label(self.secondframe,text="Today's Overview",font=('arial 15 bold'),fg='black',bg='#FF7F50')
        self.headingtoday.place(x=10,y=5)
        #sale
        self.todaysalelabel=Frame(self.secondframe,width=140,height=25,bg='#00BFFF')
        self.todaysalelabel.place(x=10,y=40)
        
        self.todaysaleentry=Frame(self.secondframe,width=140,height=60,bg='#FC165B')
        self.todaysaleentry.place(x=10,y=66)
        
        self.todaysalehead1=Label(self.todaysalelabel,text="Sales",font=('arial 10 bold'),fg='black',bg='#00BFFF')
        self.todaysalehead1.place(x=50,y=0)
        self.todaysalehead2=Label(self.todaysaleentry,text="₹100000",font=('arial 20 bold'),fg='black',bg='#FC165B')
        self.todaysalehead2.place(x=10,y=10)

        #profit
        self.todayprofitlabel=Frame(self.secondframe,width=140,height=25,bg='#00BFFF')
        self.todayprofitlabel.place(x=180,y=40)
        
        self.todayprofitentry=Frame(self.secondframe,width=140,height=60,bg='#FC165B')
        self.todayprofitentry.place(x=180,y=66)
        
        self.todayprofithead1=Label(self.todayprofitlabel,text="Profit",font=('arial 10 bold'),fg='black',bg='#00BFFF')
        self.todayprofithead1.place(x=50,y=0)
        self.todayprofithead2=Label(self.todayprofitentry,text="₹10000",font=('arial 20 bold'),fg='black',bg='#FC165B')
        self.todayprofithead2.place(x=10,y=10)

        #credit
        self.todaycreditlabel=Frame(self.secondframe,width=140,height=25,bg='#00BFFF')
        self.todaycreditlabel.place(x=350,y=40)
        
        self.todaycreditentry=Frame(self.secondframe,width=140,height=60,bg='#FC165B')
        self.todaycreditentry.place(x=350,y=66)
        
        self.todaycredithead1=Label(self.todaycreditlabel,text="credit",font=('arial 10 bold'),fg='black',bg='#00BFFF')
        self.todaycredithead1.place(x=50,y=0)
        self.todaycredithead2=Label(self.todaycreditentry,text="₹3500",font=('arial 20 bold'),fg='black',bg='#FC165B')
        self.todaycredithead2.place(x=10,y=10)

        #oldcredit

        self.todayoclabel=Frame(self.secondframe,width=140,height=25,bg='#00BFFF')
        self.todayoclabel.place(x=520,y=40)
        
        self.todayocentry=Frame(self.secondframe,width=140,height=60,bg='#FC165B')
        self.todayocentry.place(x=520,y=66)
        
        self.todayochead1=Label(self.todayoclabel,text="Old credit deposit",font=('arial 10 bold'),fg='black',bg='#00BFFF')
        self.todayochead1.place(x=10,y=0)
        self.todayochead2=Label(self.todayocentry,text="₹10000",font=('arial 20 bold'),fg='black',bg='#FC165B')
        self.todayochead2.place(x=10,y=10)

        #totalcash
        self.todaytclabel=Frame(self.secondframe,width=140,height=25,bg='#00BFFF')
        self.todaytclabel.place(x=690,y=40)
        
        self.todaytcentry=Frame(self.secondframe,width=140,height=60,bg='#FC165B')
        self.todaytcentry.place(x=690,y=66)
        
        self.todaytchead1=Label(self.todaytclabel,text="Cash Payment",font=('arial 10 bold'),fg='black',bg='#00BFFF')
        self.todaytchead1.place(x=24,y=0)
        self.todaytchead2=Label(self.todaytcentry,text="₹75000",font=('arial 20 bold'),fg='black',bg='#FC165B')
        self.todaytchead2.place(x=10,y=10)

        #totalonline
        self.todaytolabel=Frame(self.secondframe,width=140,height=25,bg='#00BFFF')
        self.todaytolabel.place(x=860,y=40)
        
        self.todaytoentry=Frame(self.secondframe,width=140,height=60,bg='#FC165B')
        self.todaytoentry.place(x=860,y=66)
        
        self.todaytohead1=Label(self.todaytolabel,text="Online Payment",font=('arial 10 bold'),fg='black',bg='#00BFFF')
        self.todaytohead1.place(x=24,y=0)
        self.todaytohead2=Label(self.todaytoentry,text="₹25000",font=('arial 20 bold'),fg='black',bg='#FC165B')
        self.todaytohead2.place(x=10,y=10)

        #paytosupplier
        self.todayptslabel=Frame(self.secondframe,width=140,height=25,bg='#00BFFF')
        self.todayptslabel.place(x=1030,y=40)
        
        self.todayptsentry=Frame(self.secondframe,width=140,height=60,bg='#FC165B')
        self.todayptsentry.place(x=1030,y=66)
        
        self.todayptshead1=Label(self.todayptslabel,text="Stocks Added",font=('arial 10 bold'),fg='black',bg='#00BFFF')
        self.todayptshead1.place(x=25,y=0)
        self.todayptshead2=Label(self.todayptsentry,text="₹26000",font=('arial 20 bold'),fg='black',bg='#FC165B')
        self.todayptshead2.place(x=10,y=10)

        #defective items
        self.todaydilabel=Frame(self.secondframe,width=140,height=25,bg='#00BFFF')
        self.todaydilabel.place(x=1200,y=40)
        
        self.todaydientry=Frame(self.secondframe,width=140,height=60,bg='#FC165B')
        self.todaydientry.place(x=1200,y=66)
        
        self.todaydihead1=Label(self.todaydilabel,text="Loss",font=('arial 10 bold'),fg='black',bg='#00BFFF')
        self.todaydihead1.place(x=50,y=0)
        self.todaydihead2=Label(self.todaydientry,text="₹500",font=('arial 20 bold'),fg='black',bg='#FC165B')
        self.todaydihead2.place(x=10,y=10)


        #left frame=======================================
        
        self.leftlabel=Frame(self.left,width=400,height=35,bg='#FF4500')
        self.leftlabel.place(x=0,y=0)
        
        self.leftheading=Label(self.left,text="To do List",font=('arial 18 bold'),fg='black',bg='#FF4500')
        self.leftheading.place(x=140,y=0)

        #middle frame===================================
        
        self.middlelabel=Frame(self.middle,width=400,height=35,bg='#FF4500')
        self.middlelabel.place(x=0,y=0)
        
        self.middleheading=Label(self.middle,text="Products Expire Soon ",font=('arial 18 bold'),fg='black',bg='#FF4500')
        self.middleheading.place(x=70,y=0)

        #right frame====================================

        self.rightlabel=Frame(self.right,width=800,height=35,bg='#FF4500')
        self.rightlabel.place(x=0,y=0)
        
        self.rightheading=Label(self.right,text="Manage your Business",font=('arial 18 bold'),fg='black',bg='#FF4500')
        self.rightheading.place(x=200,y=0)

        self.empbutton=Button(self.right,text="Employee 👨🏻‍💼",width=16,height=4,bg='#F90B3E',font=('arial 17 bold'),command=self.add_appointment)
        self.empbutton.place(x=90,y=50)
        
        self.stocksbutton=Button(self.right,text="Stocks 🍫🍭",width=16,height=4,bg='#DC143C',font=('arial 17 bold'),command=self.add_appointment)
        self.stocksbutton.place(x=430,y=50)

        self.supbutton=Button(self.right,text="Supplier 🚚",width=16,height=4,bg='#FF4500',font=('arial 17 bold'),command=self.add_appointment)
        self.supbutton.place(x=90,y=200)
        
        self.expnbutton=Button(self.right,text="Expenditure 💸💸",width=16,height=4,bg='#FF0000',font=('arial 17 bold'),command=self.add_appointment)
        self.expnbutton.place(x=430,y=200)
        
        self.oldbillbutton=Button(self.right,text="Old Bills 🗒",width=16,height=4,bg='#F08080',font=('arial 17 bold'),command=self.add_appointment)
        self.oldbillbutton.place(x=430,y=350)
        
        self.credbutton=Button(self.right,text="Credit 💳",width=16,height=4,bg='#32CD32',font=('arial 17 bold'),command=self.add_appointment)
        self.credbutton.place(x=90,y=350)
        
        self.earnbutton=Button(self.right,text="Earning 💵💰",width=16,height=4,bg='#0DC264',font=('arial 17 bold'),command=self.add_appointment)
        self.earnbutton.place(x=90,y=500)

        self.chebutton=Button(self.right,text="Checkout 📝",width=16,height=4,bg='#20B2AA',font=('arial 17 bold'),command=self.add_appointment)
        self.chebutton.place(x=430,y=500)
        
        

        
        

        
        
        


        
        

        

        

        
        

        

        
        

        
        
        

        

        


        
        #Entries=======================
        '''
        self.name_ent=Entry(self.left,width=30)
        self.name_ent.place(x=250,y=100)

        
       #buttton===================

        self.submit=Button(self.left,text="Add Appointment",width=20,height=2,bg='#FF6347',command=self.add_appointment)
        self.submit.place(x=250,y=300)
        '''
        


        #Fuction to call=======================
    def add_appointment(self):
        self.val1=self.name_ent.get()
        self.val2=self.age_ent.get()
        self.val3=self.gender_ent.get()
        self.val4=self.location_ent.get()
        self.val5=self.time_ent.get()


  #=========testing===============
        if self.val1=="" or self.val2=="" or self.val3=="" or self.val4=="" or self.val5=="":
            tkinter.messagebox.showinfo("warning","Please fill up all boxes")
        else:
            sql="INSERT INTO 'appointments' (name,age,gender,location,scheduled_time) VALUES(?,?,?,?,?)"
            c.execute(sql, (self.val1,self.val2,self.val3,self.val4,self.val5))
            conn.commit()
            print("success")







root=Tk()
b=Application(root)


root.geometry("1200x720")
root.attributes("-fullscreen",True)

root.resizable(False,False)

root.mainloop()
