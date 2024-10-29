import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Predefined admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Predefined list of flights (extended)
flights = {
    '101': {'flight_name': 'AirFly 101', 'source': 'New York', 'destination': 'London', 'date': '2024-10-02', 'time': '08:00 AM'},
    '102': {'flight_name': 'AirFly 102', 'source': 'Los Angeles', 'destination': 'Tokyo', 'date': '2024-10-05', 'time': '09:00 AM'},
    '103': {'flight_name': 'AirFly 103', 'source': 'Chicago', 'destination': 'Miami', 'date': '2024-10-10', 'time': '11:00 AM'},
    '104': {'flight_name': 'AirFly 104', 'source': 'Dallas', 'destination': 'Seattle', 'date': '2024-10-12', 'time': '01:00 PM'},
    '105': {'flight_name': 'AirFly 105', 'source': 'San Francisco', 'destination': 'New York', 'date': '2024-10-15', 'time': '03:00 PM'},
    '106': {'flight_name': 'AirFly 106', 'source': 'Boston', 'destination': 'Chicago', 'date': '2024-10-18', 'time': '04:30 PM'},
    '107': {'flight_name': 'AirFly 107', 'source': 'Miami', 'destination': 'San Francisco', 'date': '2024-10-20', 'time': '05:00 PM'},
    '123': {'flight_name': 'SpiceJet 1616', 'source': 'Mumbai', 'destination': 'Delhi', 'date': '2024-10-28', 'time': '08:00 AM'},
    '124': {'flight_name': 'IndiGo 1717', 'source': 'Bengaluru', 'destination': 'Kolkata', 'date': '2024-11-02', 'time': '09:30 AM'},
    '125': {'flight_name': 'Air India 1818', 'source': 'Chennai', 'destination': 'Hyderabad', 'date': '2024-11-07', 'time': '11:15 AM'},
    '126': {'flight_name': 'GoAir 1919', 'source': 'Pune', 'destination': 'Jaipur', 'date': '2024-11-12', 'time': '01:45 PM'},
    '127': {'flight_name': 'Vistara 2020', 'source': 'Ahmedabad', 'destination': 'Lucknow', 'date': '2024-11-17', 'time': '03:00 PM'},
    '128': {'flight_name': 'AirAsia 2121', 'source': 'Gurgaon', 'destination': 'Coimbatore', 'date': '2024-11-22', 'time': '04:30 PM'},
    '129': {'flight_name': 'Jet Airways 2222', 'source': 'Nagpur', 'destination': 'Bhopal', 'date': '2024-11-27', 'time': '06:00 AM'},
    '130': {'flight_name': 'IndiGo 2323', 'source': 'Visakhapatnam', 'destination': 'Madurai', 'date': '2024-12-01', 'time': '07:15 AM'},
    '131': {'flight_name': 'SpiceJet 2424', 'source': 'Kochi', 'destination': 'Chandigarh', 'date': '2024-12-06', 'time': '08:45 AM'},
    '132': {'flight_name': 'Air India 2525', 'source': 'Guwahati', 'destination': 'Dehradun', 'date': '2024-12-11', 'time': '09:30 AM'},
    '133': {'flight_name': 'GoAir 2626', 'source': 'Mangaluru', 'destination': 'Vadodara', 'date': '2024-12-16', 'time': '10:15 AM'},
    '134': {'flight_name': 'Vistara 2727', 'source': 'Amritsar', 'destination': 'Varanasi', 'date': '2024-12-21', 'time': '11:00 AM'},
    '135': {'flight_name': 'Jet Airways 2828', 'source': 'Nashik', 'destination': 'Raipur', 'date': '2024-12-26', 'time': '12:30 PM'},
    '136': {'flight_name': 'IndiGo 2929', 'source': 'Surat', 'destination': 'Puducherry', 'date': '2024-12-31', 'time': '01:45 PM'},
}

# Dictionary to store user data
users = {}

class AirlineReservationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AirFly.com")
        self.background_images = [
            ImageTk.PhotoImage(Image.open("D:/new peoject/1.png")),
            ImageTk.PhotoImage(Image.open("D:/new peoject/4.png")),
            ImageTk.PhotoImage(Image.open("D:/new peoject/3.png")),
            ImageTk.PhotoImage(Image.open("D:/new peoject/2.png")),
        ]
        self.home_page()

    # Clear the current window
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Create a frame with a background image
    def create_frame(self, page_type):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True, fill="both")

        # Set background image based on page type
        if page_type == 'admin':
            background_label = tk.Label(frame, image=self.background_images[1])
        else:
            background_label = tk.Label(frame, image=self.background_images[0])
        
        background_label.place(relwidth=1, relheight=1)
        return frame

    # Home Page
    def home_page(self):
        self.clear_window()
        frame = self.create_frame('home')
        
        tk.Label(frame, text="Welcome to AirFly.com", font=("Helvetica", 24), bg="lightblue").pack(pady=20)

        tk.Button(frame, text="Admin Login", command=self.admin_login).pack(pady=10)
        tk.Button(frame, text="User Sign In", command=self.user_login).pack(pady=10)
        tk.Button(frame, text="User Sign Up", command=self.user_signup).pack(pady=10)

    # Admin Login Page
    def admin_login(self):
        self.clear_window()
        frame = self.create_frame('admin')
        
        tk.Label(frame, text="Admin Login", font=("Helvetica", 18), bg="lightblue").pack(pady=20)

        tk.Label(frame, text="Username", bg="lightblue").pack(pady=5)
        self.admin_username_entry = tk.Entry(frame)
        self.admin_username_entry.pack(pady=5)

        tk.Label(frame, text="Password", bg="lightblue").pack(pady=5)
        self.admin_password_entry = tk.Entry(frame, show="*")
        self.admin_password_entry.pack(pady=5)

        tk.Button(frame, text="Login", command=self.validate_admin_login).pack(pady=20)
        tk.Button(frame, text="Back", command=self.home_page).pack(pady=10)

    # Validate Admin Login
    def validate_admin_login(self):
        username = self.admin_username_entry.get()
        password = self.admin_password_entry.get()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            self.admin_dashboard()
        else:
            messagebox.showerror("Error", "Invalid Admin Credentials")

    # Admin Dashboard
    def admin_dashboard(self):
        self.clear_window()
        frame = self.create_frame('admin')
        
        tk.Label(frame, text="Admin Dashboard", font=("Helvetica", 18), bg="lightblue").pack(pady=20)

        tk.Button(frame, text="View Booked Flights", command=self.view_booked_flights).pack(pady=10)
        tk.Button(frame, text="Add Flight", command=self.add_flight).pack(pady=10)
        tk.Button(frame, text="Remove Flight", command=self.remove_flight).pack(pady=10)
        tk.Button(frame, text="View All Flights", command=self.view_all_flights).pack(pady=10)
        tk.Button(frame, text="Logout", command=self.home_page).pack(pady=20)

    # User Sign Up
    def user_signup(self):
        self.clear_window()
        frame = self.create_frame('home')
        
        tk.Label(frame, text="User Sign Up", font=("Helvetica", 18), bg="lightblue").pack(pady=20)

        tk.Label(frame, text="Username", bg="lightblue").pack(pady=5)
        self.signup_username_entry = tk.Entry(frame)
        self.signup_username_entry.pack(pady=5)

        tk.Label(frame, text="Password", bg="lightblue").pack(pady=5)
        self.signup_password_entry = tk.Entry(frame, show="*")
        self.signup_password_entry.pack(pady=5)

        tk.Button(frame, text="Sign Up", command=self.register_user).pack(pady=20)
        tk.Button(frame, text="Back", command=self.home_page).pack(pady=10)

    # Register new user
    def register_user(self):
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()

        if username in users:
            messagebox.showerror("Error", "Username already exists")
        else:
            users[username] = {'password': password, 'booked_flights': []}
            messagebox.showinfo("Success", "User registered successfully")
            self.home_page()

    # User Login Page
    def user_login(self):
        self.clear_window()
        frame = self.create_frame('home')
        
        tk.Label(frame, text="User Sign In", font=("Helvetica", 18), bg="lightblue").pack(pady=20)

        tk.Label(frame, text="Username", bg="lightblue").pack(pady=5)
        self.user_username_entry = tk.Entry(frame)
        self.user_username_entry.pack(pady=5)

        tk.Label(frame, text="Password", bg="lightblue").pack(pady=5)
        self.user_password_entry = tk.Entry(frame, show="*")
        self.user_password_entry.pack(pady=5)

        tk.Button(frame, text="Login", command=self.validate_user_login).pack(pady=20)
        tk.Button(frame, text="Back", command=self.home_page).pack(pady=10)

    # Validate user login credentials
    def validate_user_login(self):
        username = self.user_username_entry.get()
        password = self.user_password_entry.get()

        if username in users and users[username]['password'] == password:
            self.enter_travel_details(username)  # Prompt for travel details
        else:
            messagebox.showerror("Error", "Invalid User Credentials")

    # Enter Travel Details (Source and Destination)
    def enter_travel_details(self, username):
        self.clear_window()
        frame = self.create_frame('home')
        
        tk.Label(frame, text="Enter Travel Details", font=("Helvetica", 18), bg="lightblue").pack(pady=20)

        tk.Label(frame, text="Source", bg="lightblue").pack(pady=5)
        self.source_entry = tk.Entry(frame)
        self.source_entry.pack(pady=5)

        tk.Label(frame, text="Destination", bg="lightblue").pack(pady=5)
        self.destination_entry = tk.Entry(frame)
        self.destination_entry.pack(pady=5)

        tk.Button(frame, text="Show Available Flights", command=lambda: self.show_available_flights(username)).pack(pady=20)
        tk.Button(frame, text="Back", command=self.user_login).pack(pady=10)

    # Show available flights based on user input
    def show_available_flights(self, username):
        source = self.source_entry.get()
        destination = self.destination_entry.get()

        self.clear_window()
        frame = self.create_frame('home')
        
        tk.Label(frame, text="Available Flights", font=("Helvetica", 18), bg="lightblue").pack(pady=20)

        flights_found = False  # To track if any flights are found

        for flight_number, flight in flights.items():
            if flight['source'].lower() == source.lower() and flight['destination'].lower() == destination.lower():
                flights_found = True
                flight_details = (f"Flight Number: {flight_number}, "
                                  f"Name: {flight['flight_name']}, "
                                  f"Date: {flight['date']}, "
                                  f"Time: {flight['time']}")
                tk.Label(frame, text=flight_details, bg="lightblue").pack(pady=5)
                tk.Button(frame, text=f"Book Flight {flight_number}", command=lambda fn=flight_number: self.book_flight(fn, username)).pack(pady=5)

        if not flights_found:
            tk.Label(frame, text="No flights available for the selected route.", bg="lightblue").pack(pady=10)

        tk.Button(frame, text="Back", command=lambda: self.enter_travel_details(username)).pack(pady=10)

    # Book a flight for the user
    def book_flight(self, flight_number, username):
        users[username]['booked_flights'].append(flight_number)
        messagebox.showinfo("Success", f"Flight {flight_number} booked successfully!")
        self.enter_travel_details(username)  # Return to travel details

    # View booked flights
    def view_booked_flights(self):
        self.clear_window()
        frame = self.create_frame('admin')
        
        tk.Label(frame, text="Booked Flights", font=("Helvetica", 18), bg="lightblue").pack(pady=20)

        for username, user_info in users.items():
            if user_info['booked_flights']:
                tk.Label(frame, text=f"User: {username}", bg="lightblue").pack(pady=10)
                for flight_number in user_info['booked_flights']:
                    flight = flights[flight_number]
                    flight_details = (f"Flight Number: {flight_number}, "
                                      f"Name: {flight['flight_name']}, "
                                      f"Source: {flight['source']}, "
                                      f"Destination: {flight['destination']}, "
                                      f"Date: {flight['date']}, "
                                      f"Time: {flight['time']}")
                    tk.Label(frame, text=flight_details, bg="lightblue").pack(pady=5)

        tk.Button(frame, text="Back", command=self.admin_dashboard).pack(pady=10)

    # Add a flight
    def add_flight(self):
        self.clear_window()
        frame = self.create_frame('admin')

        tk.Label(frame, text="Add Flight", font=("Helvetica", 18), bg="lightblue").pack(pady=20)

        tk.Label(frame, text="Flight Number", bg="lightblue").pack(pady=5)
        self.flight_number_entry = tk.Entry(frame)
        self.flight_number_entry.pack(pady=5)

        tk.Label(frame, text="Flight Name", bg="lightblue").pack(pady=5)
        self.flight_name_entry = tk.Entry(frame)
        self.flight_name_entry.pack(pady=5)

        tk.Label(frame, text="Source", bg="lightblue").pack(pady=5)
        self.flight_source_entry = tk.Entry(frame)
        self.flight_source_entry.pack(pady=5)

        tk.Label(frame, text="Destination", bg="lightblue").pack(pady=5)
        self.flight_destination_entry = tk.Entry(frame)
        self.flight_destination_entry.pack(pady=5)

        tk.Label(frame, text="Date (YYYY-MM-DD)", bg="lightblue").pack(pady=5)
        self.flight_date_entry = tk.Entry(frame)
        self.flight_date_entry.pack(pady=5)

        tk.Label(frame, text="Time (HH:MM AM/PM)", bg="lightblue").pack(pady=5)
        self.flight_time_entry = tk.Entry(frame)
        self.flight_time_entry.pack(pady=5)

        tk.Button(frame, text="Add Flight", command=self.save_flight).pack(pady=20)
        tk.Button(frame, text="Back", command=self.admin_dashboard).pack(pady=10)

    # Save new flight
    def save_flight(self):
        flight_number = self.flight_number_entry.get()
        flight_name = self.flight_name_entry.get()
        source = self.flight_source_entry.get()
        destination = self.flight_destination_entry.get()
        date = self.flight_date_entry.get()
        time = self.flight_time_entry.get()

        flights[flight_number] = {
            'flight_name': flight_name,
            'source': source,
            'destination': destination,
            'date': date,
            'time': time,
        }

        messagebox.showinfo("Success", "Flight added successfully!")
        self.admin_dashboard()

    # Remove a flight
    def remove_flight(self):
        self.clear_window()
        frame = self.create_frame('admin')

        tk.Label(frame, text="Remove Flight", font=("Helvetica", 18), bg="lightblue").pack(pady=20)

        tk.Label(frame, text="Flight Number", bg="lightblue").pack(pady=5)
        self.remove_flight_number_entry = tk.Entry(frame)
        self.remove_flight_number_entry.pack(pady=5)

        tk.Button(frame, text="Remove Flight", command=self.delete_flight).pack(pady=20)
        tk.Button(frame, text="Back", command=self.admin_dashboard).pack(pady=10)

    # Delete a flight
    def delete_flight(self):
        flight_number = self.remove_flight_number_entry.get()

        if flight_number in flights:
            del flights[flight_number]
            messagebox.showinfo("Success", "Flight removed successfully!")
        else:
            messagebox.showerror("Error", "Flight number does not exist")

        self.admin_dashboard()

    # View all flights
    def view_all_flights(self):
        self.clear_window()
        frame = self.create_frame('admin')

        tk.Label(frame, text="All Flights", font=("Helvetica", 18), bg="lightblue").pack(pady=20)

        for flight_number, flight in flights.items():
            flight_details = (f"Flight Number: {flight_number}, "
                              f"Name: {flight['flight_name']}, "
                              f"Source: {flight['source']}, "
                              f"Destination: {flight['destination']}, "
                              f"Date: {flight['date']}, "
                              f"Time: {flight['time']}")
            tk.Label(frame, text=flight_details, bg="lightblue").pack(pady=5)

        tk.Button(frame, text="Back", command=self.admin_dashboard).pack(pady=10)

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    app = AirlineReservationApp(root)
    root.mainloop()
