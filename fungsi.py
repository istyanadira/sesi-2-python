name = "Nadiraa"
total = len(name)
name = name.upper()

#print(name[1])
#print(name[2])
#print(name[3])

for i in range(total) :
    print(name[:total-i] + "X"*(i-1+1))