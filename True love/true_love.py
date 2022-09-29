print("Welcome to the love calculator!")
name1=input("type in your name\t").lower()
name2=input("type in their name\t").lower()
comb=name1+name2


true=comb.count("t")+comb.count("r")+comb.count("u")+comb.count("e")
love=comb.count("l")+comb.count("o")+comb.count("v")+comb.count("e")

perc=int(str(true)+str(love))
if perc>100:
    print("your love score is %",perc,", you go together like ..")
if perc>=80 :
 print("your love score is %",perc,", you go together like coca colla and mentos")

elif perc<80 and perc>40 :
 print("your love score is %",perc,", you go alright together")

else :
 print("your love score is %",perc,",They don't really like u sorry mate")


