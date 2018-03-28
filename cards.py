import random
card=0 
def pick_up_card():
    global card
    card+=1
while card != 9:
    pick_up_card()
    print (card)
print("you found the nine. Well done")
quit()
