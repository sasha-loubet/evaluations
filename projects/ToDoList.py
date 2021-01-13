import PyQt5.QtWidgets as qtw
import pickle
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("ToDoList")

def add():
    task = input_task.get()
    list_tasks.insert(tkinter.END, task)
    input_task.delete(0, tkinter.END)
    #qtw.QMessageBox.about("Champs vide")

def delete():
        task_index = list_tasks.curselection()[0]
        list_tasks.delete(task_index)
        
        #qtw.QMessageBox.about("Sellectionner une tache")

# create the buttons
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

list_tasks = tkinter.Listbox(frame_tasks, height=8, width=45)
list_tasks.pack(side=tkinter.LEFT)

input_task = tkinter.Entry(root, width=45)
input_task.pack()

button_add = tkinter.Button(root, text="Ajouter", width=50, command=add)
button_add.pack()

button_delete_task = tkinter.Button(root, text="Supprimer", width=50, command=delete)
button_delete_task.pack()


root.mainloop()