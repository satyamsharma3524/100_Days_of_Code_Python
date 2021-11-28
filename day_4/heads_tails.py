import random

coin = random.randint(1,2)
if coin==1:
    print("Heads")
elif coin==2:
    print("Tails")
else:
    print("Coin stuck in the middle, Generated a wrong random number.")