stats = {
    "energy": 50,
    "hunger": 50,
    "happiness": 50
}
action_history = []

def show_status():
    print(f"\n--- STATUS ---")
    print(f"Energy: {stats['energy']}")
    print(f"Hunger: {stats['hunger']}")
    # ... etc

def feed_creature():
    print("You feed the creature...")
    stats['hunger'] -= 10 # This is how we access and modify the stats dictionary, stats is a dictionary, and we can access its values using keys like 'hunger' and 'energy'
    stats['energy'] += 5
    action_history.append("Fed creature")

# 2. Main Game Loop
while True:
    show_status()
    print("1. Feed")
    print("2. Sleep")
    print("3. View History")
    print("4. Quit")
    
    choice = input("Choose an action: ")
    
    # 3. Logic
    if choice == "1":
        feed_creature()
    elif choice == "2":
        # Call sleep function
        pass # These are placeholders for you to implement actions you want to add
    elif choice == "3":
        # Print action_history using a loop, unless you want to implement undo functionality, in which case you can pop from the list and reverse the effects of the last action
        pass # These are placeholders for you to implement actions you want to add
    elif choice == "4":
        pass # These are placeholders for you to implement actions you want to add
    
    # 4. Game Over check
    if stats['hunger'] >= 100:
        print("Your creature starved! Game Over.")
        break