from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END

import psycopg2

root = Tk()
root.title("Python & PosgreSQL")


def save_new_student(name, age, address):
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''INSERT INTO students(name, age, address) VALUES (%s, %s, %s)'''
    cursor.execute(query, (name, age, address))
    print("succesfully data inserted")
    conn.commit()
    conn.close()
    # refresh with new students
    display_students()


def search(id):
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''SELECT * FROM students where id=%s'''
    cursor.execute(query, (id))

    row = cursor.fetchone()
    print(row)
    display_search_result(row)

    conn.commit()
    conn.close()


def display_search_result(row):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, columnspan=4, sticky=W+E)
    listbox.insert(END, row)


def display_students():
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''SELECT * FROM students'''
    cursor.execute(query)

    row = cursor.fetchall()

    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=10, columnspan=4, sticky=W+E)
    for x in row:
      listbox.insert(END, x)

    conn.commit()
    conn.close()


# Canva
canvas = Canvas(root, height=380, width=400)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text="Add a Student")
label.grid(row=0, column=1)

# Name Input
label = Label(frame, text="Name")
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)
entry_name.focus()

# Age
label = Label(frame, text="Age")
label.grid(row=2, column=0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

# Address
label = Label(frame, text="Address")
label.grid(row=3, column=0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

# Button
button = Button(frame, text="Add", command=lambda: save_new_student(
    entry_name.get(), entry_age.get(), entry_address.get()))
button.grid(row=4, column=1, sticky=W+E)

# Search
label = Label(frame, text="Search Data")
label.grid(row=5, column=1)

label = Label(frame, text="Search By ID")
label.grid(row=6, column=0)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

button = Button(frame, text="Search", command=lambda: search(id_search.get()))
button.grid(row=6, column=2)


display_students()
root.mainloop()
