import tkinter as tk
from tkinter import messagebox

class ConcertBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Concert Booking System")

        # User data
        self.user_details = {'Name': '', 'Email': '', 'Phone': ''}

        # Ticket data
        self.ticket_price = 50
        self.selected_seat = tk.StringVar()
        self.total_tickets = 0

        # GUI elements
        self.create_user_details_screen()

    def create_user_details_screen(self):
        self.user_details_frame = tk.Frame(self.root)
        self.user_details_frame.pack(padx=20, pady=20)

        tk.Label(self.user_details_frame, text="Name:").grid(row=0, column=0, sticky="e")
        tk.Label(self.user_details_frame, text="Email:").grid(row=1, column=0, sticky="e")
        tk.Label(self.user_details_frame, text="Phone:").grid(row=2, column=0, sticky="e")

        self.name_entry = tk.Entry(self.user_details_frame)
        self.email_entry = tk.Entry(self.user_details_frame)
        self.phone_entry = tk.Entry(self.user_details_frame)

        self.name_entry.grid(row=0, column=1)
        self.email_entry.grid(row=1, column=1)
        self.phone_entry.grid(row=2, column=1)

        next_button = tk.Button(self.user_details_frame, text="Next", command=self.create_seat_selection_screen)
        next_button.grid(row=3, column=0, columnspan=2, pady=10)

    def create_seat_selection_screen(self):
        self.user_details['Name'] = self.name_entry.get()
        self.user_details['Email'] = self.email_entry.get()
        self.user_details['Phone'] = self.phone_entry.get()

        self.user_details_frame.destroy()

        seat_selection_frame = tk.Frame(self.root)
        seat_selection_frame.pack(padx=20, pady=20)

        tk.Label(seat_selection_frame, text=f"Welcome, {self.user_details['Name']}!").grid(row=0, column=0, columnspan=2)

        # Seat selection
        tk.Label(seat_selection_frame, text="Select Seat:").grid(row=1, column=0, sticky="e")
        seat_dropdown = tk.OptionMenu(seat_selection_frame, self.selected_seat, "A1", "A2", "B1", "B2")
        seat_dropdown.grid(row=1, column=1)

        # Ticket booking
        tk.Button(seat_selection_frame, text="Book Ticket", command=self.book_ticket).grid(row=2, column=0, columnspan=2, pady=10)

    def book_ticket(self):
        if self.selected_seat.get():
            self.total_tickets += 1
            self.display_booking_summary()
        else:
            messagebox.showerror("Error", "Please select a seat.")

    def display_booking_summary(self):
        booking_summary = f"Booking Summary\nName: {self.user_details['Name']}\nEmail: {self.user_details['Email']}\n" \
                          f"Phone: {self.user_details['Phone']}\nSelected Seat: {self.selected_seat.get()}\n" \
                          f"Total Tickets: {self.total_tickets}\nTotal Cost: ${self.calculate_total_cost():.2f}"

        messagebox.showinfo("Booking Summary", booking_summary)

    def calculate_total_cost(self):
        total_cost = self.total_tickets * self.ticket_price
        discount = 0.1  # 10% discount for demonstration purposes
        total_cost -= total_cost * discount

        tax_rate = 0.05  # 5% tax for demonstration purposes
        total_cost += total_cost * tax_rate

        return total_cost

if __name__ == "__main__":
    root = tk.Tk()
    app = ConcertBookingSystem(root)
    root.mainloop()
