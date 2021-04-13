import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database import *
import smtplib
from tkcalendar import DateEntry

e1=""
e2=""
e3=""
e4=""
e5=""
d1=""
d2=""
email=""
email_date=""
da=""
fr=""
end=""


def msg():
    tkinter.messagebox.showinfo(title="Loggedin", message="Successful")
def error():
    tkinter.messagebox.showerror(title=" ", message="Invalid")
def msg1():
    tkinter.messagebox.showinfo(title="Registered", message="Successfully registered")


class dateissue:
    def __init__(self,da):
        self.da=da

    def mail_ver(self):
            tkinter.messagebox.showinfo(title="Booked Succesfully", message="Successful")
            self.em_da = self.da.get_date()
            global email, win4, email_date, user
            win4.destroy()
            sender = 'supremecabs001@gmail.com'
            receivers = user
            mail_dri = mycol1.find({}, {"_id": 0, "driver_name": 1})
            mail_num = mycol1.find({}, {"_id": 0, "taxi_number": 1})
            message = """From: Supreme Cabs
To: %s
Subject: Book Alert

Your Ride Booked Succesfully\nDriver : %s\nTaxi Number : %s\nDate : %s
"""%(receivers,mail_dri[0]["driver_name"], mail_num[0]["taxi_number"], self.em_da)

            try:
                smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
                smtpObj.starttls()
                smtpObj.login("supremecabs001@gmail.com", "mongodbtaxibookingsystem")
                smtpObj.sendmail(sender, receivers, message)
                print("Successfully sent email")
                smtpObj.quit()
            except smtplib.SMTPException:
                print("Error: unable to send email")


def conf():
    global win3, d1, d2, user, win4, da, email_date,fr,end
    win3.destroy()
    win4 = Tk()
    win4.title("Confirm Ride")
    win4.geometry("700x330")
    win4.config(bg="#0e0b0b")
    win4.iconbitmap(f'taxi_5pB_icon.ico')
    win4.resizable(False,False)
    tkinter.Label(win4, text="From", font=('arial', 19), bg="#0e0b0b",fg="#ff00ff").place(relx=0.2567,rely=0.2)
    tkinter.Label(win4, text="To", font=('arial', 19), bg="#0e0b0b",fg="#ff00ff").place(relx=0.2567,rely=0.4)
    tkinter.Label(win4, text="Enter the Date", font=('arial', 19), bg="#0e0b0b", fg="#ff00ff").place(relx=0.2567, rely=0.6)
    tkinter.Label(win4, text=fr, font=('times new roman', 19),bg="#0e0b0b",fg="#ebffe6").place(relx=0.4567,rely=0.2)
    tkinter.Label(win4, text=end, font=('times new roman', 19),bg="#0e0b0b",fg="#ebffe6").place(relx=0.4567,rely=0.4)
    da = DateEntry(win4,bg="dark blue",fg="white")
    da.place(relx=0.5567,rely=0.6)
    tkinter.Button(win4, text="Confirm",command=dateissue(da).mail_ver, font=('arial', 14),bd=0,).place(relx=0.3987,rely=0.8)





def check():
    global win2,c,win3,d1,d2,user,fr,end
    fr = d1.get()
    end = d2.get()
    mycol2.insert_one({"email":user,"start_loc":fr,"end_loc":end})
    com = c.get()
    win2.destroy()
    win3 = Tk()
    win3.title("Booking details")
    win3.geometry("700x600")
    win3.config(bg="#339933")
    win3.iconbitmap(f'taxi_5pB_icon.ico')
    win3.resizable(False, False)
    res1 = mycol1.find({}, {"_id": 0, "driver_name": 1})
    res2 = mycol1.find({}, {"_id": 0, "rating": 1})
    res3 = mycol1.find({}, {"_id": 0, "taxi_number": 1})
    if com =="Prime(7)":
        tkinter.Label(win3,text="DriverName",font=('arial',19),bg="#339933",fg="#ffff80").place(relx=0.2,rely=0.3)
        tkinter.Label(win3,text="Rating",font=('arial',19),bg="#339933",fg="#ffff80").place(relx=0.2,rely=0.4)
        tkinter.Label(win3,text="TaxiNumber",font=('arial',19),bg="#339933",fg="#ffff80").place(relx=0.2,rely=0.5)
        tkinter.Label(win3,text="Type of the car",font=('arial',19),bg="#339933",fg="#ffff80").place(relx=0.2,rely=0.6)
        tkinter.Label(win3,text=res1[0]["driver_name"],font=('arial',19),bg="#339933",fg="#333300").place(relx=0.5,rely=0.3)
        tkinter.Label(win3,text=res2[0]["rating"],font=('arial',19),bg="#339933",fg="#333300").place(relx=0.5,rely=0.4)
        tkinter.Label(win3, text=res3[0]["taxi_number"],font=('arial',19),bg="#339933",fg="#333300").place(relx=0.5,rely=0.5)
        tkinter.Label(win3, text=com,font=('arial',19),bg="#339933",fg="#333300").place(relx=0.5,rely=0.6)
    else:
        ty = "Mini(3)"
        tkinter.Label(win3, text="DriverName", font=('arial',19),bg="#339933",fg="#ffff80").place(relx=0.2,rely=0.3)
        tkinter.Label(win3, text="Rating", font=('arial',19),bg="#339933",fg="#ffff80").place(relx=0.2,rely=0.4)
        tkinter.Label(win3, text="TaxiNumber", font=('arial',19),bg="#339933",fg="#ffff80").place(relx=0.2,rely=0.5)
        tkinter.Label(win3, text="Type of the car", font=('arial',19),bg="#339933",fg="#ffff80").place(relx=0.2,rely=0.6)
        tkinter.Label(win3, text=res1[0]["driver_name"],font=('arial',19),bg="#339933",fg="#333300").place(relx=0.5,rely=0.3)
        tkinter.Label(win3, text=res2[0]["rating"],font=('arial',19),bg="#339933",fg="#333300").place(relx=0.5,rely=0.4)
        tkinter.Label(win3, text=res3[0]["taxi_number"],font=('arial',19),bg="#339933",fg="#333300").place(relx=0.5,rely=0.5)
        tkinter.Label(win3, text=ty,font=('arial',19),bg="#339933",fg="#333300").place(relx=0.5,rely=0.6)

    tkinter.Button(win3,text="Book",font=('times new roman',20),bg="#339933",fg="#ffffff",bd=0,command=conf).place(relx=0.4,rely=0.7567)





def book():
    global win, c, win2, d1, d2
    win.destroy()
    win2 = Tk()
    win2.title("Book a ride")
    win2.config(bg="#595959")
    win2.geometry("700x430")
    win2.iconbitmap(f'taxi_5pB_icon.ico')
    win2.resizable(False, False)
    tkinter.Label(win2,text="Starting Loacation",font=('arial',18),bg="#595959",fg="#d2ff4d").place(relx=0.2567,rely=0.2)
    tkinter.Label(win2,text="Destination",font=('arial',18),bg="#595959",fg="#d2ff4d").place(relx=0.2567,rely=0.4)
    tkinter.Label(win2,text="Type of the car",font=('arial',18),bg="#595959",fg="#d2ff4d").place(relx=0.2567,rely=0.6)
    d1 = Entry(win2)
    d1.config(font=('arial',15),bg="#f2f2f2",fg="black")
    d1.place(relx=0.5567, rely=0.2)
    d2 = Entry(win2)
    d2.config(font=('arial', 15), bg="#f2f2f2", fg="black")
    d2.place(relx=0.5567, rely=0.4)
    cars =['Mini(3)', 'Prime(7)']
    c = ttk.Combobox(win2,values=cars)
    c.config(font=('arial',15))
    c.place(relx=0.5567, rely=0.6)
    tkinter.Button(win2,text="Check for availability",font=('times new roman', 15), bg="#595959", fg="black",bd=0,command=check).place(relx=0.3987,rely=0.8)




def reg2():
    global e1, e2, e3, e4, e5,email
    firstname = e1.get()
    lastname = e2.get()
    password = e3.get()
    email = e4.get()
    phno = e5.get()
    mycol.insert_one({"first_name":firstname,"last_name":lastname,"password":password,"email":email,"phonenumber":phno})
    global win1
    msg1()
    win1.destroy()


def reg():
    global win1,i
    win1=Tk()
    win1.config(bg="#00b3b3")
    win1.title("Registration Form")
    win1.geometry("700x600")
    win1.iconbitmap(f'taxi_5pB_icon.ico')
    win.resizable(False, False)
    tkinter.Label(win1,text="First Name",font=('arial', 16), bg='#00b3b3',fg='black').place(relx=0.2567,rely=0.2)
    tkinter.Label(win1,text="Last Name",font=('arial', 16), bg='#00b3b3',fg='black').place(relx=0.2567,rely=0.3)
    tkinter.Label(win1,text="Password",font=('arial',16),bg='#00b3b3',fg='black').place(relx=0.2567,rely=0.4)
    tkinter.Label(win1,text="E-mail",font=('arial',16),bg='#00b3b3',fg='black').place(relx=0.2567,rely=0.5)
    tkinter.Label(win1,text="PhoneNumber",font=('arial',16),bg='#00b3b3',fg='black').place(relx=0.2567,rely=0.6)
    global e1, e2, e3, e4, e5
    e1 = Entry(win1)
    e1.config(font=('times new roman',13),bg='#1affff',fg='black')
    e1.place(relx=0.4567,rely=0.2)
    e2 = Entry(win1)
    e2.config(font=('times new roman',13),bg='#1affff',fg='black')
    e2.place(relx=0.4567,rely=0.3)
    e3 = Entry(win1)
    e3.config(font=('times new roman',13),bg='#1affff',fg='black')
    e3.place(relx=0.4567,rely=0.4)
    e4 = Entry(win1)
    e4.config(font=('times new roman',13),bg='#1affff',fg='black')
    e4.place(relx=0.4567,rely=0.5)
    e5 = Entry(win1)
    e5.config(font=('times new roman',13),bg='#1affff',fg='black')
    e5.place(relx=0.4567,rely=0.6)
    tkinter.Button(win1, text="Register",font=('times new roman',17),bg='#00b3b3',fg='#4d4dff',bd=0,command=reg2).place(relx=0.3987, rely=0.7)








def log():
    global user
    user = a.get()
    passw = b.get()
    dic = {"email":user,"password":passw}
    res = mycol.find({"email":user},{"_id":0,"first_name":0,"last_name":0,"phonenumber":0})
    if res[0]["email"] == dic["email"] and res[0]["password"] == dic["password"]:
        book()
    else:
        error()



win = Tk()
win.title("Supreme Cabs")
win.config(bg='#ffcc00')
win.geometry("700x600")
win.resizable(False,False)
win.iconbitmap(f'taxi_5pB_icon.ico')
tkinter.Label(win, text="E-mail", font=('arial', 20), bg='#ffcc00',fg='black').place(relx=0.2, rely=0.4)
a = StringVar()
tkinter.Entry(win, text=a,font=('times new roman',18),bg='#4d1919',fg='white').place(relx=0.4, rely=0.4)
tkinter.Label(win, text="Password", font=('arial', 20), bg='#ffcc00',fg='black').place(relx=0.2, rely=0.5)
b = StringVar()
tkinter.Entry(win, text=b,font=('times new roman',18),bg='#4d1919',fg='white', show="*").place(relx=0.4, rely=0.5)
tkinter.Button(win, text="Login", font=('times new roman', 20), bg='#ffcc00', fg='red',bd=0,
               command=log).place(relx=0.4, rely=0.6567)
tkinter.Button(win, text="New user,Register Here", font=('times new roman', 20), bg='#ffcc00', fg='green',bd=0,
               command=reg).place(relx=0.2789, rely=0.7567)
win.mainloop()
