"""
You invite home 10 of your closest friends and play a simple game of luck.
Each of your friend picks up a card from a stack of cards numbered from 300 to 325.
The person with the highest number wins
Simulate this simple game using Python
[ Hint : Make sure that no 2 friends get the same numbered card ]
"""
import random
a = xrange(99,999)
#for i in a:
#    print i
f,p = 0,0
C10Cards = random.sample(a,10)
print C10Cards
#print "C10CardsMax:",max(C10Cards),"Place holder:",C10Cards.index((max(C10Cards)))+1,"Won the Game" # with max function
for i in C10Cards:
    print "Friend at Place",C10Cards.index(i)+1,"Picked number",i,"\n"
print "C10CardsMax:",max(C10Cards),"Place holder:",C10Cards.index((max(C10Cards)))+1,"Won the Game" # with max function

"""
for i in C10Cards:
#    print i
    if i > f:
        p = C10Cards.index(i)
        f = i
  
print "Friend in place,",p+1," Wins with",f,"as Card Numbers"
"""
