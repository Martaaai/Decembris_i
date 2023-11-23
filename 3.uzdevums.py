#Izveidojiet Python programmu, kas pārbauda, vai ievadītais skaitlis ir nepāra, izmantojot if priekšrakstu.
skaitlis=int(input("ievadiet skaitli:"))
if skaitlis %2!=0:
    print("skaitlis ir nepāra")
else:
    print("skaitlis ir pāra")