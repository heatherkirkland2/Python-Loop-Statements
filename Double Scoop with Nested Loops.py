# Objective: The aim of this assignment is to practice using nested loops in Python.

# Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day 
# (morning, afternoon, evening) for each day of the week. 
# Use nested loops to implement this: 
# the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. 
# For each time, randomly select a mood from a predefined list and print it. 
# Use the random module again to randomly select the mood.

# Example Outcome: 
# An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" 
# "On Wednesday morning you were tired"

import random

# List of moods
moods = ["happy", "sad", "tired", "energetic", "calm"]

# List of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# List of times of the day
times_of_day = ["morning", "afternoon", "evening"]

# Outer loop for days
for day in days:
    # Inner loop for times of the day
    for time in times_of_day:
        # Randomly select a mood
        mood = random.choice(moods)
        # Print the mood for the time of the day
        print(f"On {day} {time} you were {mood}.")

import random

# Expanded list of moods with subcategories
moods = {
    "Happy": ["joyful", "content", "thrilled"],
    "Sad": ["downcast", "mournful", "dismal"],
    "Energetic": ["lively", "vigorous", "sprightly"],
    "Calm": ["peaceful", "tranquil", "serene"]
}

# List of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# List of times of the day
times_of_day = ["morning", "afternoon", "evening"]

# Mood modifiers
modifiers = ["very", "somewhat", "a bit"]

# Outer loop for days
for day in days:
    # Inner loop for times of the day
    for time in times_of_day:
        # Randomly select a mood category and a sub-mood
        mood_category = random.choice(list(moods.keys()))
        sub_mood = random.choice(moods[mood_category])
        # Randomly decide if a modifier should be added
        modifier = random.choice(modifiers + [None])  # None for no modifier
        # Construct the mood string
        mood = f"{modifier} {sub_mood}" if modifier else sub_mood
        # Print the mood for the time of the day
        print(f"On {day} {time} you were {mood}.")
