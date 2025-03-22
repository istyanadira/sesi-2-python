Name = "Nugraha", "John", "Jane", "Doe"
yearnow = 2025
Birthdate = yearnow - 1989, yearnow - 1990, yearnow - 1992, yearnow - 1994

print("NO|  NAME   |  AGE  ")

for i, (x,y) in enumerate(zip(Name, Birthdate), start=1):
    print(f"{i} | {x:<7} | {y}")
