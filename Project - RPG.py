import random 
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
        enemy_chance = random.randint(1, 3 )
        if enemy_chance == 1:
            print("watch out there is a mud monster")
        elif enemy_chance == 2:
            print("watch out there is a spider")
        elif enemy_chance == 3:
            print("watch out there is a dragon")

            fight_option = input ("would you like to fight or run:f or r")
            if fight_option == 'f':
                print("you have chosen to fight")
                while True:
                    player_attack = random.randint(1, 10)
                    enemy_attack = random.randint(1, 10)
                    player_health = player_health - enemy_attack 
                    enemy_health = enemy_health - player_attack
                    print(f "You have{player_health} health and the enemy has {enemy_health} health") 
                    if player_health <= 0:
                        print("you have died")
                        break
                    elif enemy_health <= 0:
                        print("you have the killed the enemy")
                        break
                    
    elif continue_walking == 'i':
        print(f"You have {player_health} health and {inventory} in your inventory.")
    # 3 different prints that says you ran into an enemy\
    print ("watch out there is a mud monster")
    print ("watch out there is a spider")
    print ("watch out there is a dragon ")

    # input that asks if you want to fight or run

    option = input("would you like to fight or run")



    print(f" are you sure this enemy is a lvl 10 threat {admin}")

