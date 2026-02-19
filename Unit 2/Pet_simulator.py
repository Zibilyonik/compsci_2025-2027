stats = {
    "energy": 50,
    "hunger": 50,
    "happiness": 50
}
action_history = []
if len(action_history)>5:
    action_history.pop(0)

def show_status():
    print(f"\n--- STATUS ---")
    print(f"Energy: {stats['energy']}")
    print(f"Hunger: {stats['hunger']}")
    print(f"Happiness: {stats['happiness']}")
    # ... etc

def feed_creature():
    print("You feed the creature...")
    stats['hunger'] -= 10 # This is how we access and modify the stats dictionary, stats is a dictionary, and we can access its values using keys like 'hunger' and 'energy'
    stats['energy'] += 5
    action_history.append("Fed creature")

def sleep_pet():
    print("Your pet is sleeping")
    action_history.append("Creature slept")

def history_view():
    print("History is here:\n" )
    for i in action_history:
        print(i)
    action_history.append("Viewed history")
    reve_fu=input("Do you want to reverse your last action?(y/n)")
    if reve_fu=="y":
        print("last action has been reversed")
    elif reve_fu=="n":
        print("last action was not reversed")
    else:
        print("invalid answer, run choice 3 again")



# 2. Main Game Loop
while True:
    show_status()
    print("1. Feed")
    print("2. Sleep")
    print("3. View History")
    print("4. Quit")
    
    choice = input("Choose an action: ")
    
    # 3. Logic
    if choice =="1":
        feed_creature()
    elif choice =="2":
        sleep_pet()
    elif choice =="3":
        history_view()# Print action_history using a loop, unless you want to implement undo functionality, in which case you can pop from the list and reverse the effects of the last action
         # These are placeholders for you to implement actions you want to add---pass
    elif choice =="4":
        print("quitting.....")
        break
    else:
        print("Choose a number 1-4")
            
    # 4. Game Over check
    if stats['hunger'] >= 100:
        print("Your creature starved! Game Over.")
        stats['hunger']=50
        break

    for category in stats:
        if stats[category] >= 100 and category!='hunger':
            stats[category]=100
        elif stats[category]<0 :
            stats[category]=0
        else:
            pass
        
