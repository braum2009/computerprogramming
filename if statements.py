# salary = int(input("What is your salary? ") )
# years  = int(input("What is your years of service? ") ) 


# if years >= 5 :
#     print(f" Your bonus will be {salary * 0.5}")
# else:
#     print("You do not qualify for a bonus.")


# length = int(input("What is the length? "))
# width = int(input("What is the width? "))

# if length == width:
#     print("This is a square")
# else:
#     print("This is not a square")

# num1 = int(input("give me one number"))
# num2 = int(input("give me a second number"))

# if num1 > num2:
#     print("num1 is greater then num2")

# person1 = int(input("Age for person 1"))
# person2 = int(input("Age for person 2"))
# person3 = int(input("Age for person 3"))

# if person1 < person2 and person1 < person3:
#     print("person1 is youngest")
# elif person2 < person1 and person2 < person3:
#     print("person2 is the youngest")
# elif person3 < person1 and person3 < person2:
#     print("person3 is the youngest")

# if person1 > person2 and person1 > person3:
#     print("person1 is oldest")
# elif person2 > person1 and person2 > person3:
#     print("person2 is the oldest ")
# elif person3 > person1 and person3 > person2:
    # print("person3 is the oldest")


classesheld = int(input("How many classes were held?"))
classesattended = int(input("How many classes were attended?"))

if (classesattended / classesheld) >= 0.75:
    print(f"Your attendance percentage is {(classesattended / classesheld) * 100}%")
    print("You may attend the exam")
else:
    print(f"Your attendance percentage is {(classesattended / classesheld) * 100}%")
    print("you may not attend the exam")





