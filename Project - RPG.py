print("Welcome to my own personal RPG")

admin = input("what is your name? ")

print(f"Nice to meet you {admin}!")

player_health = 100
inventory = []
enemy_health = 100

while True:
    # print that states they are walking
    continue_walking = input("Nice job you're starting to get the hang of it. to walk press w or press i to see your inventory ")
    if continue_walking == 'w':
        print("What a great day for a walk.")
    elif continue_walking == 'i':
        print(f"You have {player_health} health and {inventory} in your inventory.")
    # 3 different prints that says you ran into an enemy\
    print ("watch out there is a mud monster")
    print ("watch out there is a spider")
    print ("watch out there is a dragon ")

    # input that asks if you want to fight or run

    option = input("would you like to fight or run")



    print(f" are you sure this enemy is a lvl 10 threat {admin}")