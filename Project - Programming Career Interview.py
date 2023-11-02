interviewee = input("Hello thank you for comming can I get your name? ")

print(f"Hello {interviewee}. Let's get started.")

programming = input("what types of promgramming are you interested in? ")

experience = int(input("How many years of experience do you have? "))

if experience < 2:
    print("Sorry, at this time we're looking for someone with more experience. Please apply at a later time.")
    exit()

desired_salary = int(input("What is your desired salary? "))

if desired_salary > 35000:
    print("Sorry only our higher positions are qualified for more then 35000 a year and since you are not we can not give you a salary higher then 35000")
    exit()

enjoyment_or_money = input("Are you working here for the money or the enjoyment?")

why = input("why did you choose this job?")

did_you = input("did you take any risks with this job")

if did_you == "yes" or did_you == "Yes":
    print("we are sorry to inform you we do not think you would be a good fit for this company since you have not taken any risks")
    exit()

retrei_time = input("when do you plan on retiring?")

different_job = input("would you choose this job for another?")

regretfulness = input("do you regret choosing this job over being a tech guy at one of the biggest facilitys in the country?")

position = input("what is your disired position?") 

print(f"Great, that concludes our interview. Let's recap.")
print(f"You said your name was? {interviewee}.")
print(f"what is your desired salary? {desired_salary}.")
print(f"What types of programming are you interested in?{programming}"
print(f"Are you working for the money or for the enjoymen?t{enjoyment_or_money}"
print(f"why did you choose this job? "{why}
print(f"Did you take any risks with this job?"{did_you}
print(f"When do you plan on retiring?"{retrei_time}
print(f"Would you choose this job for another?"{different_job}
print(f"Do you regret choosing this job over be a tech guy at one of the biggest facilitys in the country"{regretfulness}
print(f
print(f
print(f
print(f
print(f
print(f
print(f