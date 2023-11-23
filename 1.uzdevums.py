#Izveidojiet Python programmu, kas saskaita no 1 līdz lietotāja ievadītam skaitlim, izmantojot for ciklu.
skaitlis=int(input("ievadi skaitli:"))
summa=0
for i in range(1,skaitlis+1):
    summa += i
    print("summa no 1 līdz",skaitlis,"ir",summa)
    


