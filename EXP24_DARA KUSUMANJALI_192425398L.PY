import tkinter as tk
from tkinter import messagebox
import mysql.connector
import random


# ---------------- MYSQL CONNECTION ----------------

def connect_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="college_admission"
    )


# ---------------- SIGN UP / NEW ADMISSION ----------------

def signup():

    form = tk.Toplevel(root)
    form.title("NEW ADMISSION")
    form.geometry("700x750")
    form.resizable(False, False)

    tk.Label(
        form,
        text="COLLEGE ADMISSION FORM",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    frame = tk.Frame(form)
    frame.pack()

    # First Name
    tk.Label(frame, text="First Name").grid(
        row=0, column=0, padx=10, pady=10
    )

    firstname = tk.Entry(frame, width=30)
    firstname.grid(row=0, column=1)

    # Last Name
    tk.Label(frame, text="Last Name").grid(
        row=1, column=0, padx=10, pady=10
    )

    lastname = tk.Entry(frame, width=30)
    lastname.grid(row=1, column=1)

    # Age
    tk.Label(frame, text="Age").grid(
        row=2, column=0, padx=10, pady=10
    )

    age = tk.Entry(frame, width=30)
    age.grid(row=2, column=1)

    # Gender
    tk.Label(frame, text="Gender").grid(
        row=3, column=0, padx=10, pady=10
    )

    gender = tk.StringVar(value="Male")

    tk.Radiobutton(
        frame,
        text="Male",
        variable=gender,
        value="Male"
    ).grid(row=3, column=1, sticky="w")

    tk.Radiobutton(
        frame,
        text="Female",
        variable=gender,
        value="Female"
    ).grid(row=3, column=1)

    # Date of Birth
    tk.Label(frame, text="Date of Birth").grid(
        row=4, column=0, padx=10, pady=10
    )

    dob = tk.Entry(frame, width=30)
    dob.grid(row=4, column=1)

    # Community
    tk.Label(frame, text="Community").grid(
        row=5, column=0, padx=10, pady=10
    )

    community = tk.StringVar(value="OC")

    tk.OptionMenu(
        frame,
        community,
        "OC",
        "BC",
        "MBC",
        "SC",
        "ST"
    ).grid(row=5, column=1)

    # State
    tk.Label(frame, text="State").grid(
        row=6, column=0, padx=10, pady=10
    )

    state = tk.StringVar(value="Tamil Nadu")

    tk.OptionMenu(
        frame,
        state,
        "Tamil Nadu",
        "Telangana",
        "Andhra Pradesh",
        "Karnataka",
        "Kerala",
        "Maharashtra"
    ).grid(row=6, column=1)

    # Subjects
    tk.Label(
        frame,
        text="Subjects Studied in Class 12"
    ).grid(
        row=7,
        column=0,
        padx=10,
        pady=10
    )

    maths = tk.BooleanVar()
    physics = tk.BooleanVar()
    chemistry = tk.BooleanVar()
    biology = tk.BooleanVar()
    computer = tk.BooleanVar()
    english = tk.BooleanVar()

    subject_frame = tk.Frame(frame)
    subject_frame.grid(row=7, column=1)

    tk.Checkbutton(
        subject_frame,
        text="Maths",
        variable=maths
    ).pack(anchor="w")

    tk.Checkbutton(
        subject_frame,
        text="Physics",
        variable=physics
    ).pack(anchor="w")

    tk.Checkbutton(
        subject_frame,
        text="Chemistry",
        variable=chemistry
    ).pack(anchor="w")

    tk.Checkbutton(
        subject_frame,
        text="Biology",
        variable=biology
    ).pack(anchor="w")

    tk.Checkbutton(
        subject_frame,
        text="Computer Science",
        variable=computer
    ).pack(anchor="w")

    tk.Checkbutton(
        subject_frame,
        text="English",
        variable=english
    ).pack(anchor="w")

    # Marks
    tk.Label(
        frame,
        text="Total Marks in 12th"
    ).grid(
        row=8,
        column=0,
        padx=10,
        pady=10
    )

    marks = tk.Entry(frame, width=30)
    marks.grid(row=8, column=1)

    # ---------------- SUBMIT ----------------

    def submit():

        if (
            firstname.get() == ""
            or lastname.get() == ""
            or age.get() == ""
            or dob.get() == ""
            or marks.get() == ""
        ):
            messagebox.showerror(
                "Error",
                "Please fill all required fields."
            )
            return

        selected_subjects = []

        if maths.get():
            selected_subjects.append("Maths")

        if physics.get():
            selected_subjects.append("Physics")

        if chemistry.get():
            selected_subjects.append("Chemistry")

        if biology.get():
            selected_subjects.append("Biology")

        if computer.get():
            selected_subjects.append("Computer Science")

        if english.get():
            selected_subjects.append("English")

        subjects = ", ".join(selected_subjects)

        # Generate admission number
        admission_no = random.randint(10000, 99999)

        try:

            conn = connect_database()
            cursor = conn.cursor()

            sql = """
            INSERT INTO student
            (
                admission_no,
                first_name,
                last_name,
                age,
                gender,
                dob,
                community,
                state,
                subjects,
                marks
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            values = (
                admission_no,
                firstname.get(),
                lastname.get(),
                age.get(),
                gender.get(),
                dob.get(),
                community.get(),
                state.get(),
                subjects,
                marks.get()
            )

            cursor.execute(sql, values)

            conn.commit()

            cursor.close()
            conn.close()

            messagebox.showinfo(
                "Admission Successful",
                "Admission Successful!\n\n"
                "Your Admission Number is:\n"
                + str(admission_no)
            )

            form.destroy()

        except mysql.connector.Error as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    tk.Button(
        form,
        text="SUBMIT",
        command=submit,
        width=20
    ).pack(pady=25)


# ---------------- UPDATE EXISTING DETAILS ----------------

def update_details():

    update_window = tk.Toplevel(root)
    update_window.title("EDIT ADMISSION DETAILS")
    update_window.geometry("500x500")
    update_window.resizable(False, False)

    tk.Label(
        update_window,
        text="EDIT ADMISSION DETAILS",
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    tk.Label(
        update_window,
        text="Admission Number"
    ).pack()

    admission_entry = tk.Entry(
        update_window,
        width=30
    )
    admission_entry.pack(pady=10)

    tk.Label(
        update_window,
        text="New First Name"
    ).pack()

    name_entry = tk.Entry(
        update_window,
        width=30
    )
    name_entry.pack(pady=10)

    tk.Label(
        update_window,
        text="New Age"
    ).pack()

    age_entry = tk.Entry(
        update_window,
        width=30
    )
    age_entry.pack(pady=10)

    tk.Label(
        update_window,
        text="New Marks"
    ).pack()

    marks_entry = tk.Entry(
        update_window,
        width=30
    )
    marks_entry.pack(pady=10)

    def update():

        try:

            conn = connect_database()
            cursor = conn.cursor()

            sql = """
            UPDATE student
            SET first_name = %s,
                age = %s,
                marks = %s
            WHERE admission_no = %s
            """

            values = (
                name_entry.get(),
                age_entry.get(),
                marks_entry.get(),
                admission_entry.get()
            )

            cursor.execute(sql, values)

            if cursor.rowcount == 0:

                messagebox.showwarning(
                    "Not Found",
                    "Admission number not found."
                )

            else:

                conn.commit()

                messagebox.showinfo(
                    "Success",
                    "Admission details updated successfully."
                )

            cursor.close()
            conn.close()

        except mysql.connector.Error as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    tk.Button(
        update_window,
        text="UPDATE",
        command=update,
        width=20
    ).pack(pady=20)


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()

root.title("College Admission System")
root.geometry("500x400")
root.resizable(False, False)

tk.Label(
    root,
    text="COLLEGE ADMISSION SYSTEM",
    font=("Arial", 22, "bold")
).pack(pady=50)

tk.Button(
    root,
    text="NEW ADMISSION",
    command=signup,
    width=25,
    height=2
).pack(pady=15)

tk.Button(
    root,
    text="EDIT EXISTING DETAILS",
    command=update_details,
    width=25,
    height=2
).pack(pady=15)

tk.Button(
    root,
    text="EXIT",
    command=root.destroy,
    width=25
).pack(pady=15)

root.mainloop()