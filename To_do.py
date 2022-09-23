from tkinter import *
from tkinter import messagebox

root = Tk()
root.configure(background = "ghost white")
root.title("To Do Application")
root.geometry("515x210")

list1 = []

# functions
# clearing the entry field
def clear_taskfield():
    entrybox.delete(0, END)

def inputerror():
    if entrybox.get() == "":
        messagebox.showerror("Error", "Enter task")
        return 0
    return 1

#insert function
def addtask():
    value = inputerror()
    if value == 0:
        return
    content= entrybox.get()
    list1.append(content)
    taskslist.insert(10000, content)
    clear_taskfield()

def delete():
    taskslist.delete(ANCHOR)

def delete_all():
    mb = messagebox.askyesno('Delete All', 'Are you sure?')
    if mb == True:
        taskslist.delete(0, END)

def movetask():
    completedtaskslist.insert(END, taskslist.get(ANCHOR))
    taskslist.delete(ANCHOR)

def exit1():
    print(list1)
    root.destroy()

#  Buttons
entrylabel = Label(root, text="Enter the task", background = "ghost white")
taskslabel = Label(root, text="List of tasks", background = "ghost white")
completedlabel = Label(root, text="Completed tasks", background = "ghost white")
entrybox = Entry(root, width=21)
taskslist = Listbox(root, height=11, width=25, selectmode="SINGLE")
completedtaskslist = Listbox(root, height=11, width=25, selectmode="SINGLE")
addbutton = Button(root, text="Add task", width=20, command = addtask)
deletebutton = Button(root, text="Delete", width=20, command = delete)
deleteallbutton = Button(root, text="Delete All", width=20, command = delete_all)
movebutton = Button(root, text="Move to Completed Task", width=20, command = movetask)
exitbutton = Button(root, text="Exit", width=20, command = exit1)

entrylabel.grid(row=1, column=0, padx=10)
taskslabel.grid(row=1, column=1, padx=10)
completedlabel.grid(row=1, column=2, padx=90)
entrybox.grid(row=2, column=0, padx=10, pady=2)
taskslist.place(x=180, y=20)
completedtaskslist.place(x=350, y=20)
addbutton.grid(row=3, column=0, padx=10, pady=2)
deletebutton.grid(row=4, column=0, padx=10, pady=2)
deleteallbutton.grid(row=5, column=0, padx=10, pady=2)
movebutton.grid(row=6, column=0, padx=10, pady=2)
exitbutton.grid(row=7, column=0, padx=10, pady=2)

root.mainloop()