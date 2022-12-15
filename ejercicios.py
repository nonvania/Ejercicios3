#69
pais = ("Brasil", "México", "Escocia", "Japón", "USA")
print (pais)
print ()
pp= input ("ingrese un país: ")
print (pp, "tiene como posición ", pais.index (pp))


#70
pais = ("Brasil", "México", "Escocia", "Japón", "USA")
print (pais)
print ()
p= input ("Ingrese uno de los paises: ")
print (p, "has index number", pais.index (p))
print ()
num= int(input ("escriba un numero entre 0 y 4: "))
print (pais [num])



#71
Dlist = ["Volleyball", "football"]
Dlist.append(input ("Deporte favorito: "))
Dlist.sort()
print (Dlist)



#72
Mlist = ["Física Elemental", "Matemáticas", "Inglés", "Diseño digital", "Literatura","Biología"]
print (Mlist)
N= input("Cuál de estas materias no te gusta? ")
getrid Mlist.index (N)
del Mlist [getrid]
print (Mlist)




#73
cd= {}
c1 input ("comida que te guste: ")
cd [1] = c1
c2 = input ("segunda comida: ")
cd [2]= c2
c3= input ("tercera comida: ")
cd [3]= c3
c4 = input ("ultima comida: ")
cd [4] c4
print (cd)
NO = int(input ("qué comida quieres eliminar? "))
del cd [NO]
print (sorted (cd.values ()))





#74
colores = ["red", "blue", "green", "black", "white", "pink", "orange", "purple", "yellow", "brown"]
inicio= int (input ("ingresa un numero entre 0 y 4 para empezar: "))
fin= int (input ("ingresa un numero entre 5 y 9 para terminar: "))
print (colours [inicio:fin])





#75
nums [123,345,234,765]
for i in nums:
    print (i)
    s=int (input ("Escribe un numero de la lista: "))
if s in nums:
    print (s, "está en la posición", nums.index (s))
else:
    print ("Eso no está en la lista")





#76
namel input ("a quién quieres invitar a tu fiesta? ")
name2 =input ("segundo: ")
name3= input ("tercero: ")
party =[namel, name2, name3]
a = input ("quieres invitar a alguien mas? ")
while another == "y":
    nn = party.append(input ("Enter another name: "))
    a = input ("quieres invitar a alguien mas? ")

print("tienes", len (party), "personas que vendran a tu fiesta")



#77
namel = input ("nombre de quien aisstirá a tu fiesta: ")
name2 = input ("ingresa otro nombre: ")
name3= input ("tercer nombre: ")
party [namel, name2, name3]
another input ("quieres invitar a alguien mas? s/n ")
while another == "s":
    newname = party.append(input("ingresa otro nombre: "))
    another= input("quieres invitar a alguien mas? s/n ")
print ("tienes", len (party), "personas vendrán a tu fiesta")
print (party)
selection= input ("escribe uno de los nombres: ")
print (selection, "está en la posición", party.index (selection), "on the list")
stillcome input ("aun quieres que asistan? s/n ")
if stillcome == "n":
party.remove (selection) print (party)




#78
tv = ["Ridiculous", "Malcolm", "Dragon Ball", "Bob Esponja"]
for i in tv:
    print (i)
print ()
newtv = input ("ingresa otro programa de television: ")
position =int (input ("escribe un numero entre 0 y 3: "))
tv.insert (position, newtv)
for i in tv:
    print (i)





#79
nums = []
count= 0
while count <3:
    num=int (input ("ingresa un numero: "))
    nums.append(num)
    print (nums)
    count= count + 1

n=input ("quieres que el ultimo numero se guarde? si/no ")
if lastnum == "no":
nums.remove (num)
print (nums)