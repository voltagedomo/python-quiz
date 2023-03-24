# Create a Quiz Assignment by Alexander Alkin

# Variable to count score
score = 0

# Main Menu / Input + Process
print("\nWELCOME TO THE CAR QUIZ")
print("\nWhat company is Maybach a part of?")
# Get input from user and make it case insensitive
q1_input = input("Q1 Answer: ").lower()
# Print correct / incorrect depending on input and if correct increase score
if q1_input == "mercedes" or q1_input == "mercedes-benz":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("\nWhat company created the Firebird?")
q2_input = input("Q2 Answer: ").lower()
if q2_input == "pontiac":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("\nWhat company did Adolf Hitler endorse?")
q3_input = input("Q3 Answer: ").lower()
if q3_input == "volkswagen" or q3_input == "vw":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("\nWhat the most expensive Lamborghini? (non-concept)")
q4_input = input("Q4 Answer: ").lower()
if q4_input == "veneno":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Process (Calculate score)
percentage = int(score / 4 * 100)

# Output score and feedback based on score
if score == 4:
    feedback = "Perfect!"
elif score == 3:
    feedback = "Good Job"
elif score == 2:
    feedback = "Try Harder"
elif score == 1:
    feedback = "Nice Try"
else: 
    feedback = "Get some more KNOWLEDGE and come back"
print("\nYOUR RESULTS: \n" + str(score), "/", "4 (" + str(percentage) + "%)\n" + feedback) 
# THINGS TO FIX:
# HAS TO BE 
