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

4. Create a `config.py` file in the project root and add your OpenRouter API key:
```python
OPENROUTER_API_KEY = "your-api-key-here"  # Get from https://openrouter.ai/keys
```

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
   - 🏠 Overview: View your daily summary
   - 💪 Workout: Track your exercises
   - 🍎 Nutrition: Log your meals
   - 😴 Sleep: Monitor your sleep
   - 💬 AI Chat: Get personalized advice

5. Access settings to:
   - Update your basic information
   - Change appearance mode (Dark/Light)
   - Set calorie goals
   - Customize color theme

## Requirements

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 