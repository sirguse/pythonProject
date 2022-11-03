x = int(input("Podaj liczbę: "))
str= ""
for i in range(x):
    for l in range(x):
        str += "*"
    print(str)
    str= ""
