from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from ttkbootstrap import Style
from tkcalendar import DateEntry
from tkinter import messagebox

m = Tk()
m.geometry("800x700")

var1 = StringVar()
var2 = StringVar()

def add_task():
    task = entry.get()
    if task != "Enter task" and task != "":
        listbox.insert(END, task)
        entry.delete(0, END)

def delete_tasks(l):
    selected_tasks = l.curselection()
    for i in selected_tasks[::-1]:
        l.delete(i)

def active_entry(event):
    if entry.get() == "Enter task":
        entry.delete(0, END)


def unactive_entry(event):
    if not entry.get():
        entry.insert(0, "Enter task")  

def clear_tasks():
    listbox.delete(0, END)

def set_theme(theme_name):
    style.theme_use(theme_name)

# to insert edited text
def replace(i):
    edited_text = entry.get()
    if edited_text != "Enter task":
        listbox.delete(i)
        listbox.insert(i, edited_text)
        entry.delete(0, END)
        confirm_button.place_forget()
        add_button.place(x=380, y=70)
    else:
        messagebox.showerror("Error", "Enter Edited Text.")

def complete_task():
    selected_indices = listbox.curselection()
    if selected_indices:
        for index in selected_indices:
            # Get the text of the selected item
            task_text = listbox.get(index)
            completed_task_text = f"\u0336".join(task_text)  # adding a strikethrough
            # Delete the original item from the listbox and insert the text with the strikethrough
            listbox.delete(index)
            listbox.insert(index, completed_task_text)
    else:
        messagebox.showerror("Error", "No task selected.")


# Function to handle the click event on a listbox item
def on_item_click(event):
    # Function to handle the edit command in the menu
    def edit_task(selected_indices):
        if len(selected_indices) == 1:
            selected_index = selected_indices[0]
            task_text = listbox.get(selected_index)
            entry.delete(0, END)    # if not empty, clear entry
            entry.insert(0, task_text)
            add_button.place_forget()
            confirm_button.place(x=380, y=70)
            confirm_button.config(command=lambda: replace(selected_index))

        else:
            messagebox.showerror("Error", "No task selected.")
    
    popup_menu = Menu(m, tearoff=0)
    popup_menu.add_command(label="Edit", command=lambda: edit_task(listbox.curselection()))
    # Display the pop-up menu at the mouse coordinates
    popup_menu.post(event.x_root, event.y_root)

def leaveForTmr_add():
    # Get the indices of the selected items in listbox
    selected_indices = listbox.curselection()
    if selected_indices:
        # Deleting in reverse order to avoid index issues
        for index in selected_indices[::-1]:
            task_text = listbox.get(index)
            if "\u0336" in task_text:
                messagebox.showerror("Error", "Cannot add completed task.")
                listbox.selection_clear(0, END)
            else:
                leaveForTmr_listbox.insert(0, task_text)
                listbox.delete(index)  # Delete task from original listbox
    else:
        messagebox.showerror("Error", "No task selected.")


def active_event(event):
    if event_entry.get() == "Add title":
        event_entry.delete(0, END)

def unactive_event(event):
    if not event_entry.get():
        event_entry.insert(0, "Add title")

def add_event():
    date = d_entry.get()
    event = event_entry.get()
    if event != "Add title":
        tree.insert('', 'end', values=(date, event), tags='font')
        event_entry.delete(0, END)

def delete_event():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)


# Open an image file using PIL/Pillow
image = Image.open(r"D:\Codsoft\to-do\todo_bg.png")
tk_image = ImageTk.PhotoImage(image)

# Create a canvas
canvas = Canvas(m, bg="bisque2", width=800, height=4000)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, anchor=NW, image=tk_image)

# Adding theme Menu and commands 
menubar = Menu(m)
theme = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label='Change Theme', menu=theme) 
style = Style() #creates an instance
theme_options = ['minty', 'journal', 'cosmo', 'solar','flatly', 'lumen', 'pulse', 'sandstone', 'morph']
for option in theme_options:
    theme.add_command(label=option, command=lambda theme_name=option: set_theme(theme_name),activebackground="lightcyan4", activeforeground="white") 
#set default theme
default_theme = 'journal'
set_theme(default_theme)

entry = Entry(m, textvariable=var1,relief=RIDGE,background="#D4BFBB", foreground="grey30",font=('Segoe Print', 11, 'bold'))
entry.place(x=65, y=97,width=240, height=30)
entry.insert(0, "Enter task")
entry.bind("<FocusIn>", active_entry)
entry.bind("<FocusOut>", unactive_entry)

listbox = Listbox(m, selectmode="multiple", background="#FDEEEE", font=('Segoe Print', 10, 'bold'), selectbackground="mistyrose4",fg="indianred4")
listbox.place(x=50, y=210, height=420, width=280)
listbox.bind("<Button-3>", on_item_click)

leaveForTmr_listbox = Listbox(m, selectmode="multiple", background="#DFE2E6", font=('Segoe Print', 9, 'bold'), selectbackground="mistyrose4",fg="indianred4")
leaveForTmr_listbox.place(x=550, y=90, height=170, width=180)

label1= ttk.Label(text="Tasks:", font=("broadway", 14), background='#D4BFBB')
label1.place(x=100, y=180,)

add_button = ttk.Button(m, text="ADD", command=add_task, style="secondary.Outline.TButton", width=15)
add_button.place(x=380, y=70)

del_button = ttk.Button(m, text="DELETE", command= lambda:delete_tasks(listbox), style="primary.Outline.TButton", width=15)
del_button.place(x=380, y=115)

clear_button = ttk.Button(m, text="Clear List", command=clear_tasks, style="secondary.Outline.TButton", width=15)
clear_button.place(x=210, y=595)

#initially hidden
confirm_button = ttk.Button(m, text="Confirm Edit", style="primary.TButton", width=15)

task_commpleted_but = ttk.Button(m, text="COMPLETED", style="secondary.Outline.TButton", width=15, command=complete_task)
task_commpleted_but.place(x=380, y=160)

add_icon = PhotoImage(file=r"D:\Codsoft\to-do\add.png")
small_add = add_icon.subsample(25)
leaveForTmr_add_button = ttk.Button(m,command=leaveForTmr_add, style="secondary.Outline.TButton", image=small_add)
leaveForTmr_add_button.place(x=699, y=229)
leaveForTmr_add_button.config(padding=0, takefocus=False)

del_icon = PhotoImage(file=r"D:\Codsoft\to-do\del.png")
small_del = del_icon.subsample(25)
leaveForTmr_del_button = ttk.Button(m,command= lambda: delete_tasks(leaveForTmr_listbox), style="secondary.Outline.TButton", image=small_del)
leaveForTmr_del_button.place(x=670, y=229)
leaveForTmr_del_button.config(padding=0, takefocus=False)  

# for setting an event
event_entry = Entry(m, textvariable=var2,relief=RIDGE,background="mistyrose2", foreground="grey30",font=('Segoe Print', 10, 'bold'))
event_entry.place(x=410, y=400,width=190, height=30)
event_entry.insert(0, "Add title")
event_entry.bind("<FocusIn>", active_event)
event_entry.bind("<FocusOut>", unactive_event)

d_entry = DateEntry(m, style='success.DateEntry')
d_entry.place(x=600, y=400)

f1= Frame(m, background="white")
f1.place(x=410, y=440, width=350, height=160)
tree = ttk.Treeview(f1, height= 8, columns=('Date', 'Event'), style="secondary.Treeview", show="tree")
tree.heading('#0')
tree.heading('#1', text='Date')
tree.heading('#2', text='Event')
tree.column("#0", width=0)
tree.column('#1', width=100)
tree.column('#2', width=237)
tree.grid(row=0, column=0)
tree.tag_configure('font', font=('Segoe Print', 10))
scrollbar = ttk.Scrollbar(m, command=tree.yview)
style.configure("Vertical.TScrollbar", background="silver", troughcolor="white", bordercolor="black", arrowcolor="indianred4")
scrollbar.place(x=751, y=440, height=160)
tree.config(yscrollcommand=scrollbar.set)


style2 = ttk.Style()
style2.configure('Treeview', background='mistyrose2')

event_add_button = ttk.Button(m, text="Add", command=add_event, style="primary.Link.TButton")
event_add_button.place(x=706, y=400)

delete_button = ttk.Button(m, text="Delete Event", command=delete_event, style="primary.Outline.TButton")
delete_button.place(x=540, y=610)

m.config(menu = menubar)
m.mainloop()
