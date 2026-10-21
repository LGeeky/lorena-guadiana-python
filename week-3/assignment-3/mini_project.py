day = input("What day is it? ").strip().lower()
time_of_day = input("What time of day? ").strip().lower()

if day == "sunday":
    if time_of_day == "morning":
        print("Suggestion: Start with a walk and a good breakfast.")
    elif time_of_day == "afternoon":
        print("Suggestion: Run errands while your energy is high.")
    elif time_of_day == "evening":
        print("Suggestion: Cook a simple dinner and relax.")
    else:
        print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening.")

elif day == "tuesday":
    if time_of_day == "morning":
        print("Suggestion: Morning Python class - great time to focus!")
    elif time_of_day == "afternoon":
        print("Suggestion: Practice pandas with a small dataset.")
    elif time_of_day == "evening":
        print("Suggestion: Review your notes, then relax with a podcast.")
    else:
        print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening.")

elif day == "saturday":
    if time_of_day == "morning":
        print("Suggestion: Visit a farmers market or go for a bike ride.")
    elif time_of_day == "afternoon":
        print("Suggestion: Meet up with friends or work on a personal project.")
    elif time_of_day == "evening":
        print("Suggestion: Perfect night for a movie or trying a new recipe.")
    else:
        print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening.")

else:
    print("Sorry, I don't recognize that day. Try: sunday, tuesday, saturday.")