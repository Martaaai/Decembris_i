#Izveidojiet Python programmu, kas aprēķina lietotāja ievadīta skaitļa faktoriālu, izmantojot for ciklu.
skaitlis=int(input("ievadiet skaitli:"))
faktorials=1

if skaitlis<0:
    print("faktorials nav negatīviem skaitļiem")
elif skaitlis==0:
    print(faktorials no 0 ir 1.)
else:
    for i in range(1,skaitlis+1):
        faktorials*=i
        print("faktorials no",skaitlis,"ir"faktorials)

