# Mamoun Mohamed
# 18/11/2024
# Program to build story from random data adjectives, nouns, verbs.

import random

def get_input(prompt):
    """Prompt the user for input and return the response."""
    return input(prompt).strip()

def story_one(name, place, animal, adjective, verb):
    """Generates the first story template."""
    return f"""
    One day, {name} went to {place}. There, {name} found a {adjective} {animal} that loved to {verb}.
    Together, they became the best of friends and had the most unforgettable day at {place}.
    """

def story_two(job, name, food, verb, place):
    """Generates the second story template."""
    return f"""
    Once upon a time, there was a famous {job} named {name}. 
    Every day, {name} dreamed of eating {food} while {verb} at {place}.
    It was {name}'s ultimate fantasy, and one day, it finally came true!
    """

def story_three(hero, sidekick, place, villain, weapon):
    """Generates the third story template."""
    return f"""
    In the mystical land of {place}, the brave hero {hero} and their loyal sidekick {sidekick} 
    embarked on a quest to defeat the evil {villain}. Armed with a legendary {weapon}, 
    they fought valiantly to save the day. The people of {place} will forever remember their courage!
    """

def main():
    """Main function to run the improved Mad Libs Generator."""
    print("Welcome to the Improved Mad Libs Generator!")
    print("Choose a story template to get started:\n")
    print("1. A Day at the Park")
    print("2. The Dream of a Lifetime")
    print("3. The Epic Adventure\n")
    
    # Allow the user to select a story
    while True:
        choice = get_input("Enter the number of your chosen story (1, 2, or 3): ")
        if choice in {"1", "2", "3"}:
            break
        print("Invalid choice. Please enter 1, 2, or 3.")
    
    # Collect inputs based on the chosen story
    if choice == "1":
        name = get_input("Enter a name: ")
        place = get_input("Enter a place: ")
        animal = get_input("Enter an animal: ")
        adjective = get_input("Enter an adjective: ")
        verb = get_input("Enter a verb (present tense): ")
        story = story_one(name, place, animal, adjective, verb)
    
    elif choice == "2":
        job = get_input("Enter a job title: ")
        name = get_input("Enter a name: ")
        food = get_input("Enter a type of food: ")
        verb = get_input("Enter a verb (present tense): ")
        place = get_input("Enter a place: ")
        story = story_two(job, name, food, verb, place)
    
    else:  # choice == "3"
        hero = get_input("Enter the hero's name: ")
        sidekick = get_input("Enter the sidekick's name: ")
        place = get_input("Enter a place: ")
        villain = get_input("Enter the villain's name: ")
        weapon = get_input("Enter a weapon: ")
        story = story_three(hero, sidekick, place, villain, weapon)
    
    # Display the final story
    print("\nHere is your Mad Libs story:\n")
    print(story)

if __name__ == "__main__":
    main()


