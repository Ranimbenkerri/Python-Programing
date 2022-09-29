# score = input("entre student score :").split()

# for n in range(0, len(score)):
#     score[n]=int(score[n])
# print(score)
# highest_score=score[0]
# for a in score:  
#     if a < highest_score:
#        a = highest_score
# print(f"the highest score is : {a}")
#range(a, b, step)
##########################################################
s=0
for i  in range(1, 101):
    if(i%2==0):
        s=s+i

print(s)
for i in range(1, 101):

    if(i%15==0):
        print("buzz fizz")
    elif(i%5==0):
        print("buzz")
    elif(i%3==0):
        print("fizz")
    else:
       print(i)