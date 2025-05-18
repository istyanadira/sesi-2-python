def tipe_input(input1, input2, input3):
    if isinstance(input1, str) and isinstance(input2, int) and isinstance(input3, float):
        return "Tipe input valid"
    else:
        return "Tipe input tidak valid"
    
print(tipe_input("hi", 10, 9.8))
print(tipe_input(127, 99, 5.9))
print(tipe_input("jawa", "182", 8.8))
print(tipe_input("arlecchino", 396, "96.3"))

#def tipe_input(input1, input2, input3):
#input1 = str(input("Masukkan tipe data pertama: "))
#input2 = int(input("Masukkan tipe data kedua: "))
#input3 = float(input("Masukkan tipe data ketiga: "))

#if isinstance(input1, str) and isinstance(input2, int) and isinstance(input3, float):
        #return "Tipe input valid"
    #else:
        #return "Tipe input tidak valid"

#print(input1, input2, input3)