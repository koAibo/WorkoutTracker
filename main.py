from tkinter import *
import sqlite3
from tkcalendar import *

root = Tk()
root.geometry("400x600")

# create or connect to database
connection = sqlite3.connect('workout_logs.db')
curs = connection.cursor()
curs.execute("""CREATE TABLE if not exists exercise (
        e_name text,
        sets integer,
        weight real,
        reps integer,
        date text
        )""")

curs.execute("""CREATE TABLE if not exists workouts (
        date text,
        name text
        )""")

# commit changes
connection.commit()
# close connection
connection.close()


def new_workout():
    # create submit fxn
    def submit():
        conn = sqlite3.connect('workout_logs.db')

        c = conn.cursor()

        c.execute("INSERT INTO exercise VALUES (:e_name, :sets, :weight, :reps )",
                  {
                      'e_name': e_name.get(),
                      'sets': sets.get(),
                      'weight': weight.get(),
                      'reps': reps.get()
                  })

        e_name.delete(0, END)
        sets.delete(0, END)
        weight.delete(0, END)
        reps.delete(0, END)
        # commit changes
        conn.commit()
        # close connection
        conn.close()

    workout_in = Tk()
    workout_in.title("Enter New Workout")
    workout_in.geometry("400x400")

    # new_workout input boxes
    e_name = Entry(workout_in, width=30)
    e_name.grid(row=0, column=1, padx=20)
    sets = Entry(workout_in, width=30)
    sets.grid(row=1, column=1, padx=20)
    weight = Entry(workout_in, width=30)
    weight.grid(row=2, column=1, padx=20)
    reps = Entry(workout_in, width=30)
    reps.grid(row=3, column=1, padx=20)

    # workout labels
    e_name_label = Label(workout_in, text="Exercise name")
    e_name_label.grid(row=0, column=0)
    sets_label = Label(workout_in, text="Sets")
    sets_label.grid(row=1, column=0)
    weight_label = Label(workout_in, text="Weight (lbs)")
    weight_label.grid(row=2, column=0)
    reps_label = Label(workout_in, text="Reps")
    reps_label.grid(row=3, column=0)

    submit_btn = Button(workout_in, text="Save", command=submit)
    submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


def query():
    #delete button and function

    conn = sqlite3.connect('workout_logs.db')
    c = conn.cursor()

    c.execute("SELECT oid, * FROM exercise")
    records = c.fetchall()
    p_records = ''
    for record in records:
        p_records += "ID: " + str(record[0]) + "\n" + str(record[1]) + ": " + str(record[2]) + " sets of " + str(record[4]) + \
                     " with " + str(record[3]) + " lbs" + "\n" + "\n"

#TODO: open this in new window too
    all_w = Tk()
    all_w.title("All Workouts")
    all_w.geometry("300x700")

    query_label = Label(all_w, text=p_records)
    query_label.grid(row=1, column=0, columnspan=2, padx=(0,100))
    conn.commit()
    conn.close()


# add new workout button
new_workout_btn = Button(root, text="New Workout", command=new_workout)
new_workout_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# query button
q_button = Button(root, text="Show Workouts", command=query)
q_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

#workout name label
name_label = Label(root, text="Workout Name" )
name_label.grid(row=7, column=0, columnspan=1, padx=5)

#workout name extry
name_entry = Entry(root, width=20)
name_entry.grid(row=7, column=1, columnspan=2, pady=10, padx=5)

# calendar widget 
cal = Calendar(root, selectmode="day", year=2023, month=5,day=16)
cal.grid(row=20, column=0, columnspan=2, pady=20)


# loop the gui
root.mainloop()
