import tkinter as tk
from tkinter import messagebox
import sqlite3
import random
import datetime

# ---------------- DATABASE ----------------

conn = sqlite3.connect("Railway.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS passengers (
    ticket_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    source TEXT NOT NULL,
    destination TEXT NOT NULL,
    journey_date TEXT NOT NULL,
    travel_class TEXT NOT NULL,
    phone TEXT NOT NULL
)
""")

conn.commit()


# ---------------- LOGIN WINDOW ----------------

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "dhoni" and password == "844":
        messagebox.showinfo("Login", "CONGRATULATIONS!! LOGIN SUCCESSFUL")
        login_window.destroy()
        booking_window()
    else:
        messagebox.showerror("Login", "LOGIN FAILED! TRY AGAIN")


login_window = tk.Tk()
login_window.title("Railway Reservation")
login_window.geometry("450x350")
login_window.resizable(False, False)

tk.Label(
    login_window,
    text="BHAARATH RAILWAYS",
    font=("Arial", 20, "bold")
).pack(pady=30)

tk.Label(login_window, text="Login ID", font=("Arial", 13)).pack()
username_entry = tk.Entry(login_window, width=25)
username_entry.pack(pady=5)

tk.Label(login_window, text="Password", font=("Arial", 13)).pack()
password_entry = tk.Entry(login_window, width=25, show="*")
password_entry.pack(pady=5)

tk.Button(
    login_window,
    text="LOGIN",
    command=login,
    width=15
).pack(pady=25)


# ---------------- BOOKING WINDOW ----------------

def booking_window():

    window = tk.Tk()
    window.title("Train Ticket Reservation")
    window.geometry("500x650")
    window.resizable(False, False)

    tk.Label(
        window,
        text="TRAIN TICKET RESERVATION",
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    # Source
    tk.Label(window, text="Source").pack()
    source_var = tk.StringVar(value="Select")
    source_menu = tk.OptionMenu(
        window,
        source_var,
        "Howrah",
        "Ajmer"
    )
    source_menu.pack()

    # Destination
    tk.Label(window, text="Destination").pack(pady=(10, 0))
    destination_var = tk.StringVar(value="Select")
    destination_menu = tk.OptionMenu(
        window,
        destination_var,
        "New Delhi",
        "Chandigarh"
    )
    destination_menu.pack()

    # Date
    tk.Label(window, text="Journey Date (DD-MM-YYYY)").pack(pady=(10, 0))
    date_entry = tk.Entry(window)
    date_entry.pack()

    # Class
    tk.Label(window, text="Class").pack(pady=(10, 0))
    class_var = tk.StringVar(value="Select")
    class_menu = tk.OptionMenu(
        window,
        class_var,
        "1A",
        "2A",
        "3A"
    )
    class_menu.pack()

    # Passenger name
    tk.Label(window, text="Passenger Name").pack(pady=(10, 0))
    name_entry = tk.Entry(window)
    name_entry.pack()

    # Age
    tk.Label(window, text="Age").pack(pady=(10, 0))
    age_entry = tk.Entry(window)
    age_entry.pack()

    # Gender
    tk.Label(window, text="Gender").pack(pady=(10, 0))
    gender_var = tk.StringVar(value="Select")
    gender_menu = tk.OptionMenu(
        window,
        gender_var,
        "Male",
        "Female",
        "Other"
    )
    gender_menu.pack()

    # Phone
    tk.Label(window, text="WhatsApp Number").pack(pady=(10, 0))
    phone_entry = tk.Entry(window)
    phone_entry.pack()

    # ---------------- BOOK TICKET ----------------

    def book_ticket():

        source = source_var.get()
        destination = destination_var.get()
        journey_date = date_entry.get()
        travel_class = class_var.get()
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_var.get()
        phone = phone_entry.get()

        if (
            source == "Select"
            or destination == "Select"
            or travel_class == "Select"
            or gender == "Select"
            or not journey_date
            or not name
            or not age
            or not phone
        ):
            messagebox.showerror(
                "Error",
                "Please enter all details."
            )
            return

        # Check date
        try:
            datetime.datetime.strptime(
                journey_date,
                "%d-%m-%Y"
            )
        except ValueError:
            messagebox.showerror(
                "Error",
                "Enter date in DD-MM-YYYY format."
            )
            return

        # Generate ticket number
        ticket_no = random.randint(10000, 99999)

        # Store passenger details
        cursor.execute(
            """
            INSERT INTO passengers
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                ticket_no,
                name,
                age,
                gender,
                source,
                destination,
                journey_date,
                travel_class,
                phone
            )
        )

        conn.commit()

        # Display ticket
        ticket = (
            "\n"
            "================================\n"
            "       BHAARATH RAILWAYS\n"
            "        TRAIN TICKET\n"
            "================================\n"
            f"Ticket No       : {ticket_no}\n"
            f"Passenger Name  : {name}\n"
            f"Age             : {age}\n"
            f"Gender          : {gender}\n"
            f"From            : {source}\n"
            f"To              : {destination}\n"
            f"Journey Date    : {journey_date}\n"
            f"Class           : {travel_class}\n"
            f"WhatsApp No.    : {phone}\n"
            "================================\n"
            "       BOOKING SUCCESSFUL\n"
            "================================"
        )

        messagebox.showinfo(
            "Ticket Generated",
            ticket
        )

        # Save ticket to text file
        with open(
            f"ticket_{ticket_no}.txt",
            "w"
        ) as file:
            file.write(ticket)

        messagebox.showinfo(
            "Ticket Saved",
            f"Ticket saved as ticket_{ticket_no}.txt"
        )

    tk.Button(
        window,
        text="BOOK TICKET",
        command=book_ticket,
        width=20
    ).pack(pady=25)

    window.mainloop()


login_window.mainloop()

conn.close()