# MacroMeter

MacroMeter is a comprehensive health and fitness tracking application that helps users monitor their nutrition, workouts, sleep, and overall wellness. The application features a modern, user-friendly interface and includes AI-powered nutrition advice.

## Features

- **User Authentication**: Secure login and registration system
- **Nutrition Tracking**: Log meals, track calories, and monitor macronutrients
- **Workout Tracking**: Record weight training and running workouts
- **Sleep Monitoring**: Track sleep duration and quality
- **AI Nutrition Assistant**: Get personalized nutrition and fitness advice
- **Guided Breathing**: Relaxation exercises with visual guidance
- **Customizable Settings**: Adjust appearance and set personal goals

## Installation

1. Clone the repository:
```bash
git clone https://github.com/chandannir/python-macroMeter.git
cd python-macroMeter
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up OpenRouter API:
   - Go to [OpenRouter](https://openrouter.ai/keys)
   - Sign up for a free account
   - Generate an API key
   - Create a `config.py` file in the project root with your API key:
   ```python
   # OpenRouter API Configuration
   # Get your API key from: https://openrouter.ai/keys
   OPENROUTER_API_KEY = "sk-or-v1-your-api-key-here"  # Replace with your OpenRouter API key
   ```
   Note: The API key should start with "sk-or-v1-" and be exactly 64 characters long.

## Usage

1. Run the application:
```bash
python macroMeter.py
```

2. Create a new account or log in with existing credentials

3. Complete your basic information:
   - Age, gender, birthdate
   - Weight and height
   - Sleep and water intake goals
   - Activity level

4. Use the navigation bar to access different features:
   - Overview: View your daily summary
   - Workout: Track your exercises
   - Nutrition: Log your meals
   - Sleep: Monitor your sleep
   - AI Chat: Get personalized advice

5. Access settings to:
   - Update your basic information
   - Change appearance mode (Dark/Light)
   - Set calorie goals
   - Customize color theme

## Requirements

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

## Troubleshooting

If you encounter any issues:

1. **API Authentication Error**:
   - Ensure your OpenRouter API key is correctly formatted
   - Check that the API key starts with "sk-or-v1-"
   - Verify the API key is exactly 64 characters long
   - Make sure there are no extra spaces in the config.py file

2. **Installation Issues**:
   - Make sure you're using Python 3.8 or higher
   - Try reinstalling the dependencies: `pip install -r requirements.txt --upgrade`
   - Check if your virtual environment is activated

3. **Application Errors**:
   - Check the console output for error messages
   - Ensure all required files are in the correct locations
   - Verify that the users.json file has proper permissions
