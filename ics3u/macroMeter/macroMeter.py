import tkinter as tk
from tkinter import ttk, messagebox
import json
import hashlib
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import openai
from PIL import Image, ImageTk

# Global variables
root = None
current_frame = None
current_user = None
theme = "light"
OPENAI_API_KEY = "your-api-key-here"  # Replace with your actual API key

# Theme colors
THEMES = {
    "light": {
        "bg": "#ffffff",
        "fg": "#000000",
        "button": "#e0e0e0",
        "accent": "#007bff"
    },
    "dark": {
        "bg": "#2d2d2d",
        "fg": "#ffffff",
        "button": "#404040",
        "accent": "#0d6efd"
    }
}

# Create icons directory if it doesn't exist
if not os.path.exists('icons'):
    os.makedirs('icons')

# Create placeholder icons (you can replace these with actual icons later)
def create_placeholder_icon(name, size=(32, 32)):
    img = Image.new('RGB', size, color='gray')
    img.save(f'icons/{name}.png')

# Create placeholder icons for navigation
for icon in ['ai', 'sleep', 'home', 'workout', 'nutrition', 'settings']:
    create_placeholder_icon(icon)

def clear_window():
    """Clear all widgets from the window"""
    global current_frame
    if current_frame:
        current_frame.destroy()
    current_frame = ttk.Frame(root)
    current_frame.pack(fill='both', expand=True)

def hash_password(password):
    """Hash the password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def save_user(username, password):
    """Save user credentials to JSON file"""
    users = {}
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            users = json.load(f)
    
    users[username] = {
        "password": hash_password(password),
        "basic_info": {},
        "nutrition": [],
        "workouts": [],
        "sleep": [],
        "settings": {
            "theme": "light",
            "ai_enabled": True
        }
    }
    
    with open('users.json', 'w') as f:
        json.dump(users, f)

def verify_user(username, password):
    """Verify user credentials"""
    if not os.path.exists('users.json'):
        return False
    
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    return username in users and users[username]["password"] == hash_password(password)

def save_user_data(username, data_type, data):
    """Save user data to JSON file"""
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    if data_type == "basic_info":
        users[username]["basic_info"] = data
    elif data_type in ["nutrition", "workouts", "sleep"]:
        users[username][data_type].append(data)
    elif data_type == "settings":
        users[username]["settings"] = data
    
    with open('users.json', 'w') as f:
        json.dump(users, f)

def get_user_data(username, data_type):
    """Get user data from JSON file"""
    with open('users.json', 'r') as f:
        users = json.load(f)
    return users[username].get(data_type, {})

def show_basic_info_screen(username):
    """Display the basic info collection screen"""
    clear_window()
    
    # Create a frame for the form with padding
    form_frame = ttk.Frame(current_frame, padding="20")
    form_frame.pack(fill='both', expand=True, pady=10)
    
    # Title
    title_label = ttk.Label(form_frame, text="Basic Information", font=('Helvetica', 20, 'bold'))
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
    
    # Create form fields
    fields = {
        "age": ttk.Entry(form_frame, width=20),
        "gender": ttk.Combobox(form_frame, values=["Male", "Female", "Other"], width=17),
        "birthdate": ttk.Entry(form_frame, width=20),
        "weight": ttk.Entry(form_frame, width=20),
        "height": ttk.Entry(form_frame, width=20),
        "sleep": ttk.Entry(form_frame, width=20),
        "water": ttk.Entry(form_frame, width=20),
        "activity": ttk.Combobox(form_frame, values=[
            "No exercise",
            "Light Exercise",
            "Moderate Exercise",
            "Active",
            "Very Active",
            "Extremely Active"
        ], width=17)
    }
    
    # Add labels and fields
    row = 1
    for label, field in fields.items():
        ttk.Label(form_frame, text=f"{label.title()}:").grid(row=row, column=0, padx=10, pady=3, sticky='e')
        field.grid(row=row, column=1, padx=10, pady=3, sticky='w')
        row += 1
    
    def save_info():
        try:
            # Validate and collect data
            info = {
                "age": int(fields["age"].get()),
                "gender": fields["gender"].get(),
                "birthdate": fields["birthdate"].get(),
                "weight": float(fields["weight"].get()),
                "height": float(fields["height"].get()),
                "sleep": float(fields["sleep"].get()),
                "water": int(fields["water"].get()),
                "activity": fields["activity"].get()
            }
            
            # Validate date format
            datetime.strptime(info["birthdate"], "%Y-%m-%d")
            
            # Save data
            save_user_data(username, "basic_info", info)
            show_main_menu()
            
        except ValueError as e:
            messagebox.showerror("Error", "Please fill all fields with valid data")
    
    # Save button
    save_btn = ttk.Button(form_frame, text="Save", command=save_info)
    save_btn.grid(row=row, column=0, columnspan=2, pady=15)

def show_main_menu():
    """Display the main menu with overview"""
    clear_window()
    
    # Title
    title_label = ttk.Label(current_frame, text="Overview", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=20)
    
    # Get user data
    user_data = get_user_data(current_user, "basic_info")
    nutrition_data = get_user_data(current_user, "nutrition")
    sleep_data = get_user_data(current_user, "sleep")
    workout_data = get_user_data(current_user, "workouts")
    
    # Create overview cards
    cards_frame = ttk.Frame(current_frame)
    cards_frame.pack(fill='x', padx=20, pady=10)
    
    # Nutrition Card
    nutrition_card = ttk.LabelFrame(cards_frame, text="Nutrition")
    nutrition_card.pack(fill='x', pady=5)
    if nutrition_data:
        latest = nutrition_data[-1]
        ttk.Label(nutrition_card, text=f"Calories: {latest.get('calories', 'N/A')}").pack()
        ttk.Label(nutrition_card, text=f"Protein: {latest.get('protein', 'N/A')}g").pack()
    else:
        ttk.Label(nutrition_card, text="No nutrition data").pack()
    
    # Sleep Card
    sleep_card = ttk.LabelFrame(cards_frame, text="Sleep")
    sleep_card.pack(fill='x', pady=5)
    if sleep_data:
        latest = sleep_data[-1]
        ttk.Label(sleep_card, text=f"Hours: {latest.get('hours', 'N/A')}").pack()
    else:
        ttk.Label(sleep_card, text="No sleep data").pack()
    
    # Workout Card
    workout_card = ttk.LabelFrame(cards_frame, text="Latest Workout")
    workout_card.pack(fill='x', pady=5)
    if workout_data:
        latest = workout_data[-1]
        ttk.Label(workout_card, text=f"{latest.get('name', 'N/A')}").pack()
        ttk.Label(workout_card, text=f"Duration: {latest.get('duration', 'N/A')}").pack()
    else:
        ttk.Label(workout_card, text="No workout data").pack()
    
    # Navigation buttons at bottom
    nav_frame = ttk.Frame(current_frame)
    nav_frame.pack(side='bottom', fill='x', pady=10)
    
    buttons = [
        ("AI", show_ai_chatbot),
        ("Sleep", show_sleep_screen),
        ("Home", show_main_menu),
        ("Workout", show_workout_screen),
        ("Nutrition", show_nutrition_screen),
        ("Settings", show_settings_screen)
    ]
    
    for text, command in buttons:
        btn = ttk.Button(nav_frame, text=text, command=command)
        btn.pack(side='left', expand=True, padx=5)

def show_nutrition_screen():
    """Display the nutrition screen"""
    clear_window()
    
    # Title
    title_label = ttk.Label(current_frame, text="Nutrition", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=20)
    
    # Get user data
    nutrition_data = get_user_data(current_user, "nutrition")
    
    # Nutrition info
    info_frame = ttk.LabelFrame(current_frame, text="Current Nutrition")
    info_frame.pack(fill='x', padx=20, pady=10)
    
    if nutrition_data:
        latest = nutrition_data[-1]
        ttk.Label(info_frame, text=f"Calories: {latest.get('calories', 'N/A')}").pack()
        ttk.Label(info_frame, text=f"Protein: {latest.get('protein', 'N/A')}g").pack()
        ttk.Label(info_frame, text=f"Carbs: {latest.get('carbs', 'N/A')}g").pack()
        ttk.Label(info_frame, text=f"Fats: {latest.get('fats', 'N/A')}g").pack()
    else:
        ttk.Label(info_frame, text="No nutrition data").pack()
    
    # Calorie calculator
    calc_frame = ttk.LabelFrame(current_frame, text="Calorie Calculator")
    calc_frame.pack(fill='x', padx=20, pady=10)
    
    # Add meal button
    add_btn = ttk.Button(current_frame, text="Add Meal", command=show_add_meal_screen)
    add_btn.pack(pady=10)
    
    # Navigation buttons
    show_navigation_buttons()

def show_workout_screen():
    """Display the workout screen"""
    clear_window()
    
    # Title
    title_label = ttk.Label(current_frame, text="Workout", font=('Helvetica', 20, 'bold'))
    title_label.pack(pady=10)
    
    # Create a frame for the content
    content_frame = ttk.Frame(current_frame, padding="10")
    content_frame.pack(fill='both', expand=True)
    
    # Start workout button
    start_btn = ttk.Button(content_frame, text="Start Workout", command=show_workout_tracking, width=20)
    start_btn.pack(pady=10)
    
    # Previous workouts
    workout_data = get_user_data(current_user, "workouts")
    if workout_data:
        for workout in reversed(workout_data[-5:]):  # Show last 5 workouts
            workout_frame = ttk.LabelFrame(content_frame, text=workout.get('name', 'Unnamed Workout'), padding="5")
            workout_frame.pack(fill='x', pady=5)
            ttk.Label(workout_frame, text=f"Date: {workout.get('date', 'N/A')}").pack(anchor='w')
            ttk.Label(workout_frame, text=f"Duration: {workout.get('duration', 'N/A')}").pack(anchor='w')
            if 'exercises' in workout:
                for exercise in workout['exercises']:
                    ttk.Label(workout_frame, 
                             text=f"{exercise['name']}: {exercise['sets']}x{exercise['reps']} @ {exercise['weight']}kg").pack(anchor='w')
    else:
        ttk.Label(content_frame, text="No workout history").pack(pady=10)
    
    # Navigation buttons
    show_navigation_buttons()

def show_workout_tracking():
    """Display the workout tracking screen"""
    clear_window()
    
    # Title
    title_label = ttk.Label(current_frame, text="Track Workout", font=('Helvetica', 20, 'bold'))
    title_label.pack(pady=10)
    
    # Create a frame for the content
    content_frame = ttk.Frame(current_frame, padding="10")
    content_frame.pack(fill='both', expand=True)
    
    # Workout type selection
    type_frame = ttk.LabelFrame(content_frame, text="Workout Type", padding="5")
    type_frame.pack(fill='x', pady=5)
    
    workout_type = tk.StringVar(value="weight")
    ttk.Radiobutton(type_frame, text="Weight Training", variable=workout_type, value="weight").pack(side='left', padx=10)
    ttk.Radiobutton(type_frame, text="Running", variable=workout_type, value="run").pack(side='left', padx=10)
    
    # Workout name
    name_frame = ttk.Frame(content_frame)
    name_frame.pack(fill='x', pady=5)
    ttk.Label(name_frame, text="Workout Name:").pack(side='left')
    name_entry = ttk.Entry(name_frame, width=30)
    name_entry.pack(side='left', padx=5)
    
    # Exercise tracking frame
    exercise_frame = ttk.LabelFrame(content_frame, text="Exercises", padding="5")
    exercise_frame.pack(fill='both', expand=True, pady=5)
    
    exercises = []
    
    def add_exercise():
        exercise = {
            "name": ttk.Entry(exercise_frame, width=20),
            "sets": ttk.Entry(exercise_frame, width=5),
            "reps": ttk.Entry(exercise_frame, width=5),
            "weight": ttk.Entry(exercise_frame, width=5)
        }
        
        row = len(exercises)
        ttk.Label(exercise_frame, text="Exercise:").grid(row=row, column=0, padx=5, pady=2)
        exercise["name"].grid(row=row, column=1, padx=5, pady=2)
        ttk.Label(exercise_frame, text="Sets:").grid(row=row, column=2, padx=5, pady=2)
        exercise["sets"].grid(row=row, column=3, padx=5, pady=2)
        ttk.Label(exercise_frame, text="Reps:").grid(row=row, column=4, padx=5, pady=2)
        exercise["reps"].grid(row=row, column=5, padx=5, pady=2)
        ttk.Label(exercise_frame, text="Weight:").grid(row=row, column=6, padx=5, pady=2)
        exercise["weight"].grid(row=row, column=7, padx=5, pady=2)
        
        exercises.append(exercise)
    
    # Add exercise button
    add_btn = ttk.Button(content_frame, text="Add Exercise", command=add_exercise)
    add_btn.pack(pady=5)
    
    # Timer
    timer_frame = ttk.LabelFrame(content_frame, text="Workout Timer", padding="5")
    timer_frame.pack(fill='x', pady=5)
    
    timer_label = ttk.Label(timer_frame, text="00:00:00", font=('Helvetica', 16))
    timer_label.pack(pady=5)
    
    start_time = None
    timer_running = False
    
    def update_timer():
        if timer_running:
            elapsed = datetime.now() - start_time
            hours = elapsed.seconds // 3600
            minutes = (elapsed.seconds % 3600) // 60
            seconds = elapsed.seconds % 60
            timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            root.after(1000, update_timer)
    
    def toggle_timer():
        nonlocal start_time, timer_running
        if not timer_running:
            start_time = datetime.now()
            timer_running = True
            update_timer()
            timer_btn.config(text="Stop Timer")
        else:
            timer_running = False
            timer_btn.config(text="Start Timer")
    
    timer_btn = ttk.Button(timer_frame, text="Start Timer", command=toggle_timer)
    timer_btn.pack(pady=5)
    
    def save_workout():
        workout_data = {
            "name": name_entry.get(),
            "type": workout_type.get(),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "duration": timer_label.cget("text"),
            "exercises": []
        }
        
        for exercise in exercises:
            workout_data["exercises"].append({
                "name": exercise["name"].get(),
                "sets": exercise["sets"].get(),
                "reps": exercise["reps"].get(),
                "weight": exercise["weight"].get()
            })
        
        save_user_data(current_user, "workouts", workout_data)
        messagebox.showinfo("Success", "Workout saved successfully!")
        show_workout_screen()
    
    # Save button
    save_btn = ttk.Button(content_frame, text="Save Workout", command=save_workout)
    save_btn.pack(pady=10)
    
    # Navigation buttons
    show_navigation_buttons()

def show_sleep_screen():
    """Display the sleep tracking screen"""
    clear_window()
    
    # Title
    title_label = ttk.Label(current_frame, text="Sleep Tracker", font=('Helvetica', 20, 'bold'))
    title_label.pack(pady=10)
    
    # Create a frame for the content
    content_frame = ttk.Frame(current_frame, padding="10")
    content_frame.pack(fill='both', expand=True)
    
    # Sleep data entry
    entry_frame = ttk.LabelFrame(content_frame, text="Add Sleep Data", padding="5")
    entry_frame.pack(fill='x', pady=5)
    
    # Date
    date_frame = ttk.Frame(entry_frame)
    date_frame.pack(fill='x', pady=5)
    ttk.Label(date_frame, text="Date:").pack(side='left')
    date_entry = ttk.Entry(date_frame, width=20)
    date_entry.pack(side='left', padx=5)
    date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
    
    # Sleep hours
    hours_frame = ttk.Frame(entry_frame)
    hours_frame.pack(fill='x', pady=5)
    ttk.Label(hours_frame, text="Hours:").pack(side='left')
    hours_entry = ttk.Entry(hours_frame, width=10)
    hours_entry.pack(side='left', padx=5)
    
    # Sleep quality
    quality_frame = ttk.Frame(entry_frame)
    quality_frame.pack(fill='x', pady=5)
    ttk.Label(quality_frame, text="Quality:").pack(side='left')
    quality_var = tk.StringVar(value="Good")
    quality_combo = ttk.Combobox(quality_frame, textvariable=quality_var, values=["Poor", "Fair", "Good", "Excellent"], width=10)
    quality_combo.pack(side='left', padx=5)
    
    # Notes
    notes_frame = ttk.Frame(entry_frame)
    notes_frame.pack(fill='x', pady=5)
    ttk.Label(notes_frame, text="Notes:").pack(side='left')
    notes_entry = ttk.Entry(notes_frame, width=30)
    notes_entry.pack(side='left', padx=5)
    
    def save_sleep_data():
        try:
            hours = float(hours_entry.get())
            if not 0 <= hours <= 24:
                raise ValueError("Hours must be between 0 and 24")
            
            sleep_data = {
                "date": date_entry.get(),
                "hours": hours,
                "quality": quality_var.get(),
                "notes": notes_entry.get()
            }
            
            save_user_data(current_user, "sleep", sleep_data)
            messagebox.showinfo("Success", "Sleep data saved successfully!")
            
            # Clear entries
            hours_entry.delete(0, 'end')
            notes_entry.delete(0, 'end')
            quality_var.set("Good")
            
            # Update graph
            update_sleep_graph()
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    # Save button
    save_btn = ttk.Button(entry_frame, text="Save Sleep Data", command=save_sleep_data)
    save_btn.pack(pady=10)
    
    # Sleep history graph
    graph_frame = ttk.LabelFrame(content_frame, text="Sleep History", padding="5")
    graph_frame.pack(fill='both', expand=True, pady=5)
    
    def update_sleep_graph():
        # Clear previous graph
        for widget in graph_frame.winfo_children():
            widget.destroy()
        
        # Get sleep data
        sleep_data = get_user_data(current_user, "sleep")
        if sleep_data:
            # Create figure
            fig, ax = plt.subplots(figsize=(6, 3))
            
            # Sort data by date
            sorted_data = sorted(sleep_data, key=lambda x: x['date'])
            dates = [entry['date'] for entry in sorted_data[-7:]]  # Last 7 days
            hours = [entry['hours'] for entry in sorted_data[-7:]]
            
            # Plot data
            ax.bar(dates, hours)
            ax.set_xlabel('Date')
            ax.set_ylabel('Hours of Sleep')
            ax.set_title('Sleep History (Last 7 Days)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            # Add to frame
            canvas = FigureCanvasTkAgg(fig, master=graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)
    
    # Initial graph update
    update_sleep_graph()
    
    # Navigation buttons
    show_navigation_buttons()

def show_settings_screen():
    """Display the settings screen"""
    clear_window()
    
    # Title
    title_label = ttk.Label(current_frame, text="Settings", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=20)
    
    # Theme selection
    theme_frame = ttk.LabelFrame(current_frame, text="Theme")
    theme_frame.pack(fill='x', padx=20, pady=10)
    
    theme_var = tk.StringVar(value=get_user_data(current_user, "settings").get("theme", "light"))
    ttk.Radiobutton(theme_frame, text="Light", variable=theme_var, value="light").pack()
    ttk.Radiobutton(theme_frame, text="Dark", variable=theme_var, value="dark").pack()
    
    # AI Chatbot toggle
    ai_frame = ttk.LabelFrame(current_frame, text="AI Chatbot")
    ai_frame.pack(fill='x', padx=20, pady=10)
    
    ai_var = tk.BooleanVar(value=get_user_data(current_user, "settings").get("ai_enabled", True))
    ttk.Checkbutton(ai_frame, text="Enable AI Chatbot", variable=ai_var).pack()
    
    # Edit basic info button
    edit_btn = ttk.Button(current_frame, text="Edit Basic Info", command=lambda: show_basic_info_screen(current_user))
    edit_btn.pack(pady=10)
    
    def save_settings():
        settings = {
            "theme": theme_var.get(),
            "ai_enabled": ai_var.get()
        }
        save_user_data(current_user, "settings", settings)
        messagebox.showinfo("Success", "Settings saved successfully!")
    
    # Save button
    save_btn = ttk.Button(current_frame, text="Save Settings", command=save_settings)
    save_btn.pack(pady=10)
    
    # Navigation buttons
    show_navigation_buttons()

def show_ai_chatbot():
    """Display the AI chatbot screen"""
    clear_window()
    
    # Title
    title_label = ttk.Label(current_frame, text="AI Nutrition Assistant", font=('Helvetica', 20, 'bold'))
    title_label.pack(pady=10)
    
    # Chat display
    chat_frame = ttk.Frame(current_frame, padding="10")
    chat_frame.pack(fill='both', expand=True)
    
    # Create a text widget for chat history
    chat_history = tk.Text(chat_frame, wrap=tk.WORD, height=15, width=40)
    chat_history.pack(fill='both', expand=True, pady=5)
    chat_history.config(state='disabled')
    
    # Message input
    input_frame = ttk.Frame(current_frame, padding="10")
    input_frame.pack(fill='x', pady=5)
    
    message_entry = ttk.Entry(input_frame, width=30)
    message_entry.pack(side='left', fill='x', expand=True, padx=(0, 5))
    
    def get_ai_response(message):
        try:
            openai.api_key = OPENAI_API_KEY
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful nutrition assistant. Provide concise, accurate advice about nutrition, diet, and healthy eating habits."},
                    {"role": "user", "content": message}
                ],
                max_tokens=150
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"I apologize, but I'm having trouble connecting to the AI service. Please check your API key and internet connection. Error: {str(e)}"
    
    def send_message():
        message = message_entry.get()
        if message:
            # Add user message to chat
            chat_history.config(state='normal')
            chat_history.insert(tk.END, f"You: {message}\n")
            chat_history.config(state='disabled')
            
            # Get AI response
            response = get_ai_response(message)
            chat_history.config(state='normal')
            chat_history.insert(tk.END, f"AI: {response}\n")
            chat_history.config(state='disabled')
            
            # Clear input and scroll to bottom
            message_entry.delete(0, 'end')
            chat_history.see(tk.END)
    
    send_btn = ttk.Button(input_frame, text="Send", command=send_message, width=8)
    send_btn.pack(side='right')
    
    # Navigation buttons
    show_navigation_buttons()

def show_navigation_buttons():
    """Display the navigation buttons at the bottom of the screen"""
    nav_frame = ttk.Frame(current_frame, padding="5")
    nav_frame.pack(side='bottom', fill='x', pady=5)
    
    buttons = [
        ("AI", show_ai_chatbot),
        ("Sleep", show_sleep_screen),
        ("Home", show_main_menu),
        ("Workout", show_workout_screen),
        ("Nutrition", show_nutrition_screen),
        ("Settings", show_settings_screen)
    ]
    
    for text, command in buttons:
        btn = ttk.Button(nav_frame, text=text, command=command, width=6)
        btn.pack(side='left', expand=True, padx=1)

def show_login_screen():
    """Display the login screen"""
    clear_window()
    
    # Title
    title_label = ttk.Label(current_frame, text="Login", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=30)
    
    # Username
    username_label = ttk.Label(current_frame, text="Username:")
    username_label.pack(pady=(20, 5))
    username_entry = ttk.Entry(current_frame)
    username_entry.pack(pady=5, padx=50, fill='x')
    
    # Password
    password_label = ttk.Label(current_frame, text="Password:")
    password_label.pack(pady=(20, 5))
    password_entry = ttk.Entry(current_frame, show="•")
    password_entry.pack(pady=5, padx=50, fill='x')
    
    # Login button
    def login():
        global current_user
        username = username_entry.get()
        password = password_entry.get()
        
        if verify_user(username, password):
            current_user = username
            user_data = get_user_data(username, "basic_info")
            if not user_data:
                show_basic_info_screen(username)
            else:
                show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    login_btn = ttk.Button(current_frame, text="Login", command=login)
    login_btn.pack(pady=20, padx=50, fill='x')
    
    # Back button
    back_btn = ttk.Button(current_frame, text="Back", command=show_start_screen)
    back_btn.pack(pady=10, padx=50, fill='x')

def show_register_screen():
    """Display the registration screen"""
    clear_window()
    
    # Title
    title_label = ttk.Label(current_frame, text="Register", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=30)
    
    # Username
    username_label = ttk.Label(current_frame, text="Username:")
    username_label.pack(pady=(20, 5))
    username_entry = ttk.Entry(current_frame)
    username_entry.pack(pady=5, padx=50, fill='x')
    
    # Password
    password_label = ttk.Label(current_frame, text="Password:")
    password_label.pack(pady=(20, 5))
    password_entry = ttk.Entry(current_frame, show="•")
    password_entry.pack(pady=5, padx=50, fill='x')
    
    # Confirm Password
    confirm_label = ttk.Label(current_frame, text="Confirm Password:")
    confirm_label.pack(pady=(20, 5))
    confirm_entry = ttk.Entry(current_frame, show="•")
    confirm_entry.pack(pady=5, padx=50, fill='x')
    
    # Register button
    def register():
        username = username_entry.get()
        password = password_entry.get()
        confirm = confirm_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match")
            return
        
        save_user(username, password)
        messagebox.showinfo("Success", "Registration successful! Please login.")
        show_login_screen()
    
    register_btn = ttk.Button(current_frame, text="Register", command=register)
    register_btn.pack(pady=20, padx=50, fill='x')
    
    # Back button
    back_btn = ttk.Button(current_frame, text="Back", command=show_start_screen)
    back_btn.pack(pady=10, padx=50, fill='x')

def show_start_screen():
    """Display the start screen with login and register buttons"""
    clear_window()
    
    # Title
    title_label = ttk.Label(current_frame, text="MacroMeter", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=50)
    
    # Login button
    login_btn = ttk.Button(current_frame, text="Login", command=show_login_screen)
    login_btn.pack(pady=10, padx=50, fill='x')
    
    # Register button
    register_btn = ttk.Button(current_frame, text="Register", command=show_register_screen)
    register_btn.pack(pady=10, padx=50, fill='x')

def main():
    global root
    root = tk.Tk()
    root.title("MacroMeter")
    root.geometry("400x600")  # Increased window size
    root.resizable(False, False)
    
    # Configure style
    style = ttk.Style()
    style.configure("TButton", padding=8, font=('Helvetica', 11))  # Reduced padding and font size
    style.configure("TLabel", font=('Helvetica', 11))
    style.configure("TEntry", padding=4)
    
    # Add padding to the main window
    main_padding = ttk.Frame(root, padding="10")
    main_padding.pack(fill='both', expand=True)
    
    # Start with the start screen
    show_start_screen()
    
    root.mainloop()

if __name__ == "__main__":
    main() 