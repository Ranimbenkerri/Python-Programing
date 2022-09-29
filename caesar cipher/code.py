from ast import AugAssign
from turtle import goto
from logo import Logo
print(Logo)
def cesar(t, s, d):
    if d=='encode':
        cipher_text=""
        for letter in t:
           if letter in abc:
                position = abc.index(letter)
                new = position + s
                new=new%26
                cipher_text+=abc[new]
           if letter not in abc:
                cipher_text+=letter
        print(f"the new word is : {cipher_text}")
    if d=='decode':
        cipher_text=""
        for letter in t:
            position = abc.index(letter)
            new = position - s
            new_letter= abc[new]
            cipher_text+=new_letter
        print(f"the new word is : {cipher_text}")

user_countinue= True
while user_countinue:
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    direction = input("type 'encode' to encrypt, type 'decode' for decrypt : ")
    text = input("\n type ur text : ").lower()
    shift = int(input("\n Type the shift number : "))
    shift = shift % 26
    cesar(t=text, d=direction, s= shift)

    user = input("type 'yes' if u wnat to go again,Otherwide type 'no'")
    if user == 'no':
        user_countinue= False 
        print("Goodbye")
    if user == 'yes':
        user_countinue=True   


 