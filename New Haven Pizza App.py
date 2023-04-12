# Pizza Scoring Application

# Define the scoring criteria
criteria = {
    "taste": 0.4,
    "texture": 0.3,
    "toppings": 0.2,
    "size": 0.1
}

# Define a function to calculate the total score
def calculate_score(scores):
    total_score = 0
    for key, value in scores.items():
        total_score += value * criteria[key]
    return total_score

# Define a function to prompt the user for their ratings
def prompt_user_ratings():
    taste_score = float(input("Please rate the taste of the pizza on a scale of 0 to 10: "))
    texture_score = float(input("Please rate the texture of the pizza on a scale of 0 to 10: "))
    toppings_score = float(input("Please rate the toppings of the pizza on a scale of 0 to 10: "))
    size_score = float(input("Please rate the size of the pizza on a scale of 0 to 10: "))
    return {
        "taste": taste_score / 10,
        "texture": texture_score / 10,
        "toppings": toppings_score / 10,
        "size": size_score / 10
    }

# Prompt the user for their location choice
print("Please choose a location to rate:")
print("1. Modern Apizza")
print("2. Frank Pepe's")
print("3. Sally's")
print("4. BAR")
location_choice = int(input("Enter your choice (1-4): "))

# Determine which location was chosen and prompt for ratings
if location_choice == 1:
    location_name = "Modern Apizza"
    location_scores = prompt_user_ratings()
elif location_choice == 2:
    location_name = "Frank Pepe's"
    location_scores = prompt_user_ratings()
elif location_choice == 3:
    location_name = "Sally's"
    location_scores = prompt_user_ratings()
elif location_choice == 4:
    location_name = "BAR"
    location_scores = prompt_user_ratings()
else:
    print("Invalid choice.")
    exit()

# Calculate and display the total score
total_score = calculate_score(location_scores)
print(f"\nThe total score for {location_name} is: {total_score:.2f}")
