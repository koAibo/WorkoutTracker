from tkinter import *
import sqlite3
from tkcalendar import *

root = Tk()
root.geometry("400x200")

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
    t_name = 0
    #TODO: move entry to new window, submit button functionality, check name is entered
    def submit():

        conn = sqlite3.connect('workout_logs.db')

        c = conn.cursor()

        c.execute("INSERT INTO exercise VALUES (:e_name, :sets, :weight, :reps, :date )",
                  {
                      'e_name': e_name.get(),
                      'sets': sets.get(),
                      'weight': weight.get(),
                      'reps': reps.get(),
                      'date' :cal.get_date()
                  })
        if t_name == 0 :
            t_name += 1
            c.execute("INSERT INTO workouts VALUES (:date, :name)",
                    {
                        'name':name_entry.get(),
                        'date': cal.get_date()
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
    workout_in.geometry("360x700")
    #workout name label
    name_label = Label(workout_in, text="Workout Name" )
    name_label.grid(row=0, column=0, columnspan=1, padx=5)

    #workout name extry
    name_entry = Entry(workout_in, width=20)
    name_entry.grid(row=0, column=1, columnspan=2, pady=10, padx=20)

    # calendar widget 
    cal = Calendar(workout_in, selectmode="day", year=2023, month=5,day=16)
    cal.grid(row=1, columnspan=2, pady=20)

    # workout labels
    e_name_label = Label(workout_in, text="Exercise name")
    e_name_label.grid(row=10, column=0)
    sets_label = Label(workout_in, text="Sets")
    sets_label.grid(row=11, column=0)
    weight_label = Label(workout_in, text="Weight (lbs)")
    weight_label.grid(row=12, column=0)
    reps_label = Label(workout_in, text="Reps")
    reps_label.grid(row=13, column=0)

    # new_workout input boxes
    e_name = Entry(workout_in, width=20)
    e_name.grid(row=10, column=1, padx=20)
    sets = Entry(workout_in, width=20)
    sets.grid(row=11, column=1, padx=20)
    weight = Entry(workout_in, width=20)
    weight.grid(row=12, column=1, padx=20)
    reps = Entry(workout_in, width=20)
    reps.grid(row=13, column=1, padx=20)

    submit_btn = Button(workout_in, text="Save", command=submit)
    submit_btn.grid(row=1000, column=1, columnspan=1, pady=10, padx=10, ipadx=50)


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




# loop the gui
root.mainloop()
