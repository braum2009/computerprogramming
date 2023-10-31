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
    for c in count:
        print