from tkinter import *

root = Tk()
root.title("Student Management System")
root.geometry("400x450")

# Title
Label(root, text="Student Management System",
      font=("Arial", 14, "bold")).pack(pady=10)

# Name
Label(root, text="Name").pack()
name_entry = Entry(root, width=30)
name_entry.pack()

# Roll Number
Label(root, text="Roll Number").pack()
roll_entry = Entry(root, width=30)
roll_entry.pack()

# Course
Label(root, text="Course").pack()
course_entry = Entry(root, width=30)
course_entry.pack()

# Listbox
student_list = Listbox(root, width=50, height=10)
student_list.pack(pady=10)

# Add Student
def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    course = course_entry.get()

    if name != "" and roll != "" and course != "":
        student_list.insert(END, f"{roll} - {name} - {course}")

        name_entry.delete(0, END)
        roll_entry.delete(0, END)
        course_entry.delete(0, END)

# Delete Student
def delete_student():
    selected = student_list.curselection()
    if selected:
        student_list.delete(selected)

# Clear All
def clear_all():
    student_list.delete(0, END)

# Buttons
Button(root, text="Add Student", command=add_student, width=15).pack(pady=5)
Button(root, text="Delete Student", command=delete_student, width=15).pack(pady=5)
Button(root, text="Clear All", command=clear_all, width=15).pack(pady=5)

root.mainloop()