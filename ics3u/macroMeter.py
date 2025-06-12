import pygame
import json
import hashlib
import os
from pathlib import Path

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 120, 255)
RED = (255, 0, 0)

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("MacroMeter")

# Font setup
font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 24)

class Button:
    def __init__(self, x, y, width, height, text, color=BLUE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.is_hovered = False

    def draw(self, surface):
        color = (min(self.color[0] + 30, 255), min(self.color[1] + 30, 255), min(self.color[2] + 30, 255)) if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=10)
        
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered:
                return True
        return False

class TextInput:
    def __init__(self, x, y, width, height, placeholder=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.placeholder = placeholder
        self.active = False
        self.color = GRAY

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=5)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=5)
        
        if self.text:
            text_surface = font.render(self.text, True, BLACK)
        else:
            text_surface = small_font.render(self.placeholder, True, (100, 100, 100))
        
        text_rect = text_surface.get_rect(midleft=(self.rect.x + 10, self.rect.centery))
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = WHITE if self.active else GRAY
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_user(username, password):
    users = {}
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            users = json.load(f)
    
    users[username] = hash_password(password)
    
    with open('users.json', 'w') as f:
        json.dump(users, f)

def verify_user(username, password):
    if not os.path.exists('users.json'):
        return False
    
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    return username in users and users[username] == hash_password(password)

def start_screen():
    login_button = Button(WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 - 50, 200, 50, "Login")
    register_button = Button(WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 50, 200, 50, "Register")
    
    while True:
        screen.fill(WHITE)
        
        title = font.render("MacroMeter", True, BLACK)
        screen.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 100))
        
        for button in [login_button, register_button]:
            button.draw(screen)
            if button.handle_event(pygame.event.get()):
                if button == login_button:
                    return "login"
                else:
                    return "register"
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
        
        pygame.display.flip()

def login_screen():
    username_input = TextInput(WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 - 50, 200, 40, "Username")
    password_input = TextInput(WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 10, 200, 40, "Password")
    login_button = Button(WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 70, 200, 50, "Login")
    back_button = Button(WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 140, 200, 50, "Back")
    error_text = ""
    
    while True:
        screen.fill(WHITE)
        
        title = font.render("Login", True, BLACK)
        screen.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 100))
        
        for input_field in [username_input, password_input]:
            input_field.draw(screen)
            input_field.handle_event(pygame.event.get())
        
        for button in [login_button, back_button]:
            button.draw(screen)
            if button.handle_event(pygame.event.get()):
                if button == login_button:
                    if verify_user(username_input.text, password_input.text):
                        return "main"
                    else:
                        error_text = "Invalid username or password"
                else:
                    return "start"
        
        if error_text:
            error_surface = small_font.render(error_text, True, RED)
            screen.blit(error_surface, (WINDOW_WIDTH//2 - error_surface.get_width()//2, WINDOW_HEIGHT//2 + 200))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
        
        pygame.display.flip()

def register_screen():
    username_input = TextInput(WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 - 90, 200, 40, "Username")
    password_input = TextInput(WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 - 30, 200, 40, "Password")
    confirm_input = TextInput(WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 30, 200, 40, "Confirm Password")
    register_button = Button(WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 90, 200, 50, "Register")
    back_button = Button(WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 160, 200, 50, "Back")
    error_text = ""
    
    while True:
        screen.fill(WHITE)
        
        title = font.render("Register", True, BLACK)
        screen.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 100))
        
        for input_field in [username_input, password_input, confirm_input]:
            input_field.draw(screen)
            input_field.handle_event(pygame.event.get())
        
        for button in [register_button, back_button]:
            button.draw(screen)
            if button.handle_event(pygame.event.get()):
                if button == register_button:
                    if password_input.text != confirm_input.text:
                        error_text = "Passwords do not match"
                    elif not username_input.text or not password_input.text:
                        error_text = "Please fill all fields"
                    else:
                        save_user(username_input.text, password_input.text)
                        return "login"
                else:
                    return "start"
        
        if error_text:
            error_surface = small_font.render(error_text, True, RED)
            screen.blit(error_surface, (WINDOW_WIDTH//2 - error_surface.get_width()//2, WINDOW_HEIGHT//2 + 220))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
        
        pygame.display.flip()

def main():
    current_screen = "start"
    
    while current_screen != "quit":
        if current_screen == "start":
            current_screen = start_screen()
        elif current_screen == "login":
            current_screen = login_screen()
        elif current_screen == "register":
            current_screen = register_screen()
        elif current_screen == "main":
            # TODO: Implement main menu
            pass
    
    pygame.quit()

if __name__ == "__main__":
    main()
