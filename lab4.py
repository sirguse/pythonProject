n = int(input("Proszę podać liczbę studentów: "))
a = 1 #wyświetlanie od 1 studenta
c = 0 #podstawienie pod dodawanie punktów
while a<=n:
    b = int(input(f"Proszę podać punkty studenta {a}: "))
    c += b #sumowanie punktów studentów
    a += 1 #przechodzenie do kolejnego studenta
y = c/n #obliczanie średniej
print("Średnia wszystkich studentów",y)