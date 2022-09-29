import random
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
s =["$","@","&","(",")"]
n =["1","2","3","4","5","6","7","8","9"]
pswrd=[]
lettres = int(input("how many lettres would you like in ur password? "))
for char in range(1, lettres+1):
     pswrd+=random.choice(abc)

symbol = int(input("symbols? "))
for char in range(1, symbol+1):
    pswrd+= random.choice(s)

numbres = int(input("numbres? "))
for char in range(1, numbres+1):
     pswrd+=random.choice(n)
random.shuffle(pswrd)
p=""
for char in pswrd:
   p=p+char
print(p)