from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Store Management System | Developed By MMAR")
        self.root.config(bg="white")
        #Title
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Store Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        #Logout_Button
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        
        #Clock
        self.lbl_clock=Label(self.root,text="Welcome To Store Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=70)
        
        #Left_Menu
        self.Menulogo=Image.open("Images/menu_im.png")
        self.Menulogo=self.Menulogo.resize((200,200),Image.BICUBIC)
        self.Menulogo=ImageTk.PhotoImage(self.Menulogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=140,width=200,height=585)
        
        lbl_menulogo=Label(LeftMenu,image=self.Menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)
        
        self.icon_side=PhotoImage(file="images/side.png")
        
        #Menu_Buttons
        lbl_menubutton=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_employees=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_suppliers=Button(LeftMenu,text="Suppliers",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Categories",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Products",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        
        #Content
        self.lbl_employee=Label(self.root,text="List of Employees\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=155,height=150,width=300)
        
        self.lbl_supplier=Label(self.root,text="List of Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=155,height=150,width=300)
        
        self.lbl_category=Label(self.root,text="Categories\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=155,height=150,width=300)
        
        self.lbl_product=Label(self.root,text="Products List\n[ 0 ]",bd=5,relief=RIDGE,bg="#067d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=335,height=150,width=300)
        
        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=335,height=150,width=300)
        
         #Footer
        lbl_footer=Label(self.root,text="SMS-Store Management System | Developed by MMAR\nFor any technical issue contact:+91xxxxxxxxx",font=("times new roman",15),bg="#4d636d",fg="white")
        lbl_footer.pack(side=BOTTOM,fill=X)
        
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.newobj=employeeClass(self.new_win) 
         
if __name__=="_main_":        
        root=Tk()
        obj=IMS(root)
        root.mainloop()
    
