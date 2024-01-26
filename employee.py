from tkinter import*
from PIL import Image,ImageTk
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Store Management System | Developed By MMAR")
        self.root.config(bg="white")

if __name__=="_main_":        
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()