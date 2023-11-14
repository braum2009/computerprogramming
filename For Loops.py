school = "paradigm"
for i in school:
    print(i)

for x in range(5):
    print(x)


Animals =  ['Cat','Dog','Tiger','Cow']
for n in Animals:
    print (n)


flowers = ['Jasmine','Lotus','Rose','Sunflower']
for o in flowers:
    print(o)
print("Done")

list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']
for i in list1:
    for j in list2:
        print(i,j)


vehicles = ['Car','Cycle','Bus','Tempo']
for v in vehicles:
    if v == "Bus":
        continue
    print(v)


numbers = [12,3,56,67,89,90]
count = 0
for n in numbers:
    count += 1
print(count)


numbers = [12,3,56,67,89,90]
sum = 0 
for n in numbers:
    sum += n
print(count)

numbers = [2,5,6,10,15,20,25]

for i in numbers:
    if i % 5 == 0:
        print(i) 



list1 = ['Mango','Banana','Orange']
list2 = []


for i in list1:
    list2.append(i)
print(list2)


numbers = [1,4,50,80,12]
min = 1000 

for i in numbers:
    if i<min:
         
        min = i 
print(min)



numbers = [1,4,50,80,12]
numbers.sort()
numbers.reverse()
print(numbers)

list1 = [3]
Current = 3
for i in range(5):
    list1.append(Current + 3)
    Current += 3
print(list1)



list1 = [5]
Current = 5
for i in range(2):
    list1.append(Current + 5)
    Current += 5
print(list1)

 

for i in range(10, 0, -1):
    print(i)
    
for i in reversed(range(11)):
    print(i)