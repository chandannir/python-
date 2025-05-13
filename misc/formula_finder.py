import tkinter as tk
from tkinter import ttk
import json
import os
from datetime import datetime
import shutil
import subprocess
import math
import random
import webbrowser
import urllib.parse

class FormulaDatabase:
    def __init__(self):
        self.formulas = {
            "Quadratic Equations": {
                "Standard Form": {
                    "formula": "ax² + bx + c = 0",
                    "description": "The standard form of a quadratic equation where a, b, and c are constants and a ≠ 0.",
                    "example": "2x² - 5x + 3 = 0",
                    "usage": "Used to represent any quadratic equation in its standard form.",
                    "practice_problems": [
                        {
                            "question": "Convert the equation 3x² + 2x - 5 = 0 to standard form.",
                            "answer": "3x² + 2x - 5 = 0",
                            "hint": "The equation is already in standard form."
                        },
                        {
                            "question": "Convert 2(x + 3)² - 4 = 0 to standard form.",
                            "answer": "2x² + 12x + 14 = 0",
                            "hint": "Expand (x + 3)² and multiply by 2, then subtract 4."
                        },
                        {
                            "question": "Convert (x - 2)(x + 5) = 0 to standard form.",
                            "answer": "x² + 3x - 10 = 0",
                            "hint": "Use FOIL method to expand the product."
                        }
                    ]
                },
                "Quadratic Formula": {
                    "formula": "x = (-b ± √(b² - 4ac)) / 2a",
                    "description": "The formula used to solve any quadratic equation.",
                    "example": "For x² - 5x + 6 = 0, x = (5 ± √(25 - 24)) / 2 = 2 or 3",
                    "usage": "Used to find the roots of a quadratic equation.",
                    "practice_problems": [
                        {
                            "question": "Solve the equation x² - 5x + 6 = 0 using the quadratic formula.",
                            "answer": "x = 2 or x = 3",
                            "hint": "Identify a=1, b=-5, c=6 and substitute into the formula."
                        },
                        {
                            "question": "Solve 2x² + 5x - 3 = 0 using the quadratic formula.",
                            "answer": "x = 0.5 or x = -3",
                            "hint": "Identify a=2, b=5, c=-3 and substitute into the formula."
                        },
                        {
                            "question": "Solve x² + 4x + 4 = 0 using the quadratic formula.",
                            "answer": "x = -2",
                            "hint": "This is a perfect square trinomial."
                        }
                    ]
                },
                "Vertex Form": {
                    "formula": "y = a(x - h)² + k",
                    "description": "The vertex form of a quadratic equation where (h,k) is the vertex.",
                    "example": "y = 2(x - 3)² + 4",
                    "usage": "Used to easily identify the vertex and graph the parabola.",
                    "practice_problems": [
                        {
                            "question": "Convert y = x² - 6x + 8 to vertex form.",
                            "answer": "y = (x - 3)² - 1",
                            "hint": "Complete the square for the x terms."
                        },
                        {
                            "question": "Convert y = 2x² + 8x + 5 to vertex form.",
                            "answer": "y = 2(x + 2)² - 3",
                            "hint": "Factor out 2 first, then complete the square."
                        },
                        {
                            "question": "Find the vertex of y = -3(x + 1)² + 4.",
                            "answer": "(-1, 4)",
                            "hint": "In vertex form y = a(x - h)² + k, the vertex is (h,k)."
                        }
                    ]
                }
            },
            "Trigonometry": {
                "Basic Ratios": {
                    "formula": "sin(θ) = opposite/hypotenuse\ncos(θ) = adjacent/hypotenuse\ntan(θ) = opposite/adjacent",
                    "description": "The three basic trigonometric ratios for a right triangle.",
                    "example": "In a 3-4-5 triangle, sin(θ) = 3/5, cos(θ) = 4/5, tan(θ) = 3/4",
                    "usage": "Used to find missing sides or angles in right triangles.",
                    "practice_problems": [
                        {
                            "question": "In a right triangle, if the opposite side is 3 and the hypotenuse is 5, find sin(θ).",
                            "answer": "0.6",
                            "hint": "Use the sine ratio: opposite/hypotenuse."
                        },
                        {
                            "question": "In a right triangle, if the adjacent side is 4 and the hypotenuse is 5, find cos(θ).",
                            "answer": "0.8",
                            "hint": "Use the cosine ratio: adjacent/hypotenuse."
                        },
                        {
                            "question": "In a right triangle, if the opposite side is 3 and the adjacent side is 4, find tan(θ).",
                            "answer": "0.75",
                            "hint": "Use the tangent ratio: opposite/adjacent."
                        }
                    ]
                },
                "Pythagorean Identity": {
                    "formula": "sin²(θ) + cos²(θ) = 1",
                    "description": "A fundamental trigonometric identity.",
                    "example": "If sin(θ) = 0.6, then cos(θ) = ±0.8",
                    "usage": "Used to find one trigonometric ratio when another is known.",
                    "practice_problems": [
                        {
                            "question": "If sin(θ) = 0.6, find cos(θ).",
                            "answer": "±0.8",
                            "hint": "Use the Pythagorean identity: sin²(θ) + cos²(θ) = 1."
                        },
                        {
                            "question": "If cos(θ) = 0.8, find sin(θ).",
                            "answer": "±0.6",
                            "hint": "Use the Pythagorean identity: sin²(θ) + cos²(θ) = 1."
                        },
                        {
                            "question": "If sin(θ) = 0.5, find cos(θ).",
                            "answer": "±0.866",
                            "hint": "Use the Pythagorean identity and take the square root."
                        }
                    ]
                },
                "Law of Sines": {
                    "formula": "a/sin(A) = b/sin(B) = c/sin(C)",
                    "description": "Relates the sides of a triangle to the sines of its angles.",
                    "example": "In a triangle with sides a=5, b=7, and angle A=30°, find angle B.",
                    "usage": "Used to solve triangles when given two angles and a side, or two sides and a non-included angle.",
                    "practice_problems": [
                        {
                            "question": "In a triangle, if a=5, b=7, and angle A=30°, find angle B.",
                            "answer": "44.4°",
                            "hint": "Use the Law of Sines: a/sin(A) = b/sin(B)."
                        },
                        {
                            "question": "In a triangle, if a=6, angle A=45°, and angle B=60°, find side b.",
                            "answer": "7.35",
                            "hint": "Use the Law of Sines: a/sin(A) = b/sin(B)."
                        },
                        {
                            "question": "In a triangle, if b=8, angle B=40°, and angle C=70°, find side c.",
                            "answer": "11.52",
                            "hint": "First find angle A, then use the Law of Sines."
                        }
                    ]
                }
            },
            "Calculus": {
                "Power Rule": {
                    "formula": "d/dx(x^n) = nx^(n-1)",
                    "description": "The derivative of a power function.",
                    "example": "d/dx(x³) = 3x²",
                    "usage": "Used to find the derivative of polynomial functions.",
                    "practice_problems": [
                        {
                            "question": "Find the derivative of f(x) = x⁴.",
                            "answer": "4x³",
                            "hint": "Apply the power rule: d/dx(x^n) = nx^(n-1)."
                        },
                        {
                            "question": "Find the derivative of f(x) = x² + 3x + 2.",
                            "answer": "2x + 3",
                            "hint": "Apply the power rule to each term separately."
                        },
                        {
                            "question": "Find the derivative of f(x) = 5x³ - 2x² + 7x - 1.",
                            "answer": "15x² - 4x + 7",
                            "hint": "Apply the power rule to each term and remember the constant rule."
                        }
                    ]
                },
                "Chain Rule": {
                    "formula": "d/dx[f(g(x))] = f'(g(x)) * g'(x)",
                    "description": "The derivative of a composite function.",
                    "example": "d/dx[(x² + 1)³] = 3(x² + 1)² * 2x",
                    "usage": "Used to find the derivative of composite functions.",
                    "practice_problems": [
                        {
                            "question": "Find the derivative of f(x) = (x² + 1)³.",
                            "answer": "6x(x² + 1)²",
                            "hint": "Apply the chain rule: d/dx[f(g(x))] = f'(g(x)) * g'(x)."
                        },
                        {
                            "question": "Find the derivative of f(x) = sin(x²).",
                            "answer": "2x cos(x²)",
                            "hint": "The derivative of sin(u) is cos(u) * u'."
                        },
                        {
                            "question": "Find the derivative of f(x) = √(3x + 1).",
                            "answer": "3/(2√(3x + 1))",
                            "hint": "The derivative of √u is u'/(2√u)."
                        }
                    ]
                },
                "Integration by Parts": {
                    "formula": "∫u dv = uv - ∫v du",
                    "description": "A method for integrating the product of two functions.",
                    "example": "∫x * e^x dx = x * e^x - ∫e^x dx",
                    "usage": "Used to integrate products of functions.",
                    "practice_problems": [
                        {
                            "question": "Evaluate ∫x * e^x dx.",
                            "answer": "x * e^x - e^x + C",
                            "hint": "Use integration by parts with u = x and dv = e^x dx."
                        },
                        {
                            "question": "Evaluate ∫x * sin(x) dx.",
                            "answer": "-x * cos(x) + sin(x) + C",
                            "hint": "Use integration by parts with u = x and dv = sin(x) dx."
                        },
                        {
                            "question": "Evaluate ∫x * ln(x) dx.",
                            "answer": "(x²/2) * ln(x) - x²/4 + C",
                            "hint": "Use integration by parts with u = ln(x) and dv = x dx."
                        }
                    ]
                }
            },
            "Geometry": {
                "Circle Area": {
                    "formula": "A = πr²",
                    "description": "The area of a circle with radius r.",
                    "example": "For a circle with radius 5, A = π * 25 ≈ 78.54",
                    "usage": "Used to find the area of a circle.",
                    "practice_problems": [
                        {
                            "question": "Find the area of a circle with radius 7.",
                            "answer": "49π",
                            "hint": "Use the formula A = πr²."
                        },
                        {
                            "question": "Find the area of a circle with diameter 10.",
                            "answer": "25π",
                            "hint": "First find the radius (diameter/2), then use A = πr²."
                        },
                        {
                            "question": "If a circle has area 36π, find its radius.",
                            "answer": "6",
                            "hint": "Use the formula A = πr² and solve for r."
                        }
                    ]
                },
                "Pythagorean Theorem": {
                    "formula": "a² + b² = c²",
                    "description": "Relates the sides of a right triangle.",
                    "example": "In a 3-4-5 triangle, 3² + 4² = 5²",
                    "usage": "Used to find the length of the hypotenuse or a leg of a right triangle.",
                    "practice_problems": [
                        {
                            "question": "In a right triangle, if a=3 and b=4, find c.",
                            "answer": "5",
                            "hint": "Use the Pythagorean theorem: a² + b² = c²."
                        },
                        {
                            "question": "In a right triangle, if a=6 and c=10, find b.",
                            "answer": "8",
                            "hint": "Use the Pythagorean theorem and solve for b."
                        },
                        {
                            "question": "In a right triangle, if b=12 and c=13, find a.",
                            "answer": "5",
                            "hint": "Use the Pythagorean theorem and solve for a."
                        }
                    ]
                },
                "Volume of a Sphere": {
                    "formula": "V = (4/3)πr³",
                    "description": "The volume of a sphere with radius r.",
                    "example": "For a sphere with radius 3, V = (4/3)π * 27 ≈ 113.1",
                    "usage": "Used to find the volume of a sphere.",
                    "practice_problems": [
                        {
                            "question": "Find the volume of a sphere with radius 4.",
                            "answer": "(256/3)π",
                            "hint": "Use the formula V = (4/3)πr³."
                        },
                        {
                            "question": "Find the volume of a sphere with diameter 6.",
                            "answer": "36π",
                            "hint": "First find the radius (diameter/2), then use V = (4/3)πr³."
                        },
                        {
                            "question": "If a sphere has volume (500/3)π, find its radius.",
                            "answer": "5",
                            "hint": "Use the formula V = (4/3)πr³ and solve for r."
                        }
                    ]
                }
            },
            "Functions": {
                "Linear Functions": {
                    "formula": "f(x) = mx + b",
                    "description": "A linear function where m is the slope and b is the y-intercept.",
                    "example": "f(x) = 2x + 3",
                    "usage": "Used to represent relationships with constant rate of change.",
                    "practice_problems": [
                        {
                            "question": "Find the slope and y-intercept of f(x) = 3x - 2.",
                            "answer": "slope = 3, y-intercept = -2",
                            "hint": "Compare with the form f(x) = mx + b."
                        },
                        {
                            "question": "Write the equation of a line with slope 4 passing through point (2,5).",
                            "answer": "f(x) = 4x - 3",
                            "hint": "Use point-slope form: y - y₁ = m(x - x₁)."
                        },
                        {
                            "question": "Find the x-intercept of f(x) = 2x + 6.",
                            "answer": "x = -3",
                            "hint": "Set f(x) = 0 and solve for x."
                        }
                    ]
                },
                "Quadratic Functions": {
                    "formula": "f(x) = ax² + bx + c",
                    "description": "A quadratic function where a, b, and c are constants and a ≠ 0.",
                    "example": "f(x) = x² - 4x + 3",
                    "usage": "Used to model parabolic relationships.",
                    "practice_problems": [
                        {
                            "question": "Find the vertex of f(x) = x² - 6x + 8.",
                            "answer": "(3, -1)",
                            "hint": "Use x = -b/(2a) to find x-coordinate, then substitute to find y."
                        },
                        {
                            "question": "Determine if f(x) = -2x² + 4x - 1 opens up or down.",
                            "answer": "opens down",
                            "hint": "Look at the sign of the coefficient of x²."
                        },
                        {
                            "question": "Find the axis of symmetry of f(x) = 3x² + 6x + 2.",
                            "answer": "x = -1",
                            "hint": "Use x = -b/(2a)."
                        }
                    ]
                },
                "Exponential Functions": {
                    "formula": "f(x) = a * b^x",
                    "description": "An exponential function where a is the initial value and b is the growth/decay factor.",
                    "example": "f(x) = 2 * 3^x",
                    "usage": "Used to model exponential growth or decay.",
                    "practice_problems": [
                        {
                            "question": "Find f(2) for f(x) = 3 * 2^x.",
                            "answer": "12",
                            "hint": "Substitute x = 2 into the function."
                        },
                        {
                            "question": "Determine if f(x) = 4 * (0.5)^x represents growth or decay.",
                            "answer": "decay",
                            "hint": "Look at the base: if 0 < b < 1, it's decay."
                        },
                        {
                            "question": "Find the initial value of f(x) = 5 * 2^x.",
                            "answer": "5",
                            "hint": "The initial value is the coefficient a."
                        }
                    ]
                }
            },
            "Algebra": {
                "Factoring": {
                    "formula": "ax² + bx + c = (px + q)(rx + s)",
                    "description": "Breaking down a polynomial into a product of simpler polynomials.",
                    "example": "x² + 5x + 6 = (x + 2)(x + 3)",
                    "usage": "Used to solve equations and simplify expressions.",
                    "practice_problems": [
                        {
                            "question": "Factor x² + 7x + 12.",
                            "answer": "(x + 3)(x + 4)",
                            "hint": "Find two numbers that multiply to 12 and add to 7."
                        },
                        {
                            "question": "Factor 2x² - 5x - 3.",
                            "answer": "(2x + 1)(x - 3)",
                            "hint": "Use the AC method: multiply a and c, then find factors."
                        },
                        {
                            "question": "Factor x² - 9.",
                            "answer": "(x + 3)(x - 3)",
                            "hint": "This is a difference of squares: a² - b² = (a + b)(a - b)."
                        }
                    ]
                },
                "Solving Equations": {
                    "formula": "ax + b = c → x = (c - b)/a",
                    "description": "Finding the value of the variable that makes the equation true.",
                    "example": "2x + 3 = 7 → x = 2",
                    "usage": "Used to find unknown values in mathematical relationships.",
                    "practice_problems": [
                        {
                            "question": "Solve for x: 3x + 4 = 13.",
                            "answer": "x = 3",
                            "hint": "Isolate x by subtracting 4 and dividing by 3."
                        },
                        {
                            "question": "Solve for x: 2(x - 3) = 4x + 2.",
                            "answer": "x = -4",
                            "hint": "First distribute, then collect like terms."
                        },
                        {
                            "question": "Solve for x: (x + 2)/3 = 4.",
                            "answer": "x = 10",
                            "hint": "Multiply both sides by 3, then subtract 2."
                        }
                    ]
                },
                "Systems of Equations": {
                    "formula": "ax + by = c\ndx + ey = f",
                    "description": "A set of equations with multiple variables.",
                    "example": "2x + y = 5\n3x - y = 1",
                    "usage": "Used to find values that satisfy multiple equations simultaneously.",
                    "practice_problems": [
                        {
                            "question": "Solve the system: 2x + y = 5, 3x - y = 1.",
                            "answer": "x = 1.2, y = 2.6",
                            "hint": "Add the equations to eliminate y."
                        },
                        {
                            "question": "Solve the system: x + 2y = 4, 2x - y = 3.",
                            "answer": "x = 2, y = 1",
                            "hint": "Use substitution or elimination method."
                        },
                        {
                            "question": "Solve the system: 3x + 2y = 8, 6x + 4y = 16.",
                            "answer": "infinite solutions",
                            "hint": "The second equation is a multiple of the first."
                        }
                    ]
                }
            }
        }

    def get_formula(self, section, formula_name):
        """Get a specific formula's information"""
        return self.formulas.get(section, {}).get(formula_name)

    def get_section_formulas(self, section):
        """Get all formulas for a specific section"""
        return self.formulas.get(section, {})

    def get_all_sections(self):
        """Get all available sections"""
        return list(self.formulas.keys())

    def get_practice_problems(self, section, formula_name):
        """Get practice problems for a specific formula"""
        formula = self.get_formula(section, formula_name)
        return formula.get('practice_problems', []) if formula else []

    def has_new_formulas(self):
        """Check if there are new formulas added to the database"""
        # This is a placeholder implementation. In a real application, you might want to check a database or API for new formulas.
        return False

class FormulaFinder:
    def __init__(self, root):
        self.root = root
        self.root.title("Formula Finder")
        self.root.geometry("1200x800")
        
        # Create main frame FIRST
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Initialize font sizes
        self.font_sizes = {
            'small': 10,
            'normal': 12,
            'large': 14,
            'title': 16,
            'subtitle': 14
        }
        
        # Initialize user data with default values
        self.user_data = {
            'last_login': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'name': '',
            'email': '',
            'settings': {
                'theme': 'light',
                'font_size': 'normal'
            }
        }
        
        # Load user data (this will override defaults if file exists)
        self.load_user_data()
        
        # Initialize test tracking
        self.current_test = None
        
        # Set up styles after loading user data
        self.setup_styles()
        
        # Initialize formula database
        self.formula_db = FormulaDatabase()
        
        # Initialize user progress tracking
        self.user_progress = {
            'completed_problems': {},
            'scores': {},
            'last_attempt': {},
            'favorite_formulas': {}
        }
        
        # Initialize session statistics
        self.session_stats = {
            'problems_attempted': 0,
            'correct_answers': 0,
            'time_spent': 0
        }
        
        # Create status bar
        self.status_bar = ttk.Label(self.root, text="", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Start session timer
        self.start_session_timer()
        
        # Show home screen
        self.show_home()
        
        # Initialize notes storage
        self.current_notes = {}  # Store notes for current session
    
    def start_session_timer(self):
        """Start the session timer"""
        def update_timer():
            self.session_stats['time_spent'] += 1
            self.update_status_bar()
            self.root.after(1000, update_timer)
        
        update_timer()
    
    def update_status_bar(self):
        """Update the status bar with session statistics"""
        stats = self.session_stats
        status_text = f"Problems Attempted: {stats['problems_attempted']} | " \
                     f"Correct Answers: {stats['correct_answers']} | " \
                     f"Time Spent: {stats['time_spent']} seconds"
        self.status_bar.config(text=status_text)
    
    def clear_main_frame(self):
        """Clear all widgets from the main frame"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_section_progress(self, section):
        """Display progress for a specific section"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Section", 
                               command=lambda: self.show_section(section),
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text=f"{section} Progress", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Progress information
        progress_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        progress_frame.pack(fill=tk.X, pady=10, padx=20)
        
        # Completed problems
        completed_label = ttk.Label(progress_frame, 
                                  text=f"Completed Problems: {len(self.user_progress['completed_problems'].get(section, []))}",
                                  style='Subtitle.TLabel')
        completed_label.pack(pady=5)
        
        # Average score
        scores = self.user_progress['scores'].get(section, [])
        average_score = sum(scores) / len(scores) if scores else 0
        score_label = ttk.Label(progress_frame, 
                              text=f"Average Score: {average_score:.2f}%",
                              style='Subtitle.TLabel')
        score_label.pack(pady=5)
        
        # Last attempt
        last_attempt = self.user_progress['last_attempt'].get(section, "No attempts yet")
        attempt_label = ttk.Label(progress_frame, 
                                text=f"Last Attempt: {last_attempt}",
                                style='Subtitle.TLabel')
        attempt_label.pack(pady=5)
        
        # Favorite formulas
        favorites = self.user_progress['favorite_formulas'].get(section, [])
        favorites_label = ttk.Label(progress_frame, 
                                  text=f"Favorite Formulas: {', '.join(favorites)}",
                                  style='Subtitle.TLabel')
        favorites_label.pack(pady=5)
    
    def start_practice_test(self, section):
        """Start a practice test for a specific section"""
        # Clear main frame
        self.clear_main_frame()
        
        # Get all formulas for this section
        formulas = self.formula_db.get_section_formulas(section)
        questions = []
        
        # Collect all practice problems
        for formula_name, formula_info in formulas.items():
            problems = formula_info.get('practice_problems', [])
            for problem in problems:
                problem['formula_name'] = formula_name  # Add formula name for reference
                questions.append(problem)
        
        # Shuffle questions
        random.shuffle(questions)
        
        # Limit to 10 questions
        questions = questions[:10]
        
        # Track test progress
        self.current_test = {
            'section': section,
            'questions': questions,
            'current_question': 0,
            'score': 0,
            'answers': []
        }
        
        # Display first question
        self.display_question()
    
    def display_question(self):
        """Display the current question in the practice test"""
        # Clear previous question
        for widget in self.main_frame.winfo_children():
            if isinstance(widget, ttk.Frame) and widget != self.main_frame:
                widget.destroy()
        
        # Create main canvas with scrollbar
        canvas = tk.Canvas(self.main_frame, bg=self.user_data['settings']['theme'] == 'dark' and '#1a1a1a' or '#ffffff')
        scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=canvas.yview)
        
        # Create main content frame that will be scrollable
        content_frame = ttk.Frame(canvas)
        
        # Configure canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Create window in canvas for content frame
        canvas_frame = canvas.create_window((0, 0), window=content_frame, anchor="nw", width=canvas.winfo_width())
        
        # Left side - Question and Answer
        left_frame = ttk.Frame(content_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 10), pady=10)
        
        # Get current question
        question = self.current_test['questions'][self.current_test['current_question']]
        
        # Question frame
        question_frame = ttk.Frame(left_frame, style='Card.TFrame')
        question_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Question number and text
        self.question_number_label = ttk.Label(question_frame, 
                 text=f"Question {self.current_test['current_question'] + 1} of {len(self.current_test['questions'])}", 
                 style='Title.TLabel')
        self.question_number_label.pack(pady=5)
        
        self.question_text_label = ttk.Label(question_frame, 
                 text=question['question'], 
                 style='Title.TLabel',
                 wraplength=600)
        self.question_text_label.pack(pady=5)
        
        # Answer input frame
        answer_frame = ttk.Frame(question_frame)
        answer_frame.pack(fill=tk.X, pady=5)
        
        # Answer entry with validation
        self.answer_var = tk.StringVar()
        self.answer_entry = ttk.Entry(answer_frame, 
                               textvariable=self.answer_var,
                               font=('Arial', self.font_sizes['normal']))
        self.answer_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        # Add Enter key binding
        self.answer_entry.bind('<Return>', lambda e: self.check_answer(question, self.answer_var.get()))
        
        # Buttons frame
        buttons_frame = ttk.Frame(question_frame)
        buttons_frame.pack(fill=tk.X, pady=5)
        
        # Submit button
        ttk.Button(buttons_frame,
                  text="Submit",
                  command=lambda: self.check_answer(question, self.answer_var.get()),
                  style='Category.TButton').pack(side=tk.LEFT, padx=5)
        
        # Hint button
        ttk.Button(buttons_frame,
                  text="Show Hint",
                  command=lambda: self.show_hint(question),
                  style='Category.TButton').pack(side=tk.LEFT, padx=5)
        
        # Skip button
        ttk.Button(buttons_frame,
                  text="Skip",
                  command=lambda: self.skip_question(question),
                  style='Category.TButton').pack(side=tk.LEFT, padx=5)
        
        # Right side - Calculator and Notes
        right_frame = ttk.Frame(content_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 20), pady=10)
        
        # Calculator
        calculator_frame = ttk.LabelFrame(right_frame, text="Calculator", style='Card.TFrame')
        calculator_frame.pack(fill=tk.X, pady=(0, 10))
        self.create_calculator(calculator_frame)
        
        # Notes/Scrap Work
        notes_frame = ttk.LabelFrame(right_frame, text="Scrap Work", style='Card.TFrame')
        notes_frame.pack(fill=tk.BOTH, expand=True)
        self.create_scrap_work_area(notes_frame)
        
        # Update scroll region when content changes
        def update_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        content_frame.bind('<Configure>', update_scroll_region)
        
        # Bind mouse wheel to scroll
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Make sure the canvas expands properly
        def _configure_canvas(event):
            # Update the width of the frame to match the canvas
            canvas.itemconfig(canvas_frame, width=event.width)
        
        canvas.bind('<Configure>', _configure_canvas)
        
        # Set focus to answer entry
        self.answer_entry.focus_set()
    
    def check_answer(self, question, answer):
        """Check the answer and move to next question"""
        # Check if answer is correct
        is_correct = self.check_single_answer(question, answer)
        
        # Update score
        if is_correct:
            self.current_test['score'] += 1
            self.show_feedback("Correct!", is_error=False)
        else:
            self.show_feedback(f"Incorrect. The correct answer is: {question['answer']}", is_error=True)
        
        # Store the answer
        self.current_test['answers'].append({
            'question': question['question'],
            'answer': answer,
            'correct': question['answer'],
            'hint': question['hint']
        })
        
        # Move to next question
        self.current_test['current_question'] += 1
        
        if self.current_test['current_question'] < len(self.current_test['questions']):
            # Get next question
            next_question = self.current_test['questions'][self.current_test['current_question']]
            
            # Update question text and number
            self.question_number_label.configure(text=f"Question {self.current_test['current_question'] + 1} of {len(self.current_test['questions'])}")
            self.question_text_label.configure(text=next_question['question'])
            
            # Clear answer entry
            self.answer_var.set("")
            self.answer_entry.focus_set()
        else:
            # Show end button if all questions are done
            self.show_end_button()
    
    def create_calculator(self, parent):
        """Create a calculator widget"""
        # Calculator display
        display = ttk.Entry(parent, justify='right', font=('Arial', self.font_sizes['normal']))
        display.pack(fill=tk.X, padx=5, pady=5)
        
        # Calculator buttons frame
        buttons_frame = ttk.Frame(parent)
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Create and place buttons
        row = 0
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.calculator_button_click(x, display)
            ttk.Button(buttons_frame, 
                      text=button,
                      command=cmd,
                      style='Category.TButton').grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_rowconfigure(i, weight=1)
    
    def calculator_button_click(self, button, display):
        """Handle calculator button clicks"""
        if button == '=':
            try:
                # Replace special functions with their math equivalents
                expression = display.get()
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('tan', 'math.tan')
                expression = expression.replace('π', 'math.pi')
                expression = expression.replace('√', 'math.sqrt')
                expression = expression.replace('x²', '**2')
                
                # Evaluate the expression
                result = eval(expression)
                display.delete(0, tk.END)
                display.insert(0, result)
            except Exception as e:
                display.delete(0, tk.END)
                display.insert(0, "Error")
        elif button in ['sin', 'cos', 'tan', 'π']:
            display.insert(tk.END, button)
        elif button == 'x²':
            display.insert(tk.END, '²')
        elif button == '√':
            display.insert(tk.END, '√(')
        else:
            display.insert(tk.END, button)
    
    def create_scrap_work_area(self, parent):
        """Create a scrap work area for notes and calculations"""
        # Create text widget with scrollbar
        text_frame = ttk.Frame(parent)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        notes_text = tk.Text(text_frame,
                            wrap=tk.WORD,
                            font=('Arial', self.font_sizes['normal']),
                            yscrollcommand=scrollbar.set)
        notes_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=notes_text.yview)
        
        # Save button
        ttk.Button(parent,
                  text="Save Notes",
                  command=lambda: self.save_notes(notes_text.get("1.0", tk.END)),
                  style='Category.TButton').pack(pady=5)
        
        # Load previous notes if they exist
        if hasattr(self, 'current_test') and self.current_test:
            section = self.current_test['section']
            question_num = self.current_test['current_question']
            notes_key = f"{section}_question_{question_num}"
            
            # Load from current session notes if available
            if notes_key in self.current_notes:
                notes_text.insert("1.0", self.current_notes[notes_key])
        
        return notes_text  # Return the text widget for reference
    
    def save_notes(self, notes):
        """Save notes for the current question"""
        if hasattr(self, 'current_test') and self.current_test:
            section = self.current_test['section']
            question_num = self.current_test['current_question']
            notes_key = f"{section}_question_{question_num}"
            
            # Store in current session notes
            self.current_notes[notes_key] = notes
            
            # Show feedback
            self.show_feedback("Notes saved successfully!")
    
    def show_home(self):
        """Display the home screen"""
        self.clear_main_frame()
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="Formula Finder", 
                              style='Title.TLabel')
        title_label.pack(pady=20)
        
        # Categories frame
        categories_frame = ttk.Frame(self.main_frame)
        categories_frame.pack(pady=20)
        
        # Category buttons
        categories = [
            "Quadratic Equations",
            "Trigonometry",
            "Calculus",
            "Algebra",
            "Geometry",
            "Functions"
        ]
        
        for category in categories:
            ttk.Button(categories_frame, 
                      text=category,
                      command=lambda c=category: self.show_section(c),
                      style='Category.TButton').pack(pady=10)
        
        # Navigation buttons
        nav_frame = ttk.Frame(self.main_frame)
        nav_frame.pack(pady=20)
        
        ttk.Button(nav_frame, 
                  text="Progress", 
                  command=self.show_progress,
                  style='Category.TButton').pack(side=tk.LEFT, padx=5)
        
        ttk.Button(nav_frame, 
                  text="Search", 
                  command=self.show_search,
                  style='Category.TButton').pack(side=tk.LEFT, padx=5)
        
        ttk.Button(nav_frame, 
                  text="Settings", 
                  command=self.show_settings,
                  style='Category.TButton').pack(side=tk.LEFT, padx=5)
        
        ttk.Button(nav_frame, 
                  text="Help", 
                  command=self.show_help,
                  style='Category.TButton').pack(side=tk.LEFT, padx=5)
        
        self.update_notification_badge()
    
    def update_notification_badge(self):
        """Update the notification badge on the home screen"""
        if hasattr(self, 'notification_badge'):
            self.notification_badge.destroy()
        
        notification_count = len(self.user_data.get('notifications', []))
        if notification_count > 0:
            self.notification_badge = ttk.Label(
                self.main_frame,
                text=str(notification_count),
                style='Notification.TLabel',
                background=self.colors['accent'],
                foreground='white'
            )
            self.notification_badge.place(relx=0.95, rely=0.05)
    
    def show_quadratics(self):
        """Display the Quadratic Equations section"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="Quadratic Equations", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Create navigation bar
        nav_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        nav_frame.pack(fill=tk.X, pady=10, padx=200)
        
        ttk.Button(nav_frame, 
                  text="📊 Section Progress", 
                  command=lambda: self.show_section_progress("Quadratic Equations"),
                  style='Category.TButton').pack(side=tk.LEFT, padx=10)
        
        ttk.Button(nav_frame, 
                  text="📝 Practice Test", 
                  command=lambda: self.start_practice_test("Quadratic Equations"),
                  style='Category.TButton').pack(side=tk.LEFT, padx=10)
        
        # Create scrollable frame
        canvas = tk.Canvas(self.main_frame, 
                         bg=self.colors['background'],
                         highlightthickness=0)
        
        scrollbar = ttk.Scrollbar(self.main_frame, 
                                orient="vertical", 
                                command=canvas.yview)
        
        scrollable_frame = ttk.Frame(canvas, style='Card.TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas_frame = canvas.create_window((0, 0), 
                                         window=scrollable_frame, 
                                         anchor="nw",
                                         width=canvas.winfo_width())
        
        canvas.bind('<Configure>', 
                   lambda e: canvas.itemconfig(canvas_frame, 
                                             width=e.width))
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Introduction to Quadratic Equations
        self.create_formula_card(scrollable_frame, {
            "title": "Introduction to Quadratic Equations",
            "formula": "A quadratic equation is an equation of the form ax² + bx + c = 0, where a, b, and c are constants and a ≠ 0.",
            "explanation": "Quadratic equations are fundamental in algebra and have applications in various fields including physics, engineering, and economics.",
            "steps": [
                "Understand the standard form of a quadratic equation",
                "Learn about the different methods to solve quadratic equations",
                "Master the quadratic formula",
                "Apply quadratic equations to solve real-world problems"
            ],
            "practice": {
                "problem": "Convert the equation 2x² - 5x + 3 = 0 to standard form.",
                "answer": "2x² - 5x + 3 = 0",
                "explanation": "1. The equation is already in standard form: ax² + bx + c = 0\n2. a = 2, b = -5, c = 3",
                "hint": "Ensure the equation is in the form ax² + bx + c = 0."
            }
        })
        
        # Standard Form
        self.create_formula_card(scrollable_frame, {
            "title": "Standard Form",
            "formula": "ax² + bx + c = 0",
            "explanation": "The standard form of a quadratic equation is ax² + bx + c = 0, where a, b, and c are constants and a ≠ 0.",
            "steps": [
                "Identify the coefficients a, b, and c",
                "Ensure the equation is set to zero",
                "Arrange terms in descending order of degree"
            ],
            "practice": {
                "problem": "Convert the equation 3x + 2x² = 5 to standard form.",
                "answer": "2x² + 3x - 5 = 0",
                "explanation": "1. Rearrange terms: 2x² + 3x - 5 = 0\n2. a = 2, b = 3, c = -5",
                "hint": "Rearrange the equation to the form ax² + bx + c = 0."
            }
        })
        
        # Add calculator and scrap work area
        self.create_calculator(scrollable_frame)
        self.create_scrap_work_area(scrollable_frame)
        
        # Quadratic Formula
        self.create_formula_card(scrollable_frame, {
            "title": "Quadratic Formula",
            "formula": "x = (-b ± √(b² - 4ac))/(2a)",
            "explanation": "The quadratic formula provides a method to solve any quadratic equation.",
            "steps": [
                "Identify the coefficients a, b, and c",
                "Substitute into the quadratic formula",
                "Simplify the expression",
                "Solve for x"
            ],
            "practice": {
                "problem": "Solve the equation x² - 5x + 6 = 0 using the quadratic formula.",
                "answer": "3, 2",
                "explanation": "1. a = 1, b = -5, c = 6\n2. x = (-(-5) ± √((-5)² - 4(1)(6)))/(2(1))\n3. x = (5 ± √(25 - 24))/2\n4. x = (5 ± √1)/2\n5. x = (5 ± 1)/2\n6. x = 3 or x = 2",
                "hint": "Use the quadratic formula: x = (-b ± √(b² - 4ac))/(2a)."
            }
        })
        
        # Vertex Form
        self.create_formula_card(scrollable_frame, {
            "title": "Vertex Form",
            "formula": "y = a(x - h)² + k",
            "explanation": "The vertex form of a quadratic equation is y = a(x - h)² + k, where (h, k) is the vertex of the parabola.",
            "steps": [
                "Complete the square to convert to vertex form",
                "Identify the vertex (h, k)",
                "Use the vertex to graph the parabola"
            ],
            "practice": {
                "problem": "Convert the equation y = x² - 4x + 3 to vertex form.",
                "answer": "y = (x - 3)² - 1",
                "explanation": "1. Complete the square: y = (x² - 4x + 4) - 4 + 3\n2. y = (x - 3)² - 1\n3. Vertex: (3, -1)",
                "hint": "Complete the square to convert to vertex form: y = a(x - h)² + k."
            }
        })
        
        # Factoring Method
        self.create_formula_card(scrollable_frame, {
            "title": "Factoring Method",
            "formula": "ax² + bx + c = (dx + e)(fx + g)",
            "explanation": "Factoring is a method to solve quadratic equations by expressing them as a product of linear factors.",
            "steps": [
                "Identify the coefficients a, b, and c",
                "Find factors of a and c",
                "Use trial and error to factor the equation",
                "Set each factor to zero and solve for x"
            ],
            "practice": {
                "problem": "Solve the equation x² - 5x + 6 = 0 by factoring.",
                "answer": "3, 2",
                "explanation": "1. x² - 5x + 6 = (x - 3)(x - 2)\n2. Set each factor to zero: x - 3 = 0 or x - 2 = 0\n3. x = 3 or x = 2",
                "hint": "Factor the equation into the form (x - p)(x - q) = 0."
            }
        })
        
        # Projectile Motion Problem
        self.create_formula_card(scrollable_frame, {
            "title": "Projectile Motion Problem",
            "formula": "h(t) = -16t² + v₀t + h₀",
            "explanation": "Projectile motion can be modeled using quadratic equations, where h(t) is the height at time t, v₀ is the initial velocity, and h₀ is the initial height.",
            "steps": [
                "Identify the initial velocity and height",
                "Use the quadratic equation to model the height",
                "Solve for the time when the projectile hits the ground"
            ],
            "practice": {
                "problem": "A ball is thrown upward with an initial velocity of 20 m/s from a height of 5 meters. When will the ball hit the ground?",
                "answer": "1.25",
                "explanation": "1. h(t) = -16t² + 20t + 5\n2. Set h(t) = 0: -16t² + 20t + 5 = 0\n3. Use the quadratic formula: t = (-20 ± √(400 + 320))/(-32)\n4. t = (-20 ± √720)/(-32)\n5. t = (-20 ± 26.83)/(-32)\n6. t = 1.25 seconds",
                "hint": "Use the quadratic equation h(t) = -16t² + v₀t + h₀ to model the height."
            }
        })
        
        # Applications in Real Life
        self.create_formula_card(scrollable_frame, {
            "title": "Applications in Real Life",
            "formula": "Various applications of quadratic equations in different fields",
            "explanation": "Quadratic equations are used in many real-world situations, including physics, engineering, and economics.",
            "steps": [
                "Physics: Projectile motion and free fall",
                "Engineering: Structural design and optimization",
                "Economics: Profit maximization and cost minimization",
                "Biology: Population growth and decay",
                "Computer Science: Algorithm analysis and optimization"
            ],
            "practice": {
                "problem": "A company's profit is modeled by the equation P(x) = -2x² + 100x - 800, where x is the number of units sold. How many units should be sold to maximize profit?",
                "answer": "25",
                "explanation": "1. The profit function is a quadratic equation opening downward\n2. The maximum profit occurs at the vertex\n3. x = -b/(2a) = -100/(2(-2)) = 25 units",
                "hint": "Find the vertex of the quadratic equation to determine the maximum profit."
            }
        })

    def show_trigonometry(self):
        """Display the Trigonometry section"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="Trigonometry", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Create navigation bar
        nav_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        nav_frame.pack(fill=tk.X, pady=10, padx=200)
        
        ttk.Button(nav_frame, 
                  text="📊 Section Progress", 
                  command=lambda: self.show_section_progress("Trigonometry"),
                  style='Category.TButton').pack(side=tk.LEFT, padx=10)
        
        ttk.Button(nav_frame, 
                  text="📝 Practice Test", 
                  command=lambda: self.start_practice_test("Trigonometry"),
                  style='Category.TButton').pack(side=tk.LEFT, padx=10)
        
        # Create scrollable frame
        canvas = tk.Canvas(self.main_frame, 
                         bg=self.colors['background'],
                         highlightthickness=0)
        
        scrollbar = ttk.Scrollbar(self.main_frame, 
                                orient="vertical", 
                                command=canvas.yview)
        
        scrollable_frame = ttk.Frame(canvas, style='Card.TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas_frame = canvas.create_window((0, 0), 
                                         window=scrollable_frame, 
                                         anchor="nw",
                                         width=canvas.winfo_width())
        
        canvas.bind('<Configure>', 
                   lambda e: canvas.itemconfig(canvas_frame, 
                                             width=e.width))
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Introduction to Trigonometry
        self.create_formula_card(scrollable_frame, {
            "title": "Introduction to Trigonometry",
            "formula": "Trigonometry is the study of relationships between the sides and angles of triangles.",
            "explanation": "Trigonometry is fundamental in understanding periodic phenomena and is used in various fields including physics, engineering, and navigation.",
            "steps": [
                "Understand the basic trigonometric functions",
                "Learn about the unit circle",
                "Master trigonometric identities",
                "Apply trigonometry to solve problems"
            ],
            "practice": {
                "problem": "In a right triangle, if the opposite side is 3 units and the hypotenuse is 5 units, find the sine of the angle.",
                "answer": "0.6",
                "explanation": "1. sin(θ) = opposite/hypotenuse\n2. sin(θ) = 3/5\n3. sin(θ) = 0.6",
                "hint": "Use the definition of sine: sin(θ) = opposite/hypotenuse."
            }
        })
        
        # Basic Trigonometric Ratios
        self.create_formula_card(scrollable_frame, {
            "title": "Basic Trigonometric Ratios",
            "formula": "sin(θ) = opposite/hypotenuse\ncos(θ) = adjacent/hypotenuse\ntan(θ) = opposite/adjacent",
            "explanation": "These ratios relate the angles of a right triangle to the lengths of its sides.",
            "steps": [
                "Identify the sides of the triangle",
                "Use the appropriate trigonometric ratio",
                "Substitute values and solve"
            ],
            "practice": {
                "problem": "In a right triangle, if the adjacent side is 4 units and the hypotenuse is 5 units, find the cosine of the angle.",
                "answer": "0.8",
                "explanation": "1. cos(θ) = adjacent/hypotenuse\n2. cos(θ) = 4/5\n3. cos(θ) = 0.8",
                "hint": "Use the definition of cosine: cos(θ) = adjacent/hypotenuse."
            }
        })
        
        # Add calculator and scrap work area
        self.create_calculator(scrollable_frame)
        self.create_scrap_work_area(scrollable_frame)
        
        # Pythagorean Identity
        self.create_formula_card(scrollable_frame, {
            "title": "Pythagorean Identity",
            "formula": "sin²(θ) + cos²(θ) = 1",
            "explanation": "This identity relates the sine and cosine of an angle.",
            "steps": [
                "Use the Pythagorean Identity",
                "Substitute known values",
                "Solve for the unknown"
            ],
            "practice": {
                "problem": "If sin(θ) = 0.6, find cos(θ).",
                "answer": "0.8",
                "explanation": "1. sin²(θ) + cos²(θ) = 1\n2. (0.6)² + cos²(θ) = 1\n3. 0.36 + cos²(θ) = 1\n4. cos²(θ) = 0.64\n5. cos(θ) = 0.8",
                "hint": "Use the Pythagorean Identity: sin²(θ) + cos²(θ) = 1."
            }
        })
        
        # Law of Sines
        self.create_formula_card(scrollable_frame, {
            "title": "Law of Sines",
            "formula": "a/sin(A) = b/sin(B) = c/sin(C)",
            "explanation": "The Law of Sines relates the sides of a triangle to the sines of its angles.",
            "steps": [
                "Identify the sides and angles",
                "Use the Law of Sines",
                "Substitute values and solve"
            ],
            "practice": {
                "problem": "In triangle ABC, if angle A = 30°, angle B = 45°, and side a = 10 units, find side b.",
                "answer": "14.14",
                "explanation": "1. a/sin(A) = b/sin(B)\n2. 10/sin(30°) = b/sin(45°)\n3. 10/0.5 = b/0.707\n4. 20 = b/0.707\n5. b = 14.14 units",
                "hint": "Use the Law of Sines: a/sin(A) = b/sin(B)."
            }
        })
        
        # Law of Cosines
        self.create_formula_card(scrollable_frame, {
            "title": "Law of Cosines",
            "formula": "c² = a² + b² - 2ab cos(C)",
            "explanation": "The Law of Cosines relates the sides of a triangle to the cosine of one of its angles.",
            "steps": [
                "Identify the sides and angles",
                "Use the Law of Cosines",
                "Substitute values and solve"
            ],
            "practice": {
                "problem": "In triangle ABC, if side a = 5 units, side b = 7 units, and angle C = 60°, find side c.",
                "answer": "6.24",
                "explanation": "1. c² = a² + b² - 2ab cos(C)\n2. c² = 5² + 7² - 2(5)(7)cos(60°)\n3. c² = 25 + 49 - 70(0.5)\n4. c² = 74 - 35\n5. c² = 39\n6. c = 6.24 units",
                "hint": "Use the Law of Cosines: c² = a² + b² - 2ab cos(C)."
            }
        })
        
        # Double Angle Formulas
        self.create_formula_card(scrollable_frame, {
            "title": "Double Angle Formulas",
            "formula": "sin(2x) = 2sin(x)cos(x)\ncos(2x) = cos²(x) - sin²(x)\ntan(2x) = 2tan(x)/(1 - tan²(x))",
            "explanation": "These formulas express trigonometric functions of twice an angle in terms of functions of the original angle.",
            "steps": [
                "Identify the angle",
                "Use the appropriate double angle formula",
                "Substitute values and solve"
            ],
            "practice": {
                "problem": "If sin(x) = 0.6 and cos(x) = 0.8, find sin(2x).",
                "answer": "0.96",
                "explanation": "1. sin(2x) = 2sin(x)cos(x)\n2. sin(2x) = 2(0.6)(0.8)\n3. sin(2x) = 0.96",
                "hint": "Use the double angle formula: sin(2x) = 2sin(x)cos(x)."
            }
        })
        
        # Applications in Real Life
        self.create_formula_card(scrollable_frame, {
            "title": "Applications in Real Life",
            "formula": "Various applications of trigonometry in different fields",
            "explanation": "Trigonometry is used in many real-world situations, including navigation, architecture, and physics.",
            "steps": [
                "Navigation: GPS and compass bearings",
                "Architecture: Structural design and surveying",
                "Physics: Wave motion and oscillations",
                "Engineering: Signal processing and control systems",
                "Astronomy: Celestial navigation and star tracking"
            ],
            "practice": {
                "problem": "A ladder is leaning against a wall at an angle of 60° to the ground. If the ladder is 20 feet long, how high up the wall does it reach?",
                "answer": "17.32",
                "explanation": "1. sin(60°) = height/20\n2. height = 20sin(60°)\n3. height = 20(0.866)\n4. height = 17.32 feet",
                "hint": "Use the sine function to find the height: sin(θ) = opposite/hypotenuse."
            }
        })

    def show_calculus(self):
        """Display the Calculus section"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="Calculus", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Create navigation bar
        nav_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        nav_frame.pack(fill=tk.X, pady=10, padx=200)
        
        ttk.Button(nav_frame, 
                  text="📊 Section Progress", 
                  command=lambda: self.show_section_progress("Calculus"),
                  style='Category.TButton').pack(side=tk.LEFT, padx=10)
        
        ttk.Button(nav_frame, 
                  text="📝 Practice Test", 
                  command=lambda: self.start_practice_test("Calculus"),
                  style='Category.TButton').pack(side=tk.LEFT, padx=10)
        
        # Create scrollable frame
        canvas = tk.Canvas(self.main_frame, 
                         bg=self.colors['background'],
                         highlightthickness=0)
        
        scrollbar = ttk.Scrollbar(self.main_frame, 
                                orient="vertical", 
                                command=canvas.yview)
        
        scrollable_frame = ttk.Frame(canvas, style='Card.TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas_frame = canvas.create_window((0, 0), 
                                         window=scrollable_frame, 
                                         anchor="nw",
                                         width=canvas.winfo_width())
        
        canvas.bind('<Configure>', 
                   lambda e: canvas.itemconfig(canvas_frame, 
                                             width=e.width))
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Introduction to Calculus
        self.create_formula_card(scrollable_frame, {
            "title": "Introduction to Calculus",
            "formula": "Calculus is the mathematical study of continuous change, focusing on derivatives and integrals.",
            "explanation": "Calculus is fundamental in understanding rates of change and accumulation, with applications in physics, engineering, and economics.",
            "steps": [
                "Understand limits and continuity",
                "Learn about derivatives and their applications",
                "Master integration techniques",
                "Apply calculus to solve real-world problems"
            ],
            "practice": {
                "problem": "Find the limit of (x² - 4)/(x - 2) as x approaches 2.",
                "answer": "4",
                "explanation": "1. Factor the numerator: (x + 2)(x - 2)/(x - 2)\n2. Cancel (x - 2): x + 2\n3. Substitute x = 2: 2 + 2 = 4",
                "hint": "Factor the numerator to cancel out the denominator."
            }
        })
        
        # Basic Derivatives
        self.create_formula_card(scrollable_frame, {
            "title": "Basic Derivatives",
            "formula": "Power Rule: d/dx(x^n) = nx^(n-1)\nSum Rule: d/dx(f(x) + g(x)) = f'(x) + g'(x)\nProduct Rule: d/dx(f(x)g(x)) = f'(x)g(x) + f(x)g'(x)\nQuotient Rule: d/dx(f(x)/g(x)) = (f'(x)g(x) - f(x)g'(x))/g(x)²",
            "explanation": "Derivatives measure the rate of change of a function with respect to its variable.",
            "steps": [
                "Identify the function to differentiate",
                "Apply the appropriate derivative rules",
                "Simplify the result"
            ],
            "practice": {
                "problem": "Find the derivative of f(x) = x³ + 2x² - 5x + 3.",
                "answer": "3x² + 4x - 5",
                "explanation": "1. Apply Power Rule to each term\n2. d/dx(x³) = 3x²\n3. d/dx(2x²) = 4x\n4. d/dx(-5x) = -5\n5. d/dx(3) = 0\n6. Combine: 3x² + 4x - 5",
                "hint": "Use the Power Rule for each term."
            }
        })
        
        # Add calculator and scrap work area
        self.create_calculator(scrollable_frame)
        self.create_scrap_work_area(scrollable_frame)
        
        # Chain Rule
        self.create_formula_card(scrollable_frame, {
            "title": "Chain Rule",
            "formula": "d/dx(f(g(x))) = f'(g(x))g'(x)",
            "explanation": "The Chain Rule is used to differentiate composite functions.",
            "steps": [
                "Identify the outer and inner functions",
                "Differentiate the outer function",
                "Differentiate the inner function",
                "Multiply the results"
            ],
            "practice": {
                "problem": "Find the derivative of f(x) = (x² + 1)³.",
                "answer": "6x(x² + 1)²",
                "explanation": "1. Outer function: f(u) = u³, f'(u) = 3u²\n2. Inner function: g(x) = x² + 1, g'(x) = 2x\n3. Apply Chain Rule: 3(x² + 1)²(2x)\n4. Simplify: 6x(x² + 1)²",
                "hint": "Use the Chain Rule to differentiate the composite function."
            }
        })
        
        # Basic Integration
        self.create_formula_card(scrollable_frame, {
            "title": "Basic Integration",
            "formula": "Power Rule: ∫x^n dx = (x^(n+1))/(n+1) + C\nSum Rule: ∫(f(x) + g(x)) dx = ∫f(x) dx + ∫g(x) dx\nConstant Multiple Rule: ∫cf(x) dx = c∫f(x) dx",
            "explanation": "Integration is the reverse process of differentiation, used to find areas and accumulate quantities.",
            "steps": [
                "Identify the function to integrate",
                "Apply the appropriate integration rules",
                "Add the constant of integration"
            ],
            "practice": {
                "problem": "Find the integral of f(x) = 2x³ - 3x² + 4x - 1.",
                "answer": "0.5x⁴ - x³ + 2x² - x + C",
                "explanation": "1. Apply Power Rule to each term\n2. ∫2x³ dx = 0.5x⁴\n3. ∫-3x² dx = -x³\n4. ∫4x dx = 2x²\n5. ∫-1 dx = -x\n6. Combine: 0.5x⁴ - x³ + 2x² - x + C",
                "hint": "Use the Power Rule for each term and add the constant of integration."
            }
        })
        
        # Applications of Derivatives
        self.create_formula_card(scrollable_frame, {
            "title": "Applications of Derivatives",
            "formula": "Various applications of derivatives in different fields",
            "explanation": "Derivatives are used to analyze rates of change and optimize functions.",
            "steps": [
                "Physics: Velocity and acceleration",
                "Economics: Marginal cost and revenue",
                "Engineering: Optimization and control systems",
                "Biology: Population growth and decay",
                "Computer Science: Algorithm analysis"
            ],
            "practice": {
                "problem": "A ball is thrown upward with an initial velocity of 20 m/s. The height h(t) in meters after t seconds is given by h(t) = -5t² + 20t. Find the maximum height reached by the ball.",
                "answer": "20",
                "explanation": "1. Find the derivative: h'(t) = -10t + 20\n2. Set h'(t) = 0: -10t + 20 = 0\n3. Solve for t: t = 2 seconds\n4. Substitute t = 2 into h(t): h(2) = -5(2)² + 20(2) = -20 + 40 = 20 meters",
                "hint": "Find the critical points by setting the derivative equal to zero."
            }
        })
        
        # Applications of Integration
        self.create_formula_card(scrollable_frame, {
            "title": "Applications of Integration",
            "formula": "Various applications of integration in different fields",
            "explanation": "Integration is used to find areas, volumes, and accumulated quantities.",
            "steps": [
                "Physics: Work and energy",
                "Economics: Consumer and producer surplus",
                "Engineering: Center of mass and moment of inertia",
                "Biology: Growth and decay models",
                "Computer Science: Probability and statistics"
            ],
            "practice": {
                "problem": "Find the area under the curve y = x² from x = 0 to x = 2.",
                "answer": "2.67",
                "explanation": "1. Set up the integral: ∫₀² x² dx\n2. Integrate: [x³/3]₀²\n3. Evaluate: (2³/3) - (0³/3) = 8/3 ≈ 2.67 square units",
                "hint": "Use the definite integral to find the area under the curve."
            }
        })

    def show_algebra(self):
        """Display the Algebra section"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="Algebra", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Create navigation bar
        nav_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        nav_frame.pack(fill=tk.X, pady=10, padx=200)
        
        ttk.Button(nav_frame, 
                  text="📊 Section Progress", 
                  command=lambda: self.show_section_progress("Algebra"),
                  style='Category.TButton').pack(side=tk.LEFT, padx=10)
        
        ttk.Button(nav_frame, 
                  text="📝 Practice Test", 
                  command=lambda: self.start_practice_test("Algebra"),
                  style='Category.TButton').pack(side=tk.LEFT, padx=10)
        
        # Create scrollable frame
        canvas = tk.Canvas(self.main_frame, 
                         bg=self.colors['background'],
                         highlightthickness=0)
        
        scrollbar = ttk.Scrollbar(self.main_frame, 
                                orient="vertical", 
                                command=canvas.yview)
        
        scrollable_frame = ttk.Frame(canvas, style='Card.TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas_frame = canvas.create_window((0, 0), 
                                         window=scrollable_frame, 
                                         anchor="nw",
                                         width=canvas.winfo_width())
        
        canvas.bind('<Configure>', 
                   lambda e: canvas.itemconfig(canvas_frame, 
                                             width=e.width))
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Introduction to Algebra
        self.create_formula_card(scrollable_frame, {
            "title": "Introduction to Algebra",
            "formula": "Algebra is the branch of mathematics dealing with symbols and the rules for manipulating these symbols.",
            "explanation": "Algebra is fundamental in mathematics and has applications in various fields including science, engineering, and economics.",
            "steps": [
                "Understand variables and constants",
                "Learn about algebraic expressions",
                "Master equation solving techniques",
                "Apply algebraic concepts to solve real-world problems"
            ],
            "practice": {
                "problem": "Simplify the expression: 3x + 2y - x + 4y",
                "answer": "2x + 6y",
                "explanation": "1. Combine like terms: 3x - x = 2x\n2. Combine like terms: 2y + 4y = 6y\n3. Final expression: 2x + 6y",
                "hint": "Combine terms with the same variables."
            }
        })
        
        # Factoring Methods
        self.create_formula_card(scrollable_frame, {
            "title": "Factoring Methods",
            "formula": "Difference of Squares: a² - b² = (a + b)(a - b)\nPerfect Squares: a² ± 2ab + b² = (a ± b)²",
            "explanation": "Factoring is the process of breaking down an expression into a product of simpler expressions.",
            "steps": [
                "Identify the type of expression",
                "Apply the appropriate factoring method",
                "Verify the factored form"
            ],
            "practice": {
                "problem": "Factor the expression: x² - 16",
                "answer": "(x + 4)(x - 4)",
                "explanation": "1. Recognize as difference of squares: x² - 16 = x² - 4²\n2. Apply formula: a² - b² = (a + b)(a - b)\n3. Substitute: (x + 4)(x - 4)",
                "hint": "Look for a pattern of a² - b² in the expression."
            }
        })
        
        # Add calculator and scrap work area
        self.create_calculator(scrollable_frame)
        self.create_scrap_work_area(scrollable_frame)
        
        # Systems of Linear Equations
        self.create_formula_card(scrollable_frame, {
            "title": "Systems of Linear Equations",
            "formula": "Substitution Method:\n1. Solve one equation for one variable\n2. Substitute into other equation\n\nElimination Method:\n1. Add or subtract equations to eliminate one variable\n2. Solve for remaining variable",
            "explanation": "Systems of linear equations are sets of equations with multiple variables. They can be solved using various methods.",
            "steps": [
                "Choose a method (substitution or elimination)",
                "Follow the steps for the chosen method",
                "Solve for each variable",
                "Verify the solution"
            ],
            "practice": {
                "problem": "Solve the system:\n2x + y = 5\n3x - y = 4",
                "answer": "1.8",
                "explanation": "1. Add equations: 5x = 9\n2. x = 9/5 = 1.8\n3. Substitute: 2(1.8) + y = 5\n4. 3.6 + y = 5\n5. y = 1.4",
                "hint": "Use the elimination method by adding the equations to eliminate y."
            }
        })
        
        # Polynomial Operations
        self.create_formula_card(scrollable_frame, {
            "title": "Polynomial Operations",
            "formula": "Addition, subtraction, multiplication, and division of polynomials",
            "explanation": "Polynomials are expressions with multiple terms. Understanding how to perform operations on them is essential in algebra.",
            "steps": [
                "Identify the type of operation",
                "Apply the appropriate rules",
                "Simplify the result"
            ],
            "practice": {
                "problem": "Multiply (x + 2)(x - 3)",
                "answer": "x² - x - 6",
                "explanation": "1. Use FOIL method: First, Outer, Inner, Last\n2. First: x × x = x²\n3. Outer: x × (-3) = -3x\n4. Inner: 2 × x = 2x\n5. Last: 2 × (-3) = -6\n6. Combine like terms: x² - x - 6",
                "hint": "Use the FOIL method to multiply binomials."
            }
        })
        
        # Rational Expressions
        self.create_formula_card(scrollable_frame, {
            "title": "Rational Expressions",
            "formula": "Operations with fractions containing variables",
            "explanation": "Rational expressions are fractions with polynomials in the numerator and denominator.",
            "steps": [
                "Factor numerators and denominators",
                "Cancel common factors",
                "Perform the required operation",
                "Simplify the result"
            ],
            "practice": {
                "problem": "Simplify (x² - 4)/(x - 2)",
                "answer": "x + 2",
                "explanation": "1. Factor numerator: (x + 2)(x - 2)/(x - 2)\n2. Cancel (x - 2): x + 2",
                "hint": "Factor the numerator to cancel out the denominator."
            }
        })
        
        # Applications in Real Life
        self.create_formula_card(scrollable_frame, {
            "title": "Applications in Real Life",
            "formula": "Various applications of algebra in different fields",
            "explanation": "Algebra is used in many real-world situations, including finance, science, and engineering.",
            "steps": [
                "Finance: Interest calculations, budgeting",
                "Science: Chemical equations, physics formulas",
                "Engineering: Design calculations, optimization",
                "Economics: Supply and demand analysis",
                "Statistics: Data analysis and interpretation"
            ],
            "practice": {
                "problem": "A mixture problem: How many liters of a 20% acid solution must be mixed with a 50% acid solution to get 30 liters of a 40% acid solution?",
                "answer": "10",
                "explanation": "1. Let x be liters of 20% solution\n2. 30 - x is liters of 50% solution\n3. 0.2x + 0.5(30 - x) = 0.4(30)\n4. 0.2x + 15 - 0.5x = 12\n5. -0.3x = -3\n6. x = 10 liters",
                "hint": "Set up an equation using the concentration percentages and total volume."
            }
        })

    def show_geometry(self):
        """Display the Geometry section"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="Geometry", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Create navigation bar
        nav_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        nav_frame.pack(fill=tk.X, pady=10, padx=200)
        
        ttk.Button(nav_frame, 
                  text="📊 Section Progress", 
                  command=lambda: self.show_section_progress("Geometry"),
                  style='Category.TButton').pack(side=tk.LEFT, padx=10)
        
        ttk.Button(nav_frame, 
                  text="📝 Practice Test", 
                  command=lambda: self.start_practice_test("Geometry"),
                  style='Category.TButton').pack(side=tk.LEFT, padx=10)
        
        # Create scrollable frame
        canvas = tk.Canvas(self.main_frame, 
                         bg=self.colors['background'],
                         highlightthickness=0)
        
        scrollbar = ttk.Scrollbar(self.main_frame, 
                                orient="vertical", 
                                command=canvas.yview)
        
        scrollable_frame = ttk.Frame(canvas, style='Card.TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas_frame = canvas.create_window((0, 0), 
                                         window=scrollable_frame, 
                                         anchor="nw",
                                         width=canvas.winfo_width())
        
        canvas.bind('<Configure>', 
                   lambda e: canvas.itemconfig(canvas_frame, 
                                             width=e.width))
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Introduction to Geometry
        self.create_formula_card(scrollable_frame, {
            "title": "Introduction to Geometry",
            "formula": "Geometry is the branch of mathematics concerned with the properties and relationships of points, lines, angles, surfaces, and solids.",
            "explanation": "Geometry is fundamental in understanding spatial relationships and is used in various fields including architecture, engineering, and art.",
            "steps": [
                "Understand basic geometric concepts",
                "Learn about different types of shapes",
                "Master measurement and calculation techniques",
                "Apply geometric principles to solve problems"
            ],
            "practice": {
                "problem": "Find the perimeter of a rectangle with length 8 units and width 5 units.",
                "answer": "26",
                "explanation": "1. Perimeter = 2(length + width)\n2. P = 2(8 + 5)\n3. P = 2(13)\n4. P = 26 units",
                "hint": "Use the formula for rectangle perimeter: P = 2(l + w)."
            }
        })
        
        # Circle Formulas
        self.create_formula_card(scrollable_frame, {
            "title": "Circle Formulas",
            "formula": "Area = πr²\nCircumference = 2πr\nArc Length = (θ/360) × 2πr\nSector Area = (θ/360) × πr²",
            "explanation": "Circles are fundamental geometric shapes with unique properties and formulas.",
            "steps": [
                "Identify the given information",
                "Choose the appropriate formula",
                "Substitute values and solve"
            ],
            "practice": {
                "problem": "Find the area of a circle with radius 5 units.",
                "answer": "78.54",
                "explanation": "1. Area = πr²\n2. A = π(5)²\n3. A = 25π\n4. A ≈ 78.54 square units",
                "hint": "Use the area formula A = πr² and remember π ≈ 3.14159."
            }
        })
        
        # Add calculator and scrap work area
        self.create_calculator(scrollable_frame)
        self.create_scrap_work_area(scrollable_frame)
        
        # Triangle Formulas
        self.create_formula_card(scrollable_frame, {
            "title": "Triangle Formulas",
            "formula": "Area = (1/2)bh\nPerimeter = a + b + c\nPythagorean Theorem: a² + b² = c²",
            "explanation": "Triangles are three-sided polygons with various properties and formulas for calculating their measurements.",
            "steps": [
                "Identify the type of triangle",
                "Use the appropriate formula",
                "Substitute values and solve"
            ],
            "practice": {
                "problem": "Find the area of a triangle with base 6 units and height 8 units.",
                "answer": "24",
                "explanation": "1. Area = (1/2)bh\n2. A = (1/2)(6)(8)\n3. A = (1/2)(48)\n4. A = 24 square units",
                "hint": "Use the area formula A = (1/2)bh."
            }
        })
        
        # Volume Formulas
        self.create_formula_card(scrollable_frame, {
            "title": "Volume Formulas",
            "formula": "Cube: V = s³\nRectangular Prism: V = lwh\nCylinder: V = πr²h\nSphere: V = (4/3)πr³",
            "explanation": "Volume is the measure of space occupied by a three-dimensional object.",
            "steps": [
                "Identify the shape",
                "Use the appropriate volume formula",
                "Substitute values and solve"
            ],
            "practice": {
                "problem": "Find the volume of a cylinder with radius 3 units and height 4 units.",
                "answer": "113.10",
                "explanation": "1. Volume = πr²h\n2. V = π(3)²(4)\n3. V = π(9)(4)\n4. V = 36π\n5. V ≈ 113.10 cubic units",
                "hint": "Use the volume formula V = πr²h."
            }
        })
        
        # Surface Area Formulas
        self.create_formula_card(scrollable_frame, {
            "title": "Surface Area Formulas",
            "formula": "Cube: SA = 6s²\nRectangular Prism: SA = 2lw + 2lh + 2wh\nCylinder: SA = 2πr² + 2πrh\nSphere: SA = 4πr²",
            "explanation": "Surface area is the total area of all faces of a three-dimensional object.",
            "steps": [
                "Identify the shape",
                "Use the appropriate surface area formula",
                "Substitute values and solve"
            ],
            "practice": {
                "problem": "Find the surface area of a cube with side length 5 units.",
                "answer": "150",
                "explanation": "1. Surface Area = 6s²\n2. SA = 6(5)²\n3. SA = 6(25)\n4. SA = 150 square units",
                "hint": "Use the surface area formula SA = 6s²."
            }
        })
        
        # Applications in Real Life
        self.create_formula_card(scrollable_frame, {
            "title": "Applications in Real Life",
            "formula": "Various applications of geometry in different fields",
            "explanation": "Geometry is used in many real-world situations, including architecture, engineering, and design.",
            "steps": [
                "Architecture: Building design and construction",
                "Engineering: Structural analysis and design",
                "Art: Perspective and composition",
                "Navigation: Maps and GPS systems",
                "Sports: Field and court design"
            ],
            "practice": {
                "problem": "A swimming pool is 20 meters long, 10 meters wide, and 2 meters deep. How many cubic meters of water are needed to fill it?",
                "answer": "400",
                "explanation": "1. Volume = length × width × height\n2. V = 20 × 10 × 2\n3. V = 400 cubic meters",
                "hint": "Use the volume formula for a rectangular prism: V = lwh."
            }
        })

    def show_functions(self):
        """Display the Functions section"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="Functions", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Create navigation bar
        nav_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        nav_frame.pack(fill=tk.X, pady=10, padx=200)
        
        ttk.Button(nav_frame, 
                  text="📊 Section Progress", 
                  command=lambda: self.show_section_progress("Functions"),
                  style='Category.TButton').pack(side=tk.LEFT, padx=10)
        
        ttk.Button(nav_frame, 
                  text="📝 Practice Test", 
                  command=lambda: self.start_practice_test("Functions"),
                  style='Category.TButton').pack(side=tk.LEFT, padx=10)
        
        # Create scrollable frame
        canvas = tk.Canvas(self.main_frame, 
                         bg=self.colors['background'],
                         highlightthickness=0)
        
        scrollbar = ttk.Scrollbar(self.main_frame, 
                                orient="vertical", 
                                command=canvas.yview)
        
        scrollable_frame = ttk.Frame(canvas, style='Card.TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas_frame = canvas.create_window((0, 0), 
                                         window=scrollable_frame, 
                                         anchor="nw",
                                         width=canvas.winfo_width())
        
        canvas.bind('<Configure>', 
                   lambda e: canvas.itemconfig(canvas_frame, 
                                             width=e.width))
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Introduction to Functions
        self.create_formula_card(scrollable_frame, {
            "title": "Introduction to Functions",
            "formula": "A function is a relation between a set of inputs and a set of outputs where each input is related to exactly one output.",
            "explanation": "Functions are fundamental in mathematics and are used to model relationships between variables.",
            "steps": [
                "Understand the concept of a function",
                "Learn about domain and range",
                "Master function notation",
                "Apply functions to solve problems"
            ],
            "practice": {
                "problem": "Given f(x) = 2x + 3, find f(4).",
                "answer": "11",
                "explanation": "1. Substitute x = 4 into f(x)\n2. f(4) = 2(4) + 3\n3. f(4) = 8 + 3\n4. f(4) = 11",
                "hint": "Replace x with 4 in the function f(x) = 2x + 3."
            }
        })
        
        # Function Transformations
        self.create_formula_card(scrollable_frame, {
            "title": "Function Transformations",
            "formula": "Vertical Shift: f(x) + k\nHorizontal Shift: f(x - h)\nVertical Stretch/Compression: af(x)\nHorizontal Stretch/Compression: f(bx)",
            "explanation": "Transformations change the graph of a function without changing its basic shape.",
            "steps": [
                "Identify the type of transformation",
                "Apply the transformation to the function",
                "Graph the transformed function"
            ],
            "practice": {
                "problem": "If f(x) = x², what is the equation of f(x) shifted 3 units up and 2 units right?",
                "answer": "(x - 2)² + 3",
                "explanation": "1. Start with f(x) = x²\n2. Shift right: f(x - 2) = (x - 2)²\n3. Shift up: f(x - 2) + 3 = (x - 2)² + 3",
                "hint": "Apply the horizontal shift first, then the vertical shift."
            }
        })
        
        # Add calculator and scrap work area
        self.create_calculator(scrollable_frame)
        self.create_scrap_work_area(scrollable_frame)
        
        # Inverse Functions
        self.create_formula_card(scrollable_frame, {
            "title": "Inverse Functions",
            "formula": "To find the inverse of a function, swap x and y and solve for y.",
            "explanation": "The inverse of a function undoes the original function's operation.",
            "steps": [
                "Replace f(x) with y",
                "Swap x and y",
                "Solve for y",
                "Replace y with f⁻¹(x)"
            ],
            "practice": {
                "problem": "Find the inverse of f(x) = 2x + 3.",
                "answer": "(x - 3)/2",
                "explanation": "1. y = 2x + 3\n2. x = 2y + 3\n3. x - 3 = 2y\n4. y = (x - 3)/2\n5. f⁻¹(x) = (x - 3)/2",
                "hint": "Swap x and y, then solve for y."
            }
        })
        
        # Composite Functions
        self.create_formula_card(scrollable_frame, {
            "title": "Composite Functions",
            "formula": "f(g(x)) means apply g first, then apply f to the result.",
            "explanation": "Composite functions combine two functions to create a new function.",
            "steps": [
                "Identify the functions to compose",
                "Apply the inner function first",
                "Apply the outer function to the result"
            ],
            "practice": {
                "problem": "If f(x) = x² and g(x) = 2x + 1, find f(g(x)).",
                "answer": "4x² + 4x + 1",
                "explanation": "1. f(g(x)) = f(2x + 1)\n2. f(2x + 1) = (2x + 1)²\n3. (2x + 1)² = 4x² + 4x + 1",
                "hint": "Substitute g(x) into f(x)."
            }
        })
        
        # Applications in Real Life
        self.create_formula_card(scrollable_frame, {
            "title": "Applications in Real Life",
            "formula": "Various applications of functions in different fields",
            "explanation": "Functions are used to model real-world phenomena in various fields.",
            "steps": [
                "Physics: Motion and forces",
                "Economics: Supply and demand",
                "Biology: Population growth",
                "Engineering: Signal processing",
                "Computer Science: Algorithms and data structures"
            ],
            "practice": {
                "problem": "A ball is thrown upward with an initial velocity of 20 m/s. The height h(t) in meters after t seconds is given by h(t) = -5t² + 20t. Find the maximum height reached by the ball.",
                "answer": "20",
                "explanation": "1. The maximum height occurs at the vertex of the parabola\n2. t = -b/(2a) = -20/(2(-5)) = 2 seconds\n3. h(2) = -5(2)² + 20(2) = -20 + 40 = 20 meters",
                "hint": "Find the vertex of the quadratic function to determine the maximum height."
            }
        })

    def show_feedback(self, message, is_error=False):
        """Display feedback to the user"""
        feedback_label = ttk.Label(self.main_frame, 
                                  text=message, 
                                  style='Error.TLabel' if is_error else 'Subtitle.TLabel')
        feedback_label.pack(pady=10)
        self.root.after(3000, feedback_label.destroy)

    def validate_input(self, input_value, expected_type):
        """Validate user input"""
        try:
            if expected_type == 'number':
                return float(input_value)
            elif expected_type == 'integer':
                return int(input_value)
            else:
                return input_value
        except ValueError:
            self.show_feedback("Invalid input. Please try again.", is_error=True)
            return None

    def setup_accessibility(self):
        """Set up accessibility features"""
        # Keyboard shortcuts
        self.root.bind('<Control-s>', lambda event: self.save_notes(self.scrap_work_area.get("1.0", tk.END)))
        self.root.bind('<Control-q>', lambda event: self.root.quit())
        
        # Screen reader support
        for widget in self.root.winfo_children():
            if isinstance(widget, (ttk.Button, ttk.Label, ttk.Entry)):
                widget.configure(style='Accessible.TButton' if isinstance(widget, ttk.Button) else 'Accessible.TLabel')

    def finalize_application(self):
        """Finalize the application setup"""
        # Ensure all widgets are properly configured
        self.setup_accessibility()
        
        # Set window title and icon
        self.root.title("Formula Finder")
        # self.root.iconbitmap('path/to/icon.ico')  # Uncomment and set path to your icon
        
        # Center the window on the screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Start the application
        self.run()

    def run(self):
        """Run the application"""
        self.root.mainloop()

    def show_help(self):
        """Display help information to the user"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="Help & Support", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Help frame
        help_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        help_frame.pack(fill=tk.X, pady=10, padx=20)
        
        # Help content
        help_text = """
        Welcome to Formula Finder!
        
        This application helps you learn and practice various mathematical formulas.
        
        Navigation:
        - Use the back button to return to the previous screen.
        - Use the navigation bar to access different sections and features.
        
        Features:
        - View detailed explanations and practice problems for each formula.
        - Use the calculator for quick calculations.
        - Take notes in the scrap work area.
        - Track your progress and take practice tests.
        
        Keyboard Shortcuts:
        - Ctrl + S: Save notes
        - Ctrl + Q: Quit the application
        
        For more information, please refer to the user guide.
        """
        
        ttk.Label(help_frame, 
                 text=help_text, 
                 style='Subtitle.TLabel',
                 wraplength=600).pack(pady=10)
        
        # Contact support button
        ttk.Button(help_frame, 
                  text="Contact Support", 
                  command=self.contact_support,
                  style='Category.TButton').pack(pady=10)
    
    def contact_support(self):
        """Contact support via email"""
        try:
            # Support email
            email = "support@formulafinder.com"
            subject = "Formula Finder Support Request"
            body = "Please describe your issue or question here."
            
            # Create mailto link
            mailto_link = f"mailto:{email}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
            
            # Open default email client
            webbrowser.open(mailto_link)
            
            self.show_feedback("Opening email client...")
        except Exception as e:
            self.show_feedback(f"Error opening email client: {str(e)}", is_error=True)

    def show_settings(self):
        """Display settings menu to the user"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="Settings", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Settings frame
        settings_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        settings_frame.pack(fill=tk.X, pady=10, padx=20)
        
        # Theme selection
        ttk.Label(settings_frame, 
                 text="Theme:", 
                 style='Subtitle.TLabel').pack(pady=5)
        
        theme_var = tk.StringVar(value="light")
        theme_frame = ttk.Frame(settings_frame)
        theme_frame.pack(fill=tk.X, pady=5)
        
        ttk.Radiobutton(theme_frame, 
                        text="Light", 
                        variable=theme_var, 
                        value="light",
                        command=lambda: self.change_theme("light")).pack(side=tk.LEFT, padx=5)
        
        ttk.Radiobutton(theme_frame, 
                        text="Dark", 
                        variable=theme_var, 
                        value="dark",
                        command=lambda: self.change_theme("dark")).pack(side=tk.LEFT, padx=5)
        
        # Font size selection
        ttk.Label(settings_frame, 
                 text="Font Size:", 
                 style='Subtitle.TLabel').pack(pady=5)
        
        font_size_var = tk.StringVar(value="medium")
        font_size_frame = ttk.Frame(settings_frame)
        font_size_frame.pack(fill=tk.X, pady=5)
        
        ttk.Radiobutton(font_size_frame, 
                        text="Small", 
                        variable=font_size_var, 
                        value="small",
                        command=lambda: self.change_font_size("small")).pack(side=tk.LEFT, padx=5)
        
        ttk.Radiobutton(font_size_frame, 
                        text="Medium", 
                        variable=font_size_var, 
                        value="medium",
                        command=lambda: self.change_font_size("medium")).pack(side=tk.LEFT, padx=5)
        
        ttk.Radiobutton(font_size_frame, 
                        text="Large", 
                        variable=font_size_var, 
                        value="large",
                        command=lambda: self.change_font_size("large")).pack(side=tk.LEFT, padx=5)
        
        # Save settings button
        ttk.Button(settings_frame, 
                  text="Save Settings", 
                  command=self.save_settings,
                  style='Category.TButton').pack(pady=10)
        
    def change_theme(self, theme):
        """Change the application theme"""
        # Update user settings
        self.user_data['settings']['theme'] = theme
        
        # Update styles
        self.setup_styles()
        
        # Update all existing widgets
        for widget in self.main_frame.winfo_children():
            if isinstance(widget, ttk.Frame):
                widget.configure(style='Card.TFrame')
            elif isinstance(widget, ttk.Label):
                widget.configure(style='Subtitle.TLabel')
            elif isinstance(widget, ttk.Button):
                widget.configure(style='Category.TButton')
            elif isinstance(widget, ttk.Entry):
                widget.configure(style='TEntry')
            elif isinstance(widget, ttk.Radiobutton):
                widget.configure(style='TRadiobutton')
        
        # Update root window background
        self.root.configure(bg=self.user_data['settings']['theme'] == 'dark' and '#1a1a1a' or '#ffffff')
        
        # Save settings
        self.save_user_data()
    
    def change_font_size(self, size):
        """Change the application font size"""
        if size == "small":
            self.font_sizes = {
                'title': 16,
                'subtitle': 14,
                'normal': 12,
                'small': 10
            }
        elif size == "medium":
            self.font_sizes = {
                'title': 20,
                'subtitle': 16,
                'normal': 14,
                'small': 12
            }
        else:  # large
            self.font_sizes = {
                'title': 24,
                'subtitle': 20,
                'normal': 16,
                'small': 14
            }
        
        # Update all widget styles
        self.setup_styles()
        
        # Update all existing widgets
        for widget in self.main_frame.winfo_children():
            if isinstance(widget, ttk.Label):
                if 'Title' in str(widget.cget('style')):
                    widget.configure(font=('Arial', self.font_sizes['title']))
                elif 'Subtitle' in str(widget.cget('style')):
                    widget.configure(font=('Arial', self.font_sizes['subtitle']))
                else:
                    widget.configure(font=('Arial', self.font_sizes['normal']))
    
    def save_settings(self):
        """Save user settings"""
        self.settings['theme'] = self.theme_var.get()
        self.settings['font_size'] = self.font_size_var.get()
        self.save_user_data()
        self.show_feedback("Settings saved successfully.")
    
    def load_user_data(self):
        """Load user data from file"""
        try:
            if os.path.exists('user_data.json'):
                with open('user_data.json', 'r') as f:
                    data = json.load(f)
                    # Update only if keys exist in loaded data
                    for key in data:
                        if key in self.user_data:
                            self.user_data[key] = data[key]
        except Exception as e:
            print(f"Error loading user data: {e}")
            # Keep default values if loading fails

    def save_user_data(self):
        """Save user data to file"""
        try:
            with open('user_data.json', 'w') as f:
                json.dump(self.user_data, f, indent=4)
        except Exception as e:
            print(f"Error saving user data: {e}")
    
    def update_progress(self, section, problem, score):
        """Update user progress"""
        if section not in self.user_progress:
            self.user_progress[section] = {
                'completed_problems': [],
                'scores': [],
                'last_attempt': None,
                'favorite_formulas': []
            }
        
        # Check if problem was already completed
        if problem not in self.user_progress[section]['completed_problems']:
            self.user_progress[section]['completed_problems'].append(problem)
            self.user_progress[section]['scores'].append(score)
            self.user_progress[section]['last_attempt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Calculate and show average score
            avg_score = sum(self.user_progress[section]['scores']) / len(self.user_progress[section]['scores'])
            self.show_feedback(f"Problem completed! Average score: {avg_score:.1f}")
            
            self.save_user_data()
        else:
            self.show_feedback("This problem was already completed.", is_error=True)
    
    def add_favorite_formula(self, section, formula):
        """Add a formula to favorites"""
        if section not in self.user_progress:
            self.user_progress[section] = {
                'completed_problems': [],
                'scores': [],
                'last_attempt': None,
                'favorite_formulas': []
            }
        
        if formula not in self.user_progress[section]['favorite_formulas']:
            self.user_progress[section]['favorite_formulas'].append(formula)
            self.save_user_data()
            self.show_feedback(f"{formula} added to favorites.")
    
    def remove_favorite_formula(self, section, formula):
        """Remove a formula from favorites"""
        if section in self.user_progress and formula in self.user_progress[section]['favorite_formulas']:
            self.user_progress[section]['favorite_formulas'].remove(formula)
            self.save_user_data()
            self.show_feedback(f"{formula} removed from favorites.")

    def show_search(self):
        """Display search interface to the user"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="Search Formulas", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Search frame
        search_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        search_frame.pack(fill=tk.X, pady=10, padx=20)
        
        # Search entry
        search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, 
                               textvariable=search_var, 
                               font=('Arial', 12))
        search_entry.pack(fill=tk.X, pady=5)
        
        # Search button
        ttk.Button(search_frame, 
                  text="Search", 
                  command=lambda: self.perform_search(search_var.get()),
                  style='Category.TButton').pack(pady=5)
        
        # Results frame
        self.results_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        self.results_frame.pack(fill=tk.X, pady=10, padx=20)
    
    def perform_search(self, query):
        """Perform search and display results"""
        # Clear previous results
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        
        if not query:
            self.show_feedback("Please enter a search query.", is_error=True)
            return
        
        # Search through all sections
        found_results = False
        for section in self.formula_db.get_all_sections():
            formulas = self.formula_db.get_section_formulas(section)
            for formula_name, formula_info in formulas.items():
                # Search in title, formula, description, and usage
                searchable_text = f"{formula_name} {formula_info['formula']} {formula_info['description']} {formula_info['usage']}"
                if query.lower() in searchable_text.lower():
                    found_results = True
                    result_frame = ttk.Frame(self.results_frame, style='Card.TFrame')
                    result_frame.pack(fill=tk.X, pady=5)
                    
                    ttk.Label(result_frame, 
                             text=formula_name, 
                             style='Subtitle.TLabel').pack(pady=2)
                    
                    ttk.Label(result_frame, 
                             text=formula_info['formula'], 
                             style='Subtitle.TLabel').pack(pady=2)
                    
                    ttk.Button(result_frame, 
                              text="View Details", 
                              command=lambda s=section, f=formula_name: self.show_formula_details(s, f),
                              style='Category.TButton').pack(pady=2)
        
        if not found_results:
            self.show_feedback("No results found.", is_error=True)
    
    def show_formula_details(self, section, formula_name):
        """Show detailed information for a specific formula"""
        formula_info = self.formula_db.get_formula(section, formula_name)
        if formula_info:
            self.clear_main_frame()
            
            # Back button
            back_button = ttk.Button(self.main_frame, 
                                   text="← Back to Section", 
                                   command=lambda: self.show_section(section),
                                   style='Category.TButton')
            back_button.pack(anchor='w', pady=10, padx=20)
            
            # Title
            title_label = ttk.Label(self.main_frame, 
                                  text=formula_name, 
                                  style='Subtitle.TLabel')
            title_label.pack(pady=20)
            
            # Details frame
            details_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
            details_frame.pack(fill=tk.X, pady=10, padx=20)
            
            # Formula
            ttk.Label(details_frame, 
                     text=f"Formula: {formula_info['formula']}", 
                     style='Subtitle.TLabel').pack(pady=5)
            
            # Description
            ttk.Label(details_frame, 
                     text=f"Description: {formula_info['description']}", 
                     style='Subtitle.TLabel').pack(pady=5)
            
            # Example
            ttk.Label(details_frame, 
                     text=f"Example: {formula_info['example']}", 
                     style='Subtitle.TLabel').pack(pady=5)
            
            # Usage
            ttk.Label(details_frame, 
                     text=f"Usage: {formula_info['usage']}", 
                     style='Subtitle.TLabel').pack(pady=5)
            
            # Practice Problems
            practice_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
            practice_frame.pack(fill=tk.X, pady=10, padx=20)
            
            ttk.Label(practice_frame, 
                     text="Practice Problems", 
                     style='Subtitle.TLabel').pack(pady=5)
            
            problems = self.formula_db.get_practice_problems(section, formula_name)
            for i, problem in enumerate(problems, 1):
                problem_frame = ttk.Frame(practice_frame, style='Card.TFrame')
                problem_frame.pack(fill=tk.X, pady=5, padx=10)
                
                # Problem number and question
                ttk.Label(problem_frame, 
                         text=f"Problem {i}: {problem['question']}", 
                         style='Subtitle.TLabel').pack(pady=5)
                
                # Answer entry
                answer_var = tk.StringVar()
                answer_entry = ttk.Entry(problem_frame, 
                                       textvariable=answer_var,
                                       font=('Arial', self.font_sizes['normal']))
                answer_entry.pack(fill=tk.X, pady=5)
                
                # Buttons frame
                buttons_frame = ttk.Frame(problem_frame)
                buttons_frame.pack(fill=tk.X, pady=5)
                
                # Hint button
                ttk.Button(buttons_frame, 
                          text="Show Hint", 
                          command=lambda p=problem: self.show_hint(p),
                          style='Category.TButton').pack(side=tk.LEFT, padx=5)
                
                # Check answer button
                ttk.Button(buttons_frame, 
                          text="Check Answer", 
                          command=lambda p=problem, a=answer_var: self.check_single_answer(p, a.get()),
                          style='Category.TButton').pack(side=tk.LEFT, padx=5)
                
                # Add a separator between problems
                ttk.Separator(problem_frame, orient='horizontal').pack(fill=tk.X, pady=5)
            
            # Add calculator and scrap work area
            self.create_calculator(self.main_frame)
            self.create_scrap_work_area(self.main_frame)

    def check_single_answer(self, problem, answer):
        """Check a single practice problem answer"""
        if answer.lower() == problem['answer'].lower():
            self.show_feedback("Correct! Well done.")
            # Update progress
            self.update_progress(problem.get('formula_name', ''), problem['question'], 1)
        else:
            self.show_feedback(f"Incorrect. The correct answer is: {problem['answer']}", is_error=True)
            # Update progress
            self.update_progress(problem.get('formula_name', ''), problem['question'], 0)

    def show_hint(self, problem):
        """Show hint for a practice problem"""
        hint_window = tk.Toplevel(self.root)
        hint_window.title("Hint")
        hint_window.geometry("400x200")
        
        # Center the window
        hint_window.transient(self.root)
        hint_window.grab_set()
        
        # Hint content
        ttk.Label(hint_window, 
                 text="Hint:", 
                 style='Subtitle.TLabel').pack(pady=10)
        
        ttk.Label(hint_window, 
                 text=problem['hint'], 
                 style='Subtitle.TLabel',
                 wraplength=350).pack(pady=10)
        
        # Close button
        ttk.Button(hint_window, 
                  text="Close", 
                  command=hint_window.destroy,
                  style='Category.TButton').pack(pady=10)

    def show_progress(self):
        """Display overall progress to the user"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="Learning Progress", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Progress frame
        progress_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        progress_frame.pack(fill=tk.X, pady=10, padx=20)
        
        # Overall progress
        ttk.Label(progress_frame, 
                 text="Overall Progress", 
                 style='Subtitle.TLabel').pack(pady=5)
        
        total_problems = sum(len(section['completed_problems']) for section in self.user_progress.values())
        total_sections = len(self.user_progress)
        
        ttk.Label(progress_frame, 
                 text=f"Total Problems Completed: {total_problems}", 
                 style='Subtitle.TLabel').pack(pady=5)
        
        ttk.Label(progress_frame, 
                 text=f"Total Sections: {total_sections}", 
                 style='Subtitle.TLabel').pack(pady=5)
        
        # Section progress
        ttk.Label(progress_frame, 
                 text="Section Progress", 
                 style='Subtitle.TLabel').pack(pady=5)
        
        for section, data in self.user_progress.items():
            ttk.Label(progress_frame, 
                     text=f"{section}: {len(data['completed_problems'])} problems completed", 
                     style='Subtitle.TLabel').pack(pady=5)
            
            if data['scores']:
                average_score = sum(data['scores']) / len(data['scores'])
                ttk.Label(progress_frame, 
                         text=f"Average Score: {average_score:.2f}%", 
                         style='Subtitle.TLabel').pack(pady=5)
            
            ttk.Label(progress_frame, 
                     text=f"Last Attempt: {data['last_attempt']}", 
                     style='Subtitle.TLabel').pack(pady=5)
            
            ttk.Label(progress_frame, 
                     text=f"Favorite Formulas: {', '.join(data['favorite_formulas'])}", 
                     style='Subtitle.TLabel').pack(pady=5)

    def show_profile(self):
        """Display user profile to the user"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="User Profile", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Profile frame
        profile_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        profile_frame.pack(fill=tk.X, pady=10, padx=20)
        
        # User information
        ttk.Label(profile_frame, 
                 text="User Information", 
                 style='Subtitle.TLabel').pack(pady=5)
        
        # Example user information (replace with actual user data)
        user_info = {
            "Name": "John Doe",
            "Email": "john.doe@example.com",
            "Join Date": "2023-01-01"
        }
        
        for key, value in user_info.items():
            ttk.Label(profile_frame, 
                     text=f"{key}: {value}", 
                     style='Subtitle.TLabel').pack(pady=5)
        
        # Edit profile button
        ttk.Button(profile_frame, 
                  text="Edit Profile", 
                  command=self.edit_profile,
                  style='Category.TButton').pack(pady=10)
    
    def edit_profile(self):
        """Edit user profile"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Profile", 
                               command=self.show_profile,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="Edit Profile", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Edit frame
        edit_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        edit_frame.pack(fill=tk.X, pady=10, padx=20)
        
        # Name
        ttk.Label(edit_frame, 
                 text="Name:", 
                 style='Subtitle.TLabel').pack(pady=5)
        name_entry = ttk.Entry(edit_frame, font=('Arial', 12))
        name_entry.pack(fill=tk.X, pady=5)
        name_entry.insert(0, self.user_profile.get('name', ''))
        
        # Email
        ttk.Label(edit_frame, 
                 text="Email:", 
                 style='Subtitle.TLabel').pack(pady=5)
        email_entry = ttk.Entry(edit_frame, font=('Arial', 12))
        email_entry.pack(fill=tk.X, pady=5)
        email_entry.insert(0, self.user_profile.get('email', ''))
        
        # Save button
        ttk.Button(edit_frame, 
                  text="Save Changes", 
                  command=lambda: self.save_profile(name_entry.get(), email_entry.get()),
                  style='Category.TButton').pack(pady=10)

    def save_profile(self, name, email):
        """Save user profile changes"""
        if not name or not email:
            self.show_feedback("Please fill in all fields.", is_error=True)
            return
        
        try:
            self.user_profile.update({
                'name': name,
                'email': email,
                'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
            # Save to user data
            self.save_user_data()
            
            self.show_feedback("Profile updated successfully!")
            self.show_profile()  # Return to profile view
        except Exception as e:
            self.show_feedback(f"Error updating profile: {str(e)}", is_error=True)

    def show_notifications(self):
        """Display notifications to the user"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="Notifications", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Notifications frame
        notifications_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        notifications_frame.pack(fill=tk.X, pady=10, padx=20)
        
        # Get notifications from user data
        notifications = self.user_data.get('notifications', [])
        
        if notifications:
            for notification in notifications:
                notification_frame = ttk.Frame(notifications_frame, style='Card.TFrame')
                notification_frame.pack(fill=tk.X, pady=5)
                
                # Notification content
                ttk.Label(notification_frame, 
                         text=notification['message'], 
                         style='Subtitle.TLabel').pack(side=tk.LEFT, pady=5, padx=5)
                
                # Timestamp
                ttk.Label(notification_frame, 
                         text=notification['timestamp'], 
                         style='Small.TLabel').pack(side=tk.RIGHT, pady=5, padx=5)
        else:
            ttk.Label(notifications_frame, 
                     text="No notifications", 
                     style='Subtitle.TLabel').pack(pady=10)
        
        # Clear notifications button
        ttk.Button(notifications_frame, 
                  text="Clear Notifications", 
                  command=self.clear_notifications,
                  style='Category.TButton').pack(pady=10)

    def clear_notifications(self):
        """Clear all notifications"""
        try:
            self.user_data['notifications'] = []
            self.save_user_data()
            self.show_feedback("Notifications cleared.")
            self.show_notifications()  # Refresh notifications view
        except Exception as e:
            self.show_feedback(f"Error clearing notifications: {str(e)}", is_error=True)

    def add_notification(self, message):
        """Add a new notification"""
        if 'notifications' not in self.user_data:
            self.user_data['notifications'] = []
        
        self.user_data['notifications'].append({
            'message': message,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        # Keep only the last 10 notifications
        self.user_data['notifications'] = self.user_data['notifications'][-10:]
        
        self.save_user_data()

    def show_feedback_form(self):
        """Display feedback form to the user"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="Feedback", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Feedback frame
        feedback_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        feedback_frame.pack(fill=tk.X, pady=10, padx=20)
        
        # Feedback type
        ttk.Label(feedback_frame, 
                 text="Feedback Type:", 
                 style='Subtitle.TLabel').pack(pady=5)
        
        feedback_type = tk.StringVar(value="suggestion")
        type_frame = ttk.Frame(feedback_frame)
        type_frame.pack(fill=tk.X, pady=5)
        
        types = [
            ("Suggestion", "suggestion"),
            ("Bug Report", "bug"),
            ("Feature Request", "feature"),
            ("Other", "other")
        ]
        
        for text, value in types:
            ttk.Radiobutton(type_frame, 
                           text=text, 
                           variable=feedback_type, 
                           value=value).pack(side=tk.LEFT, padx=5)
        
        # Message
        ttk.Label(feedback_frame, 
                 text="Message:", 
                 style='Subtitle.TLabel').pack(pady=5)
        
        message_text = tk.Text(feedback_frame, 
                              height=10, 
                              width=50, 
                              font=('Arial', 12))
        message_text.pack(fill=tk.X, pady=5)
        
        # Submit button
        ttk.Button(feedback_frame, 
                  text="Submit Feedback", 
                  command=lambda: self.submit_feedback(feedback_type.get(), message_text.get("1.0", tk.END)),
                  style='Category.TButton').pack(pady=10)
    
    def submit_feedback(self, feedback_type, message):
        """Submit user feedback"""
        if not message.strip():
            self.show_feedback("Please enter a message.", is_error=True)
            return
        
        try:
            # Create feedback directory if it doesn't exist
            if not os.path.exists('feedback'):
                os.makedirs('feedback')
            
            # Save feedback with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"feedback/feedback_{timestamp}.txt"
            
            with open(filename, 'w') as f:
                f.write(f"Type: {feedback_type}\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Message:\n{message}")
            
            self.show_feedback("Thank you for your feedback!")
            self.show_home()  # Return to home screen
        except Exception as e:
            self.show_feedback(f"Error submitting feedback: {str(e)}", is_error=True)

    def show_user_guide(self):
        """Display user guide to the user"""
        self.clear_main_frame()
        
        # Back button
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="User Guide", 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # User guide frame
        guide_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        guide_frame.pack(fill=tk.X, pady=10, padx=20)
        
        # User guide content
        guide_text = """
        Formula Finder User Guide
        
        Introduction:
        Formula Finder is an application designed to help you learn and practice various mathematical formulas. This guide will walk you through the features and how to use them effectively.
        
        Getting Started:
        1. Navigate through the sections using the navigation bar.
        2. Each section contains detailed explanations and practice problems.
        3. Use the calculator for quick calculations and the scrap work area for notes.
        
        Features:
        - View detailed explanations and practice problems for each formula.
        - Use the calculator for quick calculations.
        - Take notes in the scrap work area.
        - Track your progress and take practice tests.
        
        Keyboard Shortcuts:
        - Ctrl + S: Save notes
        - Ctrl + Q: Quit the application
        
        For more information, please refer to the help section or contact support.
        """
        
        ttk.Label(guide_frame, 
                 text=guide_text, 
                 style='Subtitle.TLabel',
                 wraplength=600).pack(pady=10)
        
        # Download guide button
        ttk.Button(guide_frame, 
                  text="Download User Guide", 
                  command=self.download_user_guide,
                  style='Category.TButton').pack(pady=10)
    
    def download_user_guide(self):
        """Download the user guide"""
        # Implementation for downloading the user guide
        pass

    def deploy_application(self):
        """Deploy the application"""
        # Create a distribution directory
        dist_dir = "dist"
        if os.path.exists(dist_dir):
            shutil.rmtree(dist_dir)
        os.makedirs(dist_dir)
        
        # Copy necessary files to the distribution directory
        shutil.copy("formula_finder.py", dist_dir)
        shutil.copy("user_data.json", dist_dir)
        # shutil.copy("path/to/icon.ico", dist_dir)  # Uncomment and set path to your icon
        
        # Create a README file
        with open(os.path.join(dist_dir, "README.md"), "w") as f:
            f.write("""
            Formula Finder
            
            A Python application for learning and practicing mathematical formulas.
            
            Installation:
            1. Ensure Python 3.x is installed.
            2. Run 'pip install -r requirements.txt' to install dependencies.
            3. Run 'python formula_finder.py' to start the application.
            
            For more information, please refer to the user guide.
            """)
        
        # Create a requirements file
        with open(os.path.join(dist_dir, "requirements.txt"), "w") as f:
            f.write("""
            tkinter
            """)
        
        # Create a batch file for Windows
        with open(os.path.join(dist_dir, "run_formula_finder.bat"), "w") as f:
            f.write("""
            @echo off
            python formula_finder.py
            """)
        
        # Create a shell script for Unix-based systems
        with open(os.path.join(dist_dir, "run_formula_finder.sh"), "w") as f:
            f.write("""
            #!/bin/bash
            python formula_finder.py
            """)
        
        # Make the shell script executable
        os.chmod(os.path.join(dist_dir, "run_formula_finder.sh"), 0o755)
        
        # Create a zip file for distribution
        shutil.make_archive("formula_finder", "zip", dist_dir)
        
        print("Application deployed successfully. Check the 'dist' directory for the distribution files.")

    def show_section(self, section):
        """Display a specific section of formulas"""
        self.clear_main_frame()
        
        # Back button to home
        back_button = ttk.Button(self.main_frame, 
                               text="← Back to Home", 
                               command=self.show_home,
                               style='Category.TButton')
        back_button.pack(anchor='w', pady=10, padx=20)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text=section, 
                              style='Subtitle.TLabel')
        title_label.pack(pady=20)
        
        # Navigation bar
        nav_frame = ttk.Frame(self.main_frame)
        nav_frame.pack(fill=tk.X, pady=10, padx=20)
        
        ttk.Button(nav_frame, 
                  text="Section Progress", 
                  command=lambda: self.show_section_progress(section),
                  style='Category.TButton').pack(side=tk.LEFT, padx=5)
        
        ttk.Button(nav_frame, 
                  text="Practice Test", 
                  command=lambda: self.start_practice_test(section),
                  style='Category.TButton').pack(side=tk.LEFT, padx=5)
        
        # Create a scrollable frame for formulas
        canvas = tk.Canvas(self.main_frame)
        scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Get formulas for this section
        formulas = self.formula_db.get_section_formulas(section)
        
        # Display each formula
        for formula_name, formula_info in formulas.items():
            formula_frame = ttk.Frame(scrollable_frame, style='Card.TFrame')
            formula_frame.pack(fill=tk.X, pady=10, padx=20)
            
            # Formula title
            ttk.Label(formula_frame, 
                     text=formula_name, 
                     style='Subtitle.TLabel').pack(pady=5)
            
            # Formula expression
            ttk.Label(formula_frame, 
                     text=f"Formula: {formula_info['formula']}", 
                     style='Subtitle.TLabel').pack(pady=5)
            
            # View details button
            ttk.Button(formula_frame, 
                      text="View Details", 
                      command=lambda s=section, f=formula_name: self.show_formula_details(s, f),
                      style='Category.TButton').pack(pady=5)
        
        # Pack the canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True, padx=20, pady=10)
        scrollbar.pack(side="right", fill="y")
        
        # Add calculator and scrap work area
        self.create_calculator(self.main_frame)
        self.create_scrap_work_area(self.main_frame)

    def setup_styles(self):
        """Set up application styles"""
        style = ttk.Style()
        
        # Get current theme
        is_dark = self.user_data.get('settings', {}).get('theme', 'light') == 'dark'
        
        # Define colors based on theme
        if is_dark:
            bg_color = '#1a1a1a'
            fg_color = '#ffffff'  # White text for dark mode
            accent_color = '#0d6efd'
            card_bg = '#2d2d2d'
            error_color = '#ff6b6b'  # Brighter red for dark mode
            success_color = '#51cf66'  # Brighter green for dark mode
            text_color = '#ffffff'  # White text for dark mode
        else:
            bg_color = '#ffffff'
            fg_color = '#000000'
            accent_color = '#007bff'
            card_bg = '#f8f9fa'
            error_color = '#dc3545'
            success_color = '#28a745'
            text_color = '#000000'  # Black text for light mode
        
        # Configure styles
        style.configure('Title.TLabel', 
                       font=('Arial', self.font_sizes['title'], 'bold'),
                       foreground=text_color,  # Use text_color instead of fg_color
                       background=bg_color)
        
        style.configure('Subtitle.TLabel', 
                       font=('Arial', self.font_sizes['subtitle']),
                       foreground=text_color,  # Use text_color instead of fg_color
                       background=bg_color)
        
        style.configure('Category.TButton', 
                       font=('Arial', self.font_sizes['normal']),
                       background=accent_color,
                       foreground=fg_color)
        
        style.configure('Card.TFrame', 
                       background=card_bg,
                       relief=tk.RAISED,
                       borderwidth=1)
        
        style.configure('Main.TFrame',
                       background=bg_color)
        
        style.configure('Error.TLabel',
                       foreground=error_color,
                       background=bg_color)
        
        style.configure('Success.TLabel',
                       foreground=success_color,
                       background=bg_color)
        
        # Configure hover effects for buttons
        style.map('Category.TButton',
                  background=[('active', accent_color)],
                  foreground=[('active', fg_color)])
        
        # Configure entry styles
        style.configure('TEntry',
                       fieldbackground=card_bg,
                       foreground=fg_color,
                       insertcolor=fg_color)
        
        # Configure scrollbar styles
        style.configure('TScrollbar',
                       background=accent_color,
                       troughcolor=card_bg,
                       width=12)
        
        # Configure radiobutton styles
        style.configure('TRadiobutton',
                       background=bg_color,
                       foreground=fg_color)
        
        # Configure canvas background
        self.root.configure(bg=bg_color)
        
        # Update main frame background
        self.main_frame.configure(style='Main.TFrame')

    def check_notifications(self):
        """Check for new notifications"""
        # Example notification triggers
        if self.user_data.get('last_login'):
            last_login = datetime.strptime(self.user_data['last_login'], "%Y-%m-%d %H:%M:%S")
            if (datetime.now() - last_login).days >= 1:
                self.add_notification("Welcome back! Continue your learning journey.")
        
        # Check for completed sections
        for section, data in self.user_progress.items():
            if len(data['completed_problems']) >= 10:
                self.add_notification(f"Congratulations! You've completed 10 problems in {section}.")
        
        # Check for new formulas
        if self.formula_db.has_new_formulas():
            self.add_notification("New formulas have been added to the database.")

    def show_test_results(self):
        """Show the results of the practice test"""
        # Clear main frame
        self.clear_main_frame()
        
        # Create main content frame
        content_frame = ttk.Frame(self.main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = ttk.Label(content_frame, 
                              text="Test Results", 
                              style='Title.TLabel')
        title_label.pack(pady=20)
        
        # Results frame
        results_frame = ttk.Frame(content_frame, style='Card.TFrame')
        results_frame.pack(fill=tk.X, pady=10)
        
        # Score
        score = self.current_test['score']
        total = len(self.current_test['questions'])
        percentage = (score / total) * 100
        
        # Score display
        score_label = ttk.Label(results_frame, 
                              text=f"Score: {score}/{total} ({percentage:.1f}%)", 
                              style='Title.TLabel')
        score_label.pack(pady=10)
        
        # Performance message
        if percentage >= 90:
            message = "Excellent work! You've mastered this section!"
        elif percentage >= 70:
            message = "Good job! Keep practicing to improve further."
        else:
            message = "Keep practicing! You'll get better with time."
        
        message_label = ttk.Label(results_frame, 
                                text=message,
                                style='Subtitle.TLabel')
        message_label.pack(pady=5)
        
        # Review answers
        review_frame = ttk.LabelFrame(content_frame, text="Review Answers", style='Card.TFrame')
        review_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Create canvas for review
        review_canvas = tk.Canvas(review_frame)
        review_scrollbar = ttk.Scrollbar(review_frame, orient="vertical", command=review_canvas.yview)
        review_content = ttk.Frame(review_canvas)
        
        review_canvas.configure(yscrollcommand=review_scrollbar.set)
        
        # Pack review elements
        review_scrollbar.pack(side="right", fill="y")
        review_canvas.pack(side="left", fill="both", expand=True)
        
        review_canvas.create_window((0, 0), window=review_content, anchor="nw", width=review_canvas.winfo_width())
        
        # Add each answer to review
        for i, answer in enumerate(self.current_test['answers'], 1):
            answer_frame = ttk.Frame(review_content, style='Card.TFrame')
            answer_frame.pack(fill=tk.X, pady=5, padx=5)
            
            # Question number
            ttk.Label(answer_frame, 
                     text=f"Question {i}:",
                     style='Subtitle.TLabel').pack(anchor='w', pady=2)
            
            # Question text
            ttk.Label(answer_frame, 
                     text=answer['question'],
                     style='Subtitle.TLabel',
                     wraplength=600).pack(anchor='w', pady=2)
            
            # User's answer
            ttk.Label(answer_frame, 
                     text=f"Your answer: {answer['answer']}",
                     style='Subtitle.TLabel').pack(anchor='w', pady=2)
            
            # Correct answer
            ttk.Label(answer_frame, 
                     text=f"Correct answer: {answer['correct']}",
                     style='Subtitle.TLabel').pack(anchor='w', pady=2)
            
            # Add separator
            ttk.Separator(answer_frame, orient='horizontal').pack(fill=tk.X, pady=5)
        
        # Buttons frame
        buttons_frame = ttk.Frame(content_frame)
        buttons_frame.pack(pady=20)
        
        # Retry button
        ttk.Button(buttons_frame, 
                  text="Retry Test", 
                  command=lambda: self.start_practice_test(self.current_test['section']),
                  style='Category.TButton').pack(side=tk.LEFT, padx=5)
        
        # Back to section button
        ttk.Button(buttons_frame, 
                  text="Back to Section", 
                  command=lambda: self.show_section(self.current_test['section']),
                  style='Category.TButton').pack(side=tk.LEFT, padx=5)
        
        # Update scroll region when content changes
        def update_review_scroll(event):
            review_canvas.configure(scrollregion=review_canvas.bbox("all"))
        
        review_content.bind('<Configure>', update_review_scroll)
        
        # Bind mouse wheel to scroll
        def _on_review_mousewheel(event):
            review_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        review_canvas.bind_all("<MouseWheel>", _on_review_mousewheel)

    def save_current_notes(self):
        """Save notes before moving to next question"""
        if hasattr(self, 'current_notes_widget'):
            notes = self.current_notes_widget.get("1.0", tk.END)
            self.save_notes(notes)

    def skip_question(self, question):
        """Replace the current question with a different one from the remaining questions"""
        # Save current notes before changing question
        self.save_current_notes()
        
        # Get the current question index
        current_index = self.current_test['current_question']
        
        # Get all remaining questions (excluding the current one)
        remaining_questions = self.current_test['questions'][current_index + 1:]
        
        if remaining_questions:
            # Randomly select a new question from remaining questions
            new_question = random.choice(remaining_questions)
            
            # Remove the selected question from remaining questions
            remaining_questions.remove(new_question)
            
            # Replace the current question with the new one
            self.current_test['questions'][current_index] = new_question
            
            # Update the question text
            self.question_text_label.configure(text=new_question['question'])
            
            # Clear the answer entry
            self.answer_var.set("")
            self.answer_entry.focus_set()
        else:
            # If no more questions, show end button
            self.show_end_button()

    def show_end_button(self):
        """Show the end button when all questions are done"""
        # Create end button frame
        end_frame = ttk.Frame(self.main_frame)
        end_frame.pack(pady=20)
        
        # End button
        ttk.Button(end_frame,
                  text="End Practice",
                  command=self.show_home,  # This will return to the main screen
                  style='Category.TButton').pack(pady=10)
        
        # Disable the answer entry and buttons
        self.answer_entry.configure(state='disabled')
        for widget in self.main_frame.winfo_children():
            if isinstance(widget, ttk.Frame):
                for child in widget.winfo_children():
                    if isinstance(child, ttk.Button):
                        child.configure(state='disabled')

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FormulaFinder(root)
    app.run()




