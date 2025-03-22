#for x in range(1, 20, 2):
    #print(x, end=" ")

#for x in range(2, 18, 2):
   # print(x, end=" ")

#for x in range(30, 6, -3):
 #   print(x, end=" ")

# result = 1
#add = 0

#for i in range(9) :
    #print(result, end=" ")
    #result += add
    #add += 1

#result = 30
#add = 1

#for i in range(8) :
    #print(result, end=" ")
    #result -= add
    #add += 2

a = b = c = 1

for i in range(9):
    print(c, end=" ")
    if (i >= 1) :
        c = a+b
        a = b
        b = c
