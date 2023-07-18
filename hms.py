from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


win = Tk()
win.state("zoomed")
win.config(bg="black")
win.title("Hospital Management System")

# Button function
# For saving prescreption data
def pd():
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror("Error","All Fields Are Required!")
    else:
        con = mysql.connector.connect(host="localhost",username="root",password="Vineet@8816",database="mydata")
        mycursor = con.cursor()
        mycursor.execute("insert into hospital1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            nameoftablets.get(),
            ref.get(),
            dose.get(),
            noOfTAblets.get(),
            issuedate.get(),
            expdate.get(),
            dailydose.get(),
            sideeffects.get(),
            nameofPatient.get(),
            dob.get(),
            patientAddress.get()
        ))
        con.commit()
        fetch_data()
        con.close()
        messagebox.showinfo("Successfull!","Record Has Been Inserted")

def fetch_data():
    con = mysql.connector.connect(host="localhost", username="root", password="Vineet@8816", database="mydata")
    mycursor = con.cursor()
    mycursor.execute("select * from hospital1")
    rows = mycursor.fetchall()
    if len(rows)!=0:
        table.delete(* table.get_children())
        for items in rows:
            table.insert("",END,values=items)
        con.commit()
    con.close()


def get_data(event=""):
    cursur_row = table.focus()
    data = table.item(cursur_row)
    row = data["values"]
    nameoftablets.set(row[0])
    ref.set(row[1])
    dose.set(row[2])
    noOfTAblets.set(row[3])
    issuedate.set(row[4])
    expdate.set(row[5])
    dailydose.set(row[6])
    sideeffects.set(row[7])
    nameofPatient.set(row[8])
    dob.set(row[9])
    patientAddress.set(row[10])


# prescreption button function
def pre():
    txt_frame.insert(END,"Name of Tablets:\t\t"+nameoftablets.get()+"\n")
    txt_frame.insert(END,"Reference No.:\t\t"+ref.get()+"\n")
    txt_frame.insert(END,"Dose:\t\t"+dose.get()+"\n")
    txt_frame.insert(END,"No. Of Tablets:\t\t"+noOfTAblets.get()+"\n")
    txt_frame.insert(END,"Issue date:\t\t"+issuedate.get()+"\n")
    txt_frame.insert(END,"Exp. date:\t\t"+expdate.get()+"\n")
    txt_frame.insert(END,"Daily Dose:\t\t"+dailydose.get()+"\n")
    txt_frame.insert(END,"Side Effects:\t\t"+sideeffects.get()+"\n")
    txt_frame.insert(END,"Blood Pressure:\t\t"+bloodpressure.get()+"\n")
    txt_frame.insert(END,"Storage Device:\t\t"+storage.get()+"\n")
    txt_frame.insert(END,"Medication:\t\t"+medication.get()+"\n")
    txt_frame.insert(END,"Patient ID:\t\t"+pID.get()+"\n")
    txt_frame.insert(END,"Name of Patient:\t\t"+nameofPatient.get()+"\n")
    txt_frame.insert(END,"DOB:\t\t"+dob.get()+"\n")
    txt_frame.insert(END,"Patient Address:\t\t"+patientAddress.get()+"\n")

#     Delete Button fn
def delete():
    con = mysql.connector.connect(host="localhost", username="root", password="Vineet@8816", database="mydata")
    mycursor = con.cursor()
    query = ("delete from hospital1 where Reference=%s")
    value = (ref.get(),)
    mycursor.execute(query,value)
    con.commit()
    con.close()
    fetch_data()
    messagebox.showinfo("Deleted","Patient data has been deleted.")

# Clear Buttn fn
def clear():
    nameoftablets.set("")
    ref.set("")
    dose.set("")
    noOfTAblets.set("")
    issuedate.set("")
    expdate.set("")
    dailydose.set("")
    sideeffects.set("")
    bloodpressure.set("")
    storage.set("")
    medication.set("")
    pID.set("")
    nameofPatient.set("")
    dob.set("")
    patientAddress.set("")
    txt_frame.delete(1.0,END)


# Exit button fn
def exit():
    confirm = messagebox.askyesno("Confirmation","Are You Sure You Want To Exit?")
    if confirm>0:
        win.destroy()
        return

# Label/Heading
Label(win,text="Hospital Management System",font="impack 31 bold",bg="red",fg="white").pack(fill=X)

# Frame1
frame1=Frame(win,bd=15,relief=RIDGE)
frame1.place(x=0,y=54,width=1535,height=310)

# Label Frame for patient info
lf1 = LabelFrame(frame1,text="Patient Information",font="arial 10 bold",bd=10,bg="pink")
lf1.place(x=10,y=0,width=900,height=280)

# Labels for Patient Info
Label(lf1,text="Name of Tablets",bg="pink").place(x=5,y=10)
Label(lf1,text="Reference No.",bg="pink").place(x=5,y=40)
Label(lf1,text="Dose",bg="pink").place(x=5,y=70)
Label(lf1,text="No. Of Tablets",bg="pink").place(x=5,y=100)
Label(lf1,text="Issue Date",bg="pink").place(x=5,y=130)
Label(lf1,text="Exp. Date",bg="pink").place(x=5,y=160)
Label(lf1,text="Daily Dose",bg="pink").place(x=5,y=190)
Label(lf1,text="Side Effects",bg="pink").place(x=5,y=220)
Label(lf1,text="Blood Pressure",bg="pink").place(x=370,y=10)
Label(lf1,text="Storage Device",bg="pink").place(x=370,y=40)
Label(lf1,text="Medication",bg="pink").place(x=370,y=70)
Label(lf1,text="Patient ID",bg="pink").place(x=370,y=100)
Label(lf1,text="Name of Patient",bg="pink").place(x=370,y=130)
Label(lf1,text="DOB",bg="pink").place(x=370,y=160)
Label(lf1,text="Patient Address",bg="pink").place(x=370,y=190)

# TextVariable for every field
nameoftablets = StringVar()
ref = StringVar()
dose = StringVar()
noOfTAblets = StringVar()
issuedate = StringVar()
expdate = StringVar()
dailydose = StringVar()
sideeffects = StringVar()
bloodpressure = StringVar()
storage = StringVar()
medication = StringVar()
pID = StringVar()
nameofPatient = StringVar()
dob = StringVar()
patientAddress = StringVar()

# Entry Fields for All Labels
e1 = Entry(lf1,bd=4,textvariable=nameoftablets)
e1.place(x=130,y=10,width=200)

e2 = Entry(lf1,bd=4,textvariable=ref)
e2.place(x=130,y=40,width=200)

e3 = Entry(lf1,bd=4,textvariable=dose)
e3.place(x=130,y=70,width=200)

e4 = Entry(lf1,bd=4,textvariable=noOfTAblets)
e4.place(x=130,y=100,width=200)

e5 = Entry(lf1,bd=4,textvariable=issuedate)
e5.place(x=130,y=130,width=200)

e6 = Entry(lf1,bd=4,textvariable=expdate)
e6.place(x=130,y=160,width=200)

e7 = Entry(lf1,bd=4,textvariable=dailydose)
e7.place(x=130,y=190,width=200)

e8 = Entry(lf1,bd=4,textvariable=sideeffects)
e8.place(x=130,y=220,width=200)

e9 = Entry(lf1,bd=4,textvariable=bloodpressure)
e9.place(x=500,y=10,width=200)

e10 = Entry(lf1,bd=4,textvariable=storage)
e10.place(x=500,y=40,width=200)

e11 = Entry(lf1,bd=4,textvariable=medication)
e11.place(x=500,y=70,width=200)

e12 = Entry(lf1,bd=4,textvariable=pID)
e12.place(x=500,y=100,width=200)

e13 = Entry(lf1,bd=4,textvariable=nameofPatient)
e13.place(x=500,y=130,width=200)

e14 = Entry(lf1,bd=4,textvariable=dob)
e14.place(x=500,y=160,width=200)

e15 = Entry(lf1,bd=4,textvariable=patientAddress)
e15.place(x=500,y=190,width=200)



# Label Frame for prescription
lf2 = LabelFrame(frame1,text="Prescription",font="arial 12 bold",bd=10)
lf2.place(x=920,y=0,width=470,height=280)

# TextBox for Prescription
txt_frame = Text(lf2,font="impack 10 bold",width=40,height=30,bg="orange")
txt_frame.pack(fill=BOTH)

# Frame2
frame2=Frame(win,bd=15,relief=RIDGE)
frame2.place(x=0,y=360,width=1535,height=330)

# Button
# Delete button
d_btn=Button(win,text="Delete",font="arial 15 bold",bg="red",fg="white",bd=6,cursor="hand2",command=delete)
d_btn.place(x=0,y=700,width=270)
# Prescription button
p_btn=Button(win,text="Prescription",font="arial 15 bold",bg="green",fg="white",bd=6,cursor="hand2",command=pre)
p_btn.place(x=270,y=700,width=330)
# Save Prescription data
pd_btn=Button(win,text="Save Prescription Data",font="arial 15 bold",bg="Blue",fg="white",bd=6,cursor="hand2",command=pd)
pd_btn.place(x=600,y=700,width=340)
# Clear Button
c_btn=Button(win,text="Clear",font="arial 15 bold",bg="orange",fg="white",bd=6,cursor="hand2",command=clear)
c_btn.place(x=940,y=700,width=170)
# Exit Button
e_btn=Button(win,text="Exit",font="arial 15 bold",bg="red",fg="white",bd=6,cursor="hand2",command=exit)
e_btn.place(x=1110,y=700,width=170)

# Scroll Bar for Prescription data
scroll_x = ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side="bottom",fill="x")

scroll_y = ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side="right",fill="y")

table = ttk.Treeview(frame2,columns=("not","ref","dose","nots","issd","expd","dd","sd","pn","dob","pa"),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)

scroll_x = ttk.Scrollbar(command=table.xview)
scroll_y = ttk.Scrollbar(command=table.yview)

# Table Headings for Prescription Data
table.heading("not",text="Name Of Tablets")
table.heading("ref",text="Reference No.")
table.heading("dose",text="Dose")
table.heading("nots",text="No. Of Tablets")
table.heading("issd",text="Issue date")
table.heading("expd",text="Exp. date")
table.heading("dd",text="Daily Dose")
table.heading("sd",text="Side Effects")
table.heading("pn",text="Patient Name")
table.heading("dob",text="DOB")
table.heading("pa",text="Patient Address")

table["show"] = "headings"
table.pack(fill=BOTH,expand=1)

# Reducing width of headings
table.column("not",width=100)
table.column("ref",width=100)
table.column("dose",width=100)
table.column("nots",width=100)
table.column("issd",width=100)
table.column("expd",width=100)
table.column("dd",width=100)
table.column("sd",width=100)
table.column("pn",width=100)
table.column("dob",width=100)
table.column("pa",width=100)

table.bind("<ButtonRelease-1>",get_data)

fetch_data()







mainloop()