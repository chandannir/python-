"""
MacroMeter - Health and Fitness Tracking Application
Created by: Chandan Nir, Rohith Nair, and Alireza Nouhehkhan
Date: 2024

Description:
MacroMeter is a comprehensive health and fitness tracking application that helps users monitor and improve their overall well-being.

Key Features:
1. User Management
   - Secure login and registration system
   - User profile management
   - Settings customization

2. Nutrition Tracking
   - Daily meal logging
   - Calorie tracking
   - Macronutrient Tracking (protein, carbs, fats)
   - Progress visualization

3. Workout Management
   - Weight training tracking
   - Running/distance tracking
   - Exercise history

4. Sleep Monitoring
   - Sleep duration tracking
   - Sleep quality assessment
   - Sleep history visualization
   - Guided breathing exercises

5. AI Assistant
   - Personalized nutrition advice
   - Workout recommendations
   - Sleep improvement tips
   - Real-time health insights

6. Data Visualization
   - Progress charts
   - Performance graphs
   - Trend analysis

7. Settings and Customization
   - Appearance themes (Light/Dark mode)
   - Color scheme options
   - Goal setting
   - User preferences

Technical Features:
- Modern GUI using customtkinter
- Data persistence using JSON
- Secure password hashing
- OpenRouter AI integration
- Cross-platform compatibility
- Responsive design
- Error handling and validation

Dependencies:
- customtkinter
- matplotlib
- openai
- PIL (Python Imaging Library)
- datetime
- json
- hashlib
- os
- platform
- subprocess
"""

import customtkinter as ctk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import hashlib
import os
from datetime import datetime
from openai import OpenAI
from config import OPENROUTER_API_KEY
from PIL import Image, ImageTk
import platform
import subprocess

def validate_api_key(api_key):
    # Validate the OpenRouter API key format
    # Strip any whitespace from the API key
    api_key = api_key.strip()
    print(f"Validating API key: {api_key[:10]}...")  # Debug print first 10 chars
    print(f"API key length: {len(api_key)}")  # Debug print length
    
    if not api_key:
        return False, "API key is empty"
    if not api_key.startswith("sk-or-v1-"):
        return False, "API key should start with 'sk-or-v1-'"
    if len(api_key) != 64:  # OpenRouter keys are exactly 64 characters including prefix
        return False, f"API key length is incorrect (got {len(api_key)}, expected 64)"
    return True, "API key format is valid"

# Initialize OpenAI client with OpenRouter
api_key = OPENROUTER_API_KEY.strip()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    default_headers={
        "HTTP-Referer": "https://github.com/chandannir/python-macroMeter",
        "X-Title": "MacroMeter",
        "Authorization": f"Bearer {api_key}"
    }
)

# Validate API key before configuring
is_valid, message = validate_api_key(OPENROUTER_API_KEY)
if not is_valid:
    print(f"Warning: {message}")
    print("Please check your API key in config.py")
else:
    try:
        # Test the configuration
        print("Testing API configuration...")  # Debug print
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1-0528:free",
            messages=[
                {"role": "system", "content": "Test message"},
                {"role": "user", "content": "Test response"}
            ]
        )
        print("OpenRouter API configured successfully!")
    except Exception as e:
        print(f"Error configuring OpenRouter API: {str(e)}")

# Global variables
root = None
current_frame = None
current_user = None

# Set appearance mode and default color theme
ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

def clear_window():
    # Clear all widgets from the window
    global current_frame
    if current_frame:
        current_frame.destroy()
    current_frame = ctk.CTkFrame(root)
    current_frame.pack(fill='both', expand=True)

    # Add settings button to all screens except login/register
    if current_user:
        show_settings_button()

def hash_password(password):
    # Hash the password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def save_user(username, password):
    # Save user credentials to JSON file
    users = {}
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            users = json.load(f)
    
    users[username] = {
        "password": hash_password(password),
        "basic_info": {},
        "nutrition": [],
        "workouts": [],
        "sleep": []
    }
    
    with open('users.json', 'w') as f:
        json.dump(users, f)

def verify_user(username, password):
    # Verify user credentials
    if not os.path.exists('users.json'):
        return False
    
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    return username in users and users[username]["password"] == hash_password(password)

def save_user_data(username, data_type, data):
    # Save user data to JSON file
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    if data_type == "basic_info":
        users[username]["basic_info"] = data
    elif data_type in ["nutrition", "workouts", "sleep"]:
        users[username][data_type].append(data)
    
    with open('users.json', 'w') as f:
        json.dump(users, f)

def get_user_data(username, data_type):
    # Get user data from JSON file
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    if data_type == "basic_info":
        return users[username]["basic_info"]
    elif data_type in ["nutrition", "workouts", "sleep"]:
        return users[username][data_type]
    return None

def show_start_screen():
    # Display the start screen with login and register buttons
    clear_window()
    
    # Create a frame for the logo
    logo_frame = ctk.CTkFrame(current_frame)
    logo_frame.pack(pady=20)
    
    try:
        # Load and resize the logo
        logo_path = "assets/MacroMeter.png"  # Fixed: correct filename with uppercase M
        if os.path.exists(logo_path):
            logo_image = Image.open(logo_path)
            # Resize logo to a reasonable size (e.g., 200x200 pixels)
            logo_image = logo_image.resize((200, 200), Image.Resampling.LANCZOS)
            logo_photo = ctk.CTkImage(light_image=logo_image, dark_image=logo_image, size=(200, 200))
            
            # Create a label to display the logo
            logo_label = ctk.CTkLabel(logo_frame, image=logo_photo, text="")
            logo_label.pack(pady=10)
        else:
            # If logo file doesn't exist, show a text title instead
            title_label = ctk.CTkLabel(logo_frame, text="MacroMeter", font=('Helvetica', 24, 'bold'))
            title_label.pack(pady=10)
    except Exception as e:
        print(f"Error loading logo: {e}")
        # If logo loading fails, show a text title instead
        title_label = ctk.CTkLabel(logo_frame, text="MacroMeter", font=('Helvetica', 24, 'bold'))
        title_label.pack(pady=10)
    
    # Login button
    login_btn = ctk.CTkButton(current_frame, text="Login", command=show_login_screen)
    login_btn.pack(pady=10, padx=50, fill='x')
    
    # Register button
    register_btn = ctk.CTkButton(current_frame, text="Register", command=show_register_screen)
    register_btn.pack(pady=10, padx=50, fill='x')

def show_login_screen():
    # Display the login screen
    clear_window()
    
    # Title
    title_label = ctk.CTkLabel(current_frame, text="Login", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=30)
    
    # Username
    username_label = ctk.CTkLabel(current_frame, text="Username:")
    username_label.pack(pady=(20, 5))
    username_entry = ctk.CTkEntry(current_frame)
    username_entry.pack(pady=5, padx=50, fill='x')
    
    # Password
    password_label = ctk.CTkLabel(current_frame, text="Password:")
    password_label.pack(pady=(20, 5))
    password_entry = ctk.CTkEntry(current_frame, show="•")
    password_entry.pack(pady=5, padx=50, fill='x')
    
    # Login button
    def login():
        global current_user
        username = username_entry.get()
        password = password_entry.get()
        
        if verify_user(username, password):
            current_user = username
            # Check if user has basic info
            basic_info = get_user_data(username, "basic_info")
            if not basic_info:
                show_basic_info_screen(username)
            else:
                show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    login_btn = ctk.CTkButton(current_frame, text="Login", command=login)
    login_btn.pack(pady=20, padx=50, fill='x')
    
    # Back button
    back_btn = ctk.CTkButton(current_frame, text="Back", command=show_start_screen)
    back_btn.pack(pady=10, padx=50, fill='x')

def show_register_screen():
    # Display the registration screen
    clear_window()
    
    # Title
    title_label = ctk.CTkLabel(current_frame, text="Register", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=30)
    
    # Username
    username_label = ctk.CTkLabel(current_frame, text="Username:")
    username_label.pack(pady=(20, 5))
    username_entry = ctk.CTkEntry(current_frame)
    username_entry.pack(pady=5, padx=50, fill='x')
    
    # Password
    password_label = ctk.CTkLabel(current_frame, text="Password:")
    password_label.pack(pady=(20, 5))
    password_entry = ctk.CTkEntry(current_frame, show="•")
    password_entry.pack(pady=5, padx=50, fill='x')
    
    # Confirm Password
    confirm_label = ctk.CTkLabel(current_frame, text="Confirm Password:")
    confirm_label.pack(pady=(20, 5))
    confirm_entry = ctk.CTkEntry(current_frame, show="•")
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
    
    register_btn = ctk.CTkButton(current_frame, text="Register", command=register)
    register_btn.pack(pady=20, padx=50, fill='x')
    
    # Back button
    back_btn = ctk.CTkButton(current_frame, text="Back", command=show_start_screen)
    back_btn.pack(pady=10, padx=50, fill='x')

def show_basic_info_screen(username):
    # Display the basic info collection screen
    clear_window()
    
    # Title
    title_label = ctk.CTkLabel(current_frame, text="Basic Information", font=('Helvetica', 20, 'bold'))
    title_label.pack(pady=10)
    
    # Create main content frame
    content_frame = ctk.CTkFrame(current_frame)
    content_frame.pack(fill='both', expand=True, padx=20, pady=5)
    
    # Create form fields
    fields = {
        "age": ctk.CTkEntry(content_frame, width=20),
        "gender": ctk.CTkCombobox(content_frame, values=["Male", "Female", "Other"], width=18),
        "birthdate": ctk.CTkEntry(content_frame, width=20),
        "weight": ctk.CTkEntry(content_frame, width=20),
        "height": ctk.CTkEntry(content_frame, width=20),
        "sleep": ctk.CTkEntry(content_frame, width=20),
        "water": ctk.CTkEntry(content_frame, width=20),
        "activity": ctk.CTkCombobox(content_frame, values=[
            "No exercise",
            "Light Exercise",
            "Moderate Exercise",
            "Active",
            "Very Active",
            "Extremely Active"
        ], width=18)
    }
    
    # Add labels and fields in vertical layout
    for label, field in fields.items():
        label_text = label.replace("_", " ").title() + ":"
        ctk.CTkLabel(content_frame, text=label_text).pack(pady=(5, 0))
        field.pack(pady=(0, 5))
    
    def save_info():
        info = {
            "age": fields["age"].get(),
            "gender": fields["gender"].get(),
            "birthdate": fields["birthdate"].get(),
            "weight": fields["weight"].get(),
            "height": fields["height"].get(),
            "sleep": fields["sleep"].get(),
            "water": fields["water"].get(),
            "activity": fields["activity"].get()
        }
        
        # Validate data
        try:
            if not all(info.values()):
                raise ValueError("Please fill all fields")
            
            # Validate numeric fields
            float(info["age"])
            float(info["weight"])
            float(info["height"])
            float(info["sleep"])
            float(info["water"])
            
            # Validate date format
            datetime.strptime(info["birthdate"], "%Y-%m-%d")
            
            save_user_data(username, "basic_info", info)
            show_main_menu()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    # Button frame
    button_frame = ctk.CTkFrame(current_frame)
    button_frame.pack(fill='x', pady=10, padx=20)
    
    # Save button
    save_btn = ctk.CTkButton(button_frame, text="Save", command=save_info)
    save_btn.pack(fill='x', pady=5)

def show_main_menu():
    # Display the main menu with overview
    clear_window()
    
    # Title
    title_label = ctk.CTkLabel(current_frame, text="Overview", font=('Helvetica', 20, 'bold'))
    title_label.pack(pady=20)
    
    # Get user data
    user_data = get_user_data(current_user, "basic_info")
    nutrition_data = get_user_data(current_user, "nutrition")
    sleep_data = get_user_data(current_user, "sleep")
    workout_data = get_user_data(current_user, "workouts")
    
    # Create overview cards
    cards_frame = ctk.CTkFrame(current_frame)
    cards_frame.pack(fill='both', expand=True, padx=20, pady=10)
    
    # Nutrition Card
    nutrition_frame = ctk.CTkFrame(cards_frame)
    nutrition_frame.pack(fill='x', pady=5)
    ctk.CTkLabel(nutrition_frame, text="Nutrition", font=('Helvetica', 14, 'bold')).pack(pady=5)
    if nutrition_data:
        latest = nutrition_data[-1]
        ctk.CTkLabel(nutrition_frame, text=f"Meal: {latest.get('meal_type', 'N/A')}").pack(pady=2)
        ctk.CTkLabel(nutrition_frame, text=f"Food: {latest.get('food_items', 'N/A')}").pack(pady=2)
        ctk.CTkLabel(nutrition_frame, text=f"Calories: {latest.get('calories', 'N/A')}").pack(pady=2)
        ctk.CTkLabel(nutrition_frame, text=f"Protein: {latest.get('protein', 'N/A')}g").pack(pady=2)
    else:
        ctk.CTkLabel(nutrition_frame, text="No nutrition data").pack(pady=2)
    
    # Sleep Card
    sleep_frame = ctk.CTkFrame(cards_frame)
    sleep_frame.pack(fill='x', pady=5)
    ctk.CTkLabel(sleep_frame, text="Sleep", font=('Helvetica', 14, 'bold')).pack(pady=5)
    if sleep_data:
        latest = sleep_data[-1]
        ctk.CTkLabel(sleep_frame, text=f"Hours: {latest.get('hours', 'N/A')}").pack(pady=2)
    else:
        ctk.CTkLabel(sleep_frame, text="No sleep data").pack(pady=2)
    
    # Workout Card
    workout_frame = ctk.CTkFrame(cards_frame)
    workout_frame.pack(fill='x', pady=5)
    ctk.CTkLabel(workout_frame, text="Latest Workout", font=('Helvetica', 14, 'bold')).pack(pady=5)
    if workout_data:
        latest = workout_data[-1]
        workout_type = latest.get('type', 'N/A')
        ctk.CTkLabel(workout_frame, text=f"Type: {workout_type.title()}").pack(pady=2)
        
        if workout_type == "run":
            ctk.CTkLabel(workout_frame, text=f"Distance: {latest.get('distance', 'N/A')} km").pack(pady=2)
            ctk.CTkLabel(workout_frame, text=f"Pace: {latest.get('pace', 'N/A')}").pack(pady=2)
            ctk.CTkLabel(workout_frame, text=f"Duration: {latest.get('duration', 'N/A')}").pack(pady=2)
        else:  # weight training
            if 'exercises' in latest:
                exercises = latest['exercises']
                if exercises:
                    ctk.CTkLabel(workout_frame, text=f"Exercises: {len(exercises)}").pack(pady=2)
                    # Show first exercise as example
                    first_exercise = exercises[0]
                    exercise_text = f"{first_exercise['name']}: {first_exercise['sets']}x{first_exercise['reps']} @ {first_exercise['weight']}kg"
                    ctk.CTkLabel(workout_frame, text=exercise_text).pack(pady=2)
            ctk.CTkLabel(workout_frame, text=f"Duration: {latest.get('duration', 'N/A')}").pack(pady=2)
    else:
        ctk.CTkLabel(workout_frame, text="No workout data").pack(pady=2)
    
    # Back to Start button
    def logout():
        global current_user
        current_user = None
        show_start_screen()
    
    back_to_start_btn = ctk.CTkButton(current_frame, text="Back to Start", command=logout)
    back_to_start_btn.pack(pady=10)
    
    # Add navigation bar
    show_navigation_bar()

def show_sleep_screen():
    # Display the sleep screen
    clear_window()
    
    # Title
    title_label = ctk.CTkLabel(current_frame, text="Sleep Tracker", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=20)
    
    # Create graph
    fig, ax = plt.subplots(figsize=(6, 3))
    canvas = FigureCanvasTkAgg(fig, master=current_frame)
    canvas.get_tk_widget().pack(pady=10)
    
    # Get sleep data
    sleep_data = get_user_data(current_user, "sleep")
    
    if sleep_data:
        dates = [entry["date"] for entry in sleep_data[-7:]]  # Last 7 days
        hours = [entry["hours"] for entry in sleep_data[-7:]]
        
        ax.bar(dates, hours)
        ax.set_xlabel("Date")
        ax.set_ylabel("Hours")
        ax.set_title("Sleep Hours")
        plt.xticks(rotation=45)
        plt.tight_layout()
    else:
        ax.text(0.5, 0.5, "No sleep data", ha='center', va='center')
    
    # Add data button
    def show_add_sleep():
        show_add_sleep_screen()
    
    add_btn = ctk.CTkButton(current_frame, text="Add Sleep Data", command=show_add_sleep)
    add_btn.pack(pady=5)
    
    # Relax button
    relax_btn = ctk.CTkButton(current_frame, text="Relax", command=show_relax_screen)
    relax_btn.pack(pady=5)
    
    # Add navigation bar
    show_navigation_bar()

def get_ai_response(message, user_data):
    # Generate AI response using OpenRouter API with DeepSeek R1
    try:
        # Prepare user data for context
        basic_info = user_data.get("basic_info", {})
        nutrition_data = user_data.get("nutrition", [])
        workout_data = user_data.get("workouts", [])
        sleep_data = user_data.get("sleep", [])
        
        # Calculate today's calories
        today = datetime.now().strftime("%Y-%m-%d")
        today_calories = sum(entry.get('calories', 0) for entry in nutrition_data 
                           if entry.get('date') == today)
        calorie_goal = basic_info.get("calorie_goal", 2000)
        
        # Create system message with user context
        context = f"""You are a helpful nutrition and fitness assistant. Here is the user's current data:
- Today's calories: {today_calories}/{calorie_goal}
- Latest workout: {workout_data[-1] if workout_data else 'No recent workouts'}
- Latest sleep: {sleep_data[-1] if sleep_data else 'No sleep data recorded'}
- User info: {basic_info}

Provide personalized advice based on this data. Keep responses concise and actionable."""
        
        print("Sending request to OpenRouter...")  # Debug print
        print(f"API key format check: {api_key[:10]}...")  # Debug print first 10 chars
        
        # Make the API request
        completion = client.chat.completions.create(
            model="deepseek/deepseek-r1-0528:free",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": message}
            ]
        )
        
        print("Received response from OpenRouter!")  # Debug print
        return completion.choices[0].message.content
        
    except Exception as e:
        error_message = str(e)
        print(f"Error in AI chat: {error_message}")  # Debug print
        
        if "api_key" in error_message.lower():
            return "I'm having trouble connecting to my knowledge base. Please check your OpenRouter API key in config.py and make sure it starts with 'sk-or-v1-'."
        elif "quota" in error_message.lower():
            return "I'm currently experiencing high traffic. Please try again in a few moments."
        elif "permission" in error_message.lower():
            return "I don't have permission to access my knowledge base. Please check your OpenRouter API key permissions."
        elif "401" in error_message:
            return "I'm unable to authenticate with my knowledge base. Please check your OpenRouter API key in config.py and make sure it's correctly formatted."
        elif "404" in error_message:
            return "I'm having trouble finding the right information. Please try rephrasing your question."
        elif "timeout" in error_message.lower():
            return "I'm taking too long to respond. Please check your internet connection and try again."
        else:
            return "I'm having trouble connecting right now. Please try again in a few moments. If the problem persists, check your internet connection and OpenRouter API key."

def show_ai_chat():
    """Display the AI chat screen"""
    clear_window()
    
    # Title
    title_label = ctk.CTkLabel(current_frame, text="AI Nutrition Chat", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=20)
    
    # Chat history
    chat_frame = ctk.CTkFrame(current_frame)
    chat_frame.pack(fill='both', expand=True, padx=20, pady=10)
    
    chat_history = ctk.CTkTextbox(chat_frame, height=8, wrap="word")
    chat_history.pack(fill='both', expand=True)
    
    # Add welcome message
    chat_history.insert("end", "AI: Hi! I'm your AI nutrition and fitness assistant. How can I help you today?\n")
    
    # Message entry
    message_frame = ctk.CTkFrame(current_frame)
    message_frame.pack(fill='x', padx=20, pady=5)
    
    message_entry = ctk.CTkEntry(message_frame)
    message_entry.pack(side='left', fill='x', expand=True)
    
    def send_message():
        message = message_entry.get()
        if message:
            # Add user message to chat
            chat_history.insert("end", f"You: {message}\n")
            message_entry.delete(0, "end")
            
            # Get user data for context
            user_data = {
                "basic_info": get_user_data(current_user, "basic_info"),
                "nutrition": get_user_data(current_user, "nutrition"),
                "workouts": get_user_data(current_user, "workouts"),
                "sleep": get_user_data(current_user, "sleep")
            }
            
            # Show loading message
            chat_history.insert("end", "AI: Thinking...\n")
            chat_history.see("end")
            
            # Get and display AI response
            try:
                response = get_ai_response(message, user_data)
                
                # Remove loading message and add response
                chat_history.delete("end-2c linestart", "end-1c lineend+1c")
                chat_history.insert("end", f"AI: {response}\n")
            except Exception as e:
                # Remove loading message and add error
                chat_history.delete("end-2c linestart", "end-1c lineend+1c")
                chat_history.insert("end", "AI: I'm having trouble connecting right now. Please try again in a few moments.\n")
            
            # Scroll to bottom
            chat_history.see("end")
    
    # Bind Enter key to send message
    def on_enter(event):
        send_message()
    
    message_entry.bind('<Return>', on_enter)
    
    send_btn = ctk.CTkButton(message_frame, text="Send", command=send_message)
    send_btn.pack(side='right', padx=5)
    
    # Add navigation bar
    show_navigation_bar()

def show_nutrition_screen():
    """Display the nutrition screen"""
    clear_window()
    
    # Title
    title_label = ctk.CTkLabel(current_frame, text="Nutrition", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=30)
    
    # Nutrition data
    nutrition_data = get_user_data(current_user, "nutrition")
    user_data = get_user_data(current_user, "basic_info")
    calorie_goal = user_data.get("calorie_goal", 2000)  # Default to 2000 if not set
    
    # Create main content frame
    content_frame = ctk.CTkFrame(current_frame)
    content_frame.pack(fill='both', expand=True, padx=20, pady=20)
    
    # Calorie progress bar
    progress_frame = ctk.CTkFrame(content_frame)
    progress_frame.pack(fill='x', pady=10)
    
    # Calculate today's total calories
    today = datetime.now().strftime("%Y-%m-%d")
    today_calories = sum(entry.get('calories', 0) for entry in nutrition_data 
                        if entry.get('date') == today)
    
    # Create progress bar
    progress_bar = ctk.CTkProgressBar(progress_frame, orientation="horizontal", width=300)
    progress_bar.pack(pady=10)
    progress_bar.set(min(today_calories / calorie_goal, 1.0))
    
    # Calorie labels
    calorie_label = ctk.CTkLabel(progress_frame, 
                                text=f"Calories: {today_calories}/{calorie_goal}")
    calorie_label.pack(pady=5)
    
    # Left side - Nutrition info
    info_frame = ctk.CTkFrame(content_frame)
    info_frame.pack(side='left', fill='both', expand=True, padx=10)
    ctk.CTkLabel(info_frame, text="Today's Meals", font=('Helvetica', 14, 'bold')).pack(pady=5)

    if nutrition_data:
        # Filter today's meals
        today_meals = [entry for entry in nutrition_data if entry.get('date') == today]
        if today_meals:
            for meal in today_meals:
                meal_frame = ctk.CTkFrame(info_frame)
                meal_frame.pack(fill='x', pady=5)
                
                # Time and meal type
                time_str = datetime.strptime(meal.get('date', '') + ' ' + 
                                           meal.get('time', '00:00'), 
                                           '%Y-%m-%d %H:%M').strftime('%I:%M %p')
                ctk.CTkLabel(meal_frame, 
                           text=f"{time_str} - {meal.get('meal_type', 'N/A')}",
                           font=('Helvetica', 12, 'bold')).pack(anchor='w')
                
                # Food items
                ctk.CTkLabel(meal_frame, 
                           text=f"Food: {meal.get('food_items', 'N/A')}").pack(anchor='w')
                
                # Calories
                ctk.CTkLabel(meal_frame, 
                           text=f"Calories: {meal.get('calories', 'N/A')}").pack(anchor='w')
        else:
            ctk.CTkLabel(info_frame, text="No meals recorded today").pack()
    else:
        ctk.CTkLabel(info_frame, text="No nutrition data").pack()
    
    # Add data button
    def show_add_nutrition():
        show_add_nutrition_screen()
    
    add_btn = ctk.CTkButton(current_frame, text="Add Nutrition Data", command=show_add_nutrition)
    add_btn.pack(pady=20)
    
    # Add navigation bar
    show_navigation_bar()

def show_add_nutrition_screen():
    """Display the add nutrition data screen"""
    clear_window()
    
    # Title
    title_label = ctk.CTkLabel(current_frame, text="Add Nutrition Data", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=30)
    
    # Create form fields
    meal_type = ctk.StringVar(value="breakfast")
    
    # Meal type selection
    meal_frame = ctk.CTkFrame(current_frame)
    meal_frame.pack(fill='x', pady=10, padx=20)
    
    ctk.CTkLabel(meal_frame, text="Meal Type:").pack(pady=5)
    meal_menu = ctk.CTkOptionMenu(meal_frame, values=["Breakfast", "Lunch", "Dinner", "Snack"],
                                variable=meal_type)
    meal_menu.pack(pady=5)
    
    # Food items
    food_frame = ctk.CTkFrame(current_frame)
    food_frame.pack(fill='x', pady=10, padx=20)
    
    ctk.CTkLabel(food_frame, text="Food Items:").pack(pady=5)
    food_entry = ctk.CTkEntry(food_frame, placeholder_text="Enter food items (e.g., Oatmeal, Banana, Coffee)")
    food_entry.pack(pady=5, padx=20, fill='x')
    
    # Nutrition fields
    fields = {
        "calories": ctk.CTkEntry(current_frame),
        "protein": ctk.CTkEntry(current_frame),
        "carbs": ctk.CTkEntry(current_frame),
        "fats": ctk.CTkEntry(current_frame)
    }
    
    # Add labels and fields
    for label, field in fields.items():
        ctk.CTkLabel(current_frame, text=label.title() + ":").pack(pady=(20, 5))
        field.pack(pady=5, padx=50, fill='x')
    
    def save_nutrition():
        try:
            data = {
                "date": datetime.now().strftime("%Y-%m-%d"),
                "time": datetime.now().strftime("%H:%M"),
                "meal_type": meal_type.get(),
                "food_items": food_entry.get(),
                "calories": float(fields["calories"].get()),
                "protein": float(fields["protein"].get()),
                "carbs": float(fields["carbs"].get()),
                "fats": float(fields["fats"].get())
            }
            
            save_user_data(current_user, "nutrition", data)
            show_nutrition_screen()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for nutrition values")
    
    # Save button
    save_btn = ctk.CTkButton(current_frame, text="Save", command=save_nutrition)
    save_btn.pack(pady=20, padx=50, fill='x')
    
    # Back button
    back_btn = ctk.CTkButton(current_frame, text="Back", command=show_nutrition_screen)
    back_btn.pack(pady=10, padx=50, fill='x')

def show_workout_screen():
    """Display the workout screen"""
    clear_window()
    
    # Title
    title_label = ctk.CTkLabel(current_frame, text="Workout", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=30)
    
    # Start workout button
    start_btn = ctk.CTkButton(current_frame, text="Start Workout", command=show_workout_tracking)
    start_btn.pack(pady=20, padx=50, fill='x')
    
    # Previous workouts
    workout_data = get_user_data(current_user, "workouts")
    
    if workout_data:
        # Create a scrollable frame for workout history
        history_frame = ctk.CTkScrollableFrame(current_frame, height=400)
        history_frame.pack(fill='both', expand=True, pady=10, padx=20)
        
        for workout in reversed(workout_data[-5:]):  # Show last 5 workouts
            workout_frame = ctk.CTkFrame(history_frame)
            workout_frame.pack(fill='x', pady=5, padx=5)
            
            # Date header
            date_label = ctk.CTkLabel(workout_frame, 
                                    text=workout.get("date", "No date"),
                                    font=('Helvetica', 14, 'bold'))
            date_label.pack(pady=5)
            
            # Workout details
            details_frame = ctk.CTkFrame(workout_frame)
            details_frame.pack(fill='x', padx=10, pady=5)
            
            ctk.CTkLabel(details_frame, text=f"Type: {workout.get('type', 'N/A')}").pack(anchor='w')
            ctk.CTkLabel(details_frame, text=f"Duration: {workout.get('duration', 'N/A')}").pack(anchor='w')
            
            if "exercises" in workout:
                exercises_frame = ctk.CTkFrame(details_frame)
                exercises_frame.pack(fill='x', pady=5)
                
                for exercise in workout["exercises"]:
                    exercise_text = f"{exercise['name']}: {exercise['sets']}x{exercise['reps']} @ {exercise['weight']}kg"
                    ctk.CTkLabel(exercises_frame, text=exercise_text).pack(anchor='w', pady=2)
    else:
        ctk.CTkLabel(current_frame, text="No workout history").pack()
    
    # Add navigation bar
    show_navigation_bar()

def show_workout_tracking():
    """Display the workout tracking screen"""
    clear_window()
    
    # Title
    title_label = ctk.CTkLabel(current_frame, text="Track Workout", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=30)
    
    # Workout type selection
    type_frame = ctk.CTkFrame(current_frame)
    type_frame.pack(pady=20)
    
    workout_type = ctk.StringVar(value="weight")
    
    # Create frames for different workout types
    weight_frame = ctk.CTkFrame(current_frame)
    run_frame = ctk.CTkFrame(current_frame)
    
    def show_weight_workout():
        weight_frame.pack(fill='both', expand=True, pady=20, padx=20)
        run_frame.pack_forget()
    
    def show_run_workout():
        run_frame.pack(fill='both', expand=True, pady=20, padx=20)
        weight_frame.pack_forget()
    
    def on_type_change(*args):
        if workout_type.get() == "weight":
            show_weight_workout()
        else:
            show_run_workout()
    
    workout_type.trace_add("write", on_type_change)
    
    ctk.CTkRadioButton(type_frame, text="Weight Training", variable=workout_type, value="weight").pack(side='left', padx=10)
    ctk.CTkRadioButton(type_frame, text="Run", variable=workout_type, value="run").pack(side='left', padx=10)
    
    # Weight Training Frame
    exercises_frame = ctk.CTkFrame(weight_frame)
    exercises_frame.pack(fill='both', expand=True)
    ctk.CTkLabel(exercises_frame, text="Exercises", font=('Helvetica', 14, 'bold')).pack(pady=5)
    
    # Create a scrollable frame for exercises
    exercises_container = ctk.CTkScrollableFrame(exercises_frame, height=200)
    exercises_container.pack(fill='both', expand=True, pady=5)
    
    exercises_list = []
    confirmed_exercises = []
    
    def confirm_exercise(exercise_data):
        try:
            # Validate inputs
            if not exercise_data['name'].get():
                messagebox.showerror("Error", "Please enter exercise name")
                return
            if not exercise_data['sets'].get() or not exercise_data['reps'].get() or not exercise_data['weight'].get():
                messagebox.showerror("Error", "Please fill all fields")
                return
            
            # Convert to numbers
            sets = int(exercise_data['sets'].get())
            reps = int(exercise_data['reps'].get())
            weight = float(exercise_data['weight'].get())
            
            # Create confirmed exercise entry
            confirmed_frame = ctk.CTkFrame(exercises_container)
            confirmed_frame.pack(fill='x', pady=5, padx=5)
            
            exercise_info = f"{exercise_data['name'].get()}: {sets}x{reps} @ {weight}kg"
            ctk.CTkLabel(confirmed_frame, text=exercise_info).pack(side='left', padx=5, expand=True)
            
            def remove_confirmed():
                confirmed_frame.destroy()
                confirmed_exercises.remove(exercise_entry)
            
            remove_btn = ctk.CTkButton(confirmed_frame, text="×", width=30, command=remove_confirmed)
            remove_btn.pack(side='right', padx=5)
            
            exercise_entry = {
                'frame': confirmed_frame,
                'name': exercise_data['name'].get(),
                'sets': sets,
                'reps': reps,
                'weight': weight
            }
            confirmed_exercises.append(exercise_entry)
            
            # Remove the input frame
            exercise_data['frame'].destroy()
            exercises_list.remove(exercise_data)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for sets, reps, and weight")
    
    def add_exercise():
        exercise_frame = ctk.CTkFrame(exercises_container)
        exercise_frame.pack(fill='x', pady=5, padx=5)
        
        # Create a horizontal scrollable frame for exercise fields
        fields_container = ctk.CTkScrollableFrame(exercise_frame, orientation="horizontal", height=40)
        fields_container.pack(fill='x', pady=5)
        
        # Exercise fields
        fields_frame = ctk.CTkFrame(fields_container)
        fields_frame.pack(fill='x', pady=5)
        
        # Set minimum width for the fields frame to ensure scrolling
        fields_frame.configure(width=600)
        
        name_entry = ctk.CTkEntry(fields_frame, placeholder_text="Exercise Name", width=200)
        name_entry.pack(side='left', padx=5)
        
        sets_entry = ctk.CTkEntry(fields_frame, placeholder_text="Sets", width=80)
        sets_entry.pack(side='left', padx=5)
        
        reps_entry = ctk.CTkEntry(fields_frame, placeholder_text="Reps", width=80)
        reps_entry.pack(side='left', padx=5)
        
        weight_entry = ctk.CTkEntry(fields_frame, placeholder_text="Weight (kg)", width=100)
        weight_entry.pack(side='left', padx=5)
        
        def remove_exercise():
            exercise_frame.destroy()
            exercises_list.remove(exercise_data)
        
        remove_btn = ctk.CTkButton(fields_frame, text="×", width=30, command=remove_exercise)
        remove_btn.pack(side='left', padx=5)
        
        confirm_btn = ctk.CTkButton(fields_frame, text="✓", width=30, 
                                  command=lambda: confirm_exercise(exercise_data))
        confirm_btn.pack(side='left', padx=5)
        
        exercise_data = {
            'frame': exercise_frame,
            'name': name_entry,
            'sets': sets_entry,
            'reps': reps_entry,
            'weight': weight_entry
        }
        exercises_list.append(exercise_data)
    
    # Add exercise button
    add_exercise_btn = ctk.CTkButton(exercises_frame, text="Add Exercise", command=add_exercise)
    add_exercise_btn.pack(pady=5)
    
    # Run Frame
    run_details_frame = ctk.CTkFrame(run_frame)
    run_details_frame.pack(fill='both', expand=True)
    ctk.CTkLabel(run_details_frame, text="Run Details", font=('Helvetica', 14, 'bold')).pack(pady=5)
    
    # Time inputs
    time_frame = ctk.CTkFrame(run_details_frame)
    time_frame.pack(fill='x', pady=10, padx=20)
    
    # Start time
    start_time_label = ctk.CTkLabel(time_frame, text="Start Time (HH:MM):")
    start_time_label.pack(pady=(10, 5))
    start_time_entry = ctk.CTkEntry(time_frame, width=150)
    start_time_entry.pack(pady=(0, 10))
    
    # End time
    end_time_label = ctk.CTkLabel(time_frame, text="End Time (HH:MM):")
    end_time_label.pack(pady=(10, 5))
    end_time_entry = ctk.CTkEntry(time_frame, width=150)
    end_time_entry.pack(pady=(0, 10))
    
    # Distance input
    distance_frame = ctk.CTkFrame(run_details_frame)
    distance_frame.pack(fill='x', pady=10, padx=20)
    
    distance_label = ctk.CTkLabel(distance_frame, text="Distance (km):")
    distance_label.pack(pady=(10, 5))
    distance_entry = ctk.CTkEntry(distance_frame, width=150)
    distance_entry.pack(pady=(0, 10))
    
    # Stopwatch
    stopwatch_frame = ctk.CTkFrame(current_frame)
    stopwatch_frame.pack(pady=20)
    ctk.CTkLabel(stopwatch_frame, text="Stopwatch", font=('Helvetica', 14, 'bold')).pack(pady=5)
    
    time_label = ctk.CTkLabel(stopwatch_frame, text="00:00:00", font=('Helvetica', 20))
    time_label.pack(pady=5)
    
    running = False
    start_time = None
    elapsed_time = 0
    
    def update_stopwatch():
        nonlocal running, start_time, elapsed_time
        if running:
            current_elapsed = elapsed_time + (datetime.now() - start_time).total_seconds()
            hours = int(current_elapsed // 3600)
            minutes = int((current_elapsed % 3600) // 60)
            seconds = int(current_elapsed % 60)
            time_label.configure(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            root.after(1000, update_stopwatch)
    
    def toggle_stopwatch():
        nonlocal running, start_time, elapsed_time
        if not running:
            running = True
            start_time = datetime.now()
            update_stopwatch()
        else:
            running = False
            elapsed_time += (datetime.now() - start_time).total_seconds()
    
    def reset_stopwatch():
        nonlocal running, start_time, elapsed_time
        running = False
        start_time = None
        elapsed_time = 0
        time_label.configure(text="00:00:00")
    
    # Stopwatch controls
    controls_frame = ctk.CTkFrame(stopwatch_frame)
    controls_frame.pack(pady=5)
    
    start_stop_btn = ctk.CTkButton(controls_frame, text="Start/Stop", command=toggle_stopwatch)
    start_stop_btn.pack(side='left', padx=5)
    
    reset_btn = ctk.CTkButton(controls_frame, text="Reset", command=reset_stopwatch)
    reset_btn.pack(side='left', padx=5)
    
    # Save workout
    def save_workout():
        if workout_type.get() == "weight":
            if not confirmed_exercises:
                messagebox.showerror("Error", "Please add and confirm at least one exercise")
                return
            
            data = {
                "date": datetime.now().strftime("%Y-%m-%d"),
                "type": "weight",
                "duration": time_label.cget("text"),
                "exercises": [{
                    "name": exercise['name'],
                    "sets": exercise['sets'],
                    "reps": exercise['reps'],
                    "weight": exercise['weight']
                } for exercise in confirmed_exercises]
            }
        else:  # Run workout
            try:
                if not start_time_entry.get() or not end_time_entry.get() or not distance_entry.get():
                    messagebox.showerror("Error", "Please fill all run details")
                    return
                
                # Parse times
                start_time = datetime.strptime(start_time_entry.get(), "%H:%M")
                end_time = datetime.strptime(end_time_entry.get(), "%H:%M")
                distance = float(distance_entry.get())
                
                # Calculate duration
                duration = end_time - start_time
                if duration.total_seconds() < 0:
                    duration = datetime.combine(datetime.today(), end_time.time()) - datetime.combine(datetime.today(), start_time.time())
                
                data = {
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "type": "run",
                    "start_time": start_time_entry.get(),
                    "end_time": end_time_entry.get(),
                    "duration": str(duration).split('.')[0],
                    "distance": distance,
                    "pace": f"{duration.total_seconds() / 60 / distance:.2f} min/km"
                }
            except ValueError:
                messagebox.showerror("Error", "Please enter valid times (HH:MM) and distance")
                return
        
        save_user_data(current_user, "workouts", data)
        show_workout_screen()
    
    # Button frame
    button_frame = ctk.CTkFrame(current_frame)
    button_frame.pack(fill='x', pady=20, padx=20)
    
    save_btn = ctk.CTkButton(button_frame, text="Save Workout", command=save_workout)
    save_btn.pack(side='left', expand=True, padx=5)
    
    back_btn = ctk.CTkButton(button_frame, text="Back", command=show_workout_screen)
    back_btn.pack(side='left', expand=True, padx=5)
    
    # Show initial workout type
    show_weight_workout()

def show_add_sleep_screen():
    """Display the add sleep data screen"""
    clear_window()
    
    # Title
    title_label = ctk.CTkLabel(current_frame, text="Add Sleep Data", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=30)
    
    # Date entry
    ctk.CTkLabel(current_frame, text="Date (YYYY-MM-DD):").pack(pady=(20, 5))
    date_entry = ctk.CTkEntry(current_frame)
    date_entry.pack(pady=5, padx=50, fill='x')
    
    # Hours entry
    ctk.CTkLabel(current_frame, text="Hours:").pack(pady=(20, 5))
    hours_entry = ctk.CTkEntry(current_frame)
    hours_entry.pack(pady=5, padx=50, fill='x')
    
    def save_sleep():
        try:
            date = datetime.strptime(date_entry.get(), "%Y-%m-%d").strftime("%Y-%m-%d")
            hours = float(hours_entry.get())
            
            data = {
                "date": date,
                "hours": hours
            }
            
            save_user_data(current_user, "sleep", data)
            show_sleep_screen()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid date and hours")
    
    # Save button
    save_btn = ctk.CTkButton(current_frame, text="Save", command=save_sleep)
    save_btn.pack(pady=20, padx=50, fill='x')
    
    # Back button
    back_btn = ctk.CTkButton(current_frame, text="Back", command=show_sleep_screen)
    back_btn.pack(pady=10, padx=50, fill='x')

def show_settings():
    """Display the settings screen"""
    clear_window()
    
    # Title
    title_label = ctk.CTkLabel(current_frame, text="Settings", font=('Helvetica', 20, 'bold'))
    title_label.pack(pady=10)
    
    # Create scrollable frame for settings
    settings_frame = ctk.CTkScrollableFrame(current_frame)
    settings_frame.pack(fill='both', expand=True, padx=20, pady=10)
    
    # Basic Info Section
    basic_info_frame = ctk.CTkFrame(settings_frame)
    basic_info_frame.pack(fill='x', pady=10)
    ctk.CTkLabel(basic_info_frame, text="Basic Information", font=('Helvetica', 16, 'bold')).pack(pady=5)
    
    # Get current user data
    user_data = get_user_data(current_user, "basic_info")
    if not user_data:
        user_data = {}
    
    # Create form fields
    fields = {
        "age": ctk.CTkEntry(basic_info_frame, width=200),
        "gender": ctk.CTkComboBox(basic_info_frame, values=["Male", "Female", "Other"], width=200),
        "birthdate": ctk.CTkEntry(basic_info_frame, width=200),
        "weight": ctk.CTkEntry(basic_info_frame, width=200),
        "height": ctk.CTkEntry(basic_info_frame, width=200),
        "sleep": ctk.CTkEntry(basic_info_frame, width=200),
        "water": ctk.CTkEntry(basic_info_frame, width=200),
        "activity": ctk.CTkComboBox(basic_info_frame, values=[
            "No exercise",
            "Light Exercise",
            "Moderate Exercise",
            "Active",
            "Very Active",
            "Extremely Active"
        ], width=200)
    }
    
    # Add labels and fields
    for label, field in fields.items():
        label_text = label.replace("_", " ").title() + ":"
        ctk.CTkLabel(basic_info_frame, text=label_text).pack(pady=(5, 0))
        field.pack(pady=(0, 5))
        # Set current values if they exist
        if label in user_data:
            if isinstance(field, ctk.CTkComboBox):
                field.set(user_data[label])
            else:
                field.insert(0, str(user_data[label]))
    
    def save_basic_info():
        try:
            # Validate numeric fields
            float(fields["age"].get())
            float(fields["weight"].get())
            float(fields["height"].get())
            float(fields["sleep"].get())
            float(fields["water"].get())
            
            # Validate date format
            datetime.strptime(fields["birthdate"].get(), "%Y-%m-%d")
            
            # Save data
            info = {
                "age": fields["age"].get(),
                "gender": fields["gender"].get(),
                "birthdate": fields["birthdate"].get(),
                "weight": fields["weight"].get(),
                "height": fields["height"].get(),
                "sleep": fields["sleep"].get(),
                "water": fields["water"].get(),
                "activity": fields["activity"].get()
            }
            
            save_user_data(current_user, "basic_info", info)
            messagebox.showinfo("Success", "Basic information updated successfully!")
        except ValueError as e:
            messagebox.showerror("Error", "Please enter valid numbers and date (YYYY-MM-DD)")
    
    # Save button for basic info
    save_basic_btn = ctk.CTkButton(basic_info_frame, text="Save Basic Info", command=save_basic_info)
    save_basic_btn.pack(pady=10)
    
    # Appearance Settings Section
    appearance_frame = ctk.CTkFrame(settings_frame)
    appearance_frame.pack(fill='x', pady=10)
    ctk.CTkLabel(appearance_frame, text="Appearance", font=('Helvetica', 16, 'bold')).pack(pady=5)
    
    # Theme selection
    theme_label = ctk.CTkLabel(appearance_frame, text="Appearance Mode:")
    theme_label.pack(pady=(10, 5))
    
    def change_appearance_mode(new_mode):
        ctk.set_appearance_mode(new_mode)
    
    theme_menu = ctk.CTkOptionMenu(appearance_frame, values=["System", "Dark", "Light"],
                                 command=change_appearance_mode)
    theme_menu.pack(pady=5)
    theme_menu.set(ctk.get_appearance_mode())
    
    # Color theme selection
    color_label = ctk.CTkLabel(appearance_frame, text="Color Theme:")
    color_label.pack(pady=(10, 5))
    
    def change_color_theme(new_theme):
        ctk.set_default_color_theme(new_theme)
    
    color_menu = ctk.CTkOptionMenu(appearance_frame, values=["blue", "green", "dark-blue"],
                                 command=change_color_theme)
    color_menu.pack(pady=5)
    color_menu.set("blue")
    
    # Calorie goal setting
    calorie_frame = ctk.CTkFrame(settings_frame)
    calorie_frame.pack(fill='x', pady=10)
    ctk.CTkLabel(calorie_frame, text="Nutrition Goals", font=('Helvetica', 16, 'bold')).pack(pady=5)
    
    ctk.CTkLabel(calorie_frame, text="Daily Calorie Goal:").pack(pady=5)
    calorie_entry = ctk.CTkEntry(calorie_frame)
    calorie_entry.pack(pady=5)
    
    # Load current calorie goal
    if user_data and "calorie_goal" in user_data:
        calorie_entry.insert(0, str(user_data["calorie_goal"]))
    else:
        calorie_entry.insert(0, "2000")  # Default value
    
    def save_calorie_goal():
        nonlocal user_data
        try:
            goal = int(calorie_entry.get())
            if goal <= 0:
                raise ValueError("Calorie goal must be positive")
            
            # Update user data
            if not user_data:
                user_data = {}
            user_data["calorie_goal"] = goal
            save_user_data(current_user, "basic_info", user_data)
            
            messagebox.showinfo("Success", "Calorie goal updated successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid calorie goal")
    
    save_goal_btn = ctk.CTkButton(calorie_frame, text="Save Goal", command=save_calorie_goal)
    save_goal_btn.pack(pady=5)
    
    # Back button
    back_btn = ctk.CTkButton(settings_frame, text="Back", command=show_main_menu)
    back_btn.pack(pady=10)

def show_settings_button():
    """Show the settings button in the top right"""
    settings_btn = ctk.CTkButton(current_frame, text="⚙️", command=show_settings, width=2)
    settings_btn.pack(side='top', anchor='e', padx=5, pady=2)

def show_navigation_bar():
    """Show the navigation bar at the bottom of the screen"""
    nav_frame = ctk.CTkFrame(current_frame)
    nav_frame.pack(side='bottom', fill='x', pady=2)
    
    # Create a frame for the navigation buttons
    buttons_frame = ctk.CTkFrame(nav_frame)
    buttons_frame.pack(fill='x', padx=2)
    
    # Navigation buttons with icons (using text as placeholders)
    buttons = [
        ("🏠", show_main_menu),
        ("💪", show_workout_screen),
        ("🍎", show_nutrition_screen),
        ("😴", show_sleep_screen),
        ("💬", show_ai_chat)
    ]
    
    for icon, command in buttons:
        btn = ctk.CTkButton(buttons_frame, text=icon, command=command, width=2)
        btn.pack(side='left', expand=True, padx=1)

def play_sound(file_path):
    """Play a sound file using platform-specific methods"""
    try:
        if platform.system() == "Darwin":  # macOS
            subprocess.run(["afplay", file_path])
        elif platform.system() == "Windows":
            import winsound
            winsound.PlaySound(file_path, winsound.SND_FILENAME)
        else:  # Linux
            subprocess.run(["aplay", file_path])
    except Exception as e:
        print(f"Error playing sound: {e}")

def show_relax_screen():
    """Display the relaxation screen with guided breathing exercise"""
    clear_window()
    
    # Title
    title_label = ctk.CTkLabel(current_frame, text="Guided Breathing", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=20)
    
    # Create a frame for the breathing box
    breathing_frame = ctk.CTkFrame(current_frame)
    breathing_frame.pack(pady=20, padx=20, fill='both', expand=True)
    
    # Create the breathing box with highlighted borders
    box_size = 200
    breathing_box = ctk.CTkFrame(breathing_frame, width=box_size, height=box_size)
    breathing_box.pack(pady=20)
    
    # Create border frames
    border_width = 5
    left_border = ctk.CTkFrame(breathing_box, width=border_width, height=box_size, fg_color="gray")
    left_border.place(x=0, y=0)
    
    top_border = ctk.CTkFrame(breathing_box, width=box_size, height=border_width, fg_color="gray")
    top_border.place(x=0, y=0)
    
    right_border = ctk.CTkFrame(breathing_box, width=border_width, height=box_size, fg_color="gray")
    right_border.place(x=box_size-border_width, y=0)
    
    bottom_border = ctk.CTkFrame(breathing_box, width=box_size, height=border_width, fg_color="gray")
    bottom_border.place(x=0, y=box_size-border_width)
    
    # Animation variables
    breathing_active = False
    borders = [left_border, top_border, right_border, bottom_border]
    phases = ["Breathe In", "Hold", "Breathe Out", "Hold"]
    current_phase = 0
    animation_speed = 4000  # 4 seconds per phase
    countdown = 4  # Countdown for each phase
    
    # Breathing text
    breathing_text = ctk.CTkLabel(breathing_frame, text="Press Start to Begin", font=('Helvetica', 16))
    breathing_text.pack(pady=10)
    
    # Countdown text
    countdown_text = ctk.CTkLabel(breathing_frame, text="", font=('Helvetica', 24, 'bold'))
    countdown_text.pack(pady=5)
    
    # Breathing instructions
    instructions = ctk.CTkLabel(breathing_frame, 
                              text="Follow the highlighted border and voice guidance.\nComplete one full cycle of breathing.",
                              font=('Helvetica', 12))
    instructions.pack(pady=10)
    
    def highlight_border(border, color="blue"):
        """Highlight a border with the specified color"""
        try:
            if border.winfo_exists():
                border.configure(fg_color=color)
        except:
            pass
    
    def reset_borders():
        """Reset all borders to gray"""
        for border in borders:
            try:
                if border.winfo_exists():
                    border.configure(fg_color="gray")
            except:
                pass
    
    def play_phase_audio(phase):
        """Play audio for the current phase"""
        audio_file = f"assets/breathing_{phase.lower().replace(' ', '_')}.wav"
        if os.path.exists(audio_file):
            play_sound(audio_file)
    
    def update_countdown():
        """Update the countdown display"""
        nonlocal countdown
        try:
            if countdown > 0 and countdown_text.winfo_exists():
                countdown_text.configure(text=str(countdown))
                countdown -= 1
                root.after(1000, update_countdown)
            elif countdown_text.winfo_exists():
                countdown_text.configure(text="")
        except:
            pass
    
    def breathing_cycle():
        """Run one complete breathing cycle"""
        nonlocal current_phase, breathing_active, countdown
        try:
            if not breathing_active or not breathing_text.winfo_exists():
                return
            
            # Reset all borders
            reset_borders()
            
            # Highlight current border and update text
            highlight_border(borders[current_phase])
            breathing_text.configure(text=phases[current_phase])
            
            # Play audio for current phase
            play_phase_audio(phases[current_phase])
            
            # Start countdown
            countdown = 4
            update_countdown()
            
            # Move to next phase
            current_phase = (current_phase + 1) % 4
            
            # Schedule next phase
            if breathing_active and breathing_text.winfo_exists():
                root.after(animation_speed, breathing_cycle)
        except:
            pass
    
    def start_breathing():
        """Start the breathing exercise"""
        nonlocal breathing_active
        try:
            breathing_active = True
            start_stop_btn.configure(text="Stop")
            # Wait 4 seconds before starting
            breathing_text.configure(text="Starting in 4...")
            countdown = 4
            update_countdown()
            root.after(4000, breathing_cycle)
        except:
            pass
    
    def stop_breathing():
        """Stop the breathing exercise"""
        nonlocal breathing_active
        try:
            breathing_active = False
            start_stop_btn.configure(text="Start")
            reset_borders()
            if breathing_text.winfo_exists():
                breathing_text.configure(text="Press Start to Begin")
            if countdown_text.winfo_exists():
                countdown_text.configure(text="")
        except:
            pass
    
    def toggle_breathing():
        """Toggle the breathing exercise"""
        if breathing_active:
            stop_breathing()
        else:
            start_breathing()
    
    # Control buttons
    controls_frame = ctk.CTkFrame(breathing_frame)
    controls_frame.pack(pady=20)
    
    start_stop_btn = ctk.CTkButton(controls_frame, text="Start", command=toggle_breathing)
    start_stop_btn.pack(side='left', padx=5)
    
    # Back button
    back_btn = ctk.CTkButton(current_frame, text="Back", command=show_sleep_screen)
    back_btn.pack(pady=20, padx=50, fill='x')
    
    # Add navigation bar
    show_navigation_bar()

def main():
    global root
    root = ctk.CTk()
    root.title("MacroMeter")
    root.geometry("400x800")
    root.resizable(False, False)
    
    # Configure the main window to use all available space
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    # Start with the start screen
    show_start_screen()
    
    root.mainloop()

if __name__ == "__main__":
    main()