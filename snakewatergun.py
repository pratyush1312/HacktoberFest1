import random 
comp=random.randint(1,3)
you=int(input("Choose between snake(1), water(2),gun(3) \n "))

if comp==1:
    comp="snake"
    if you==1:
        print(f"Game is tie. Computer choose {(comp)}")
    elif you==2:
        print(f"Computer won. Computer choose {(comp)}")
    else:
        print(f"You won. Computer choose {(comp)}")
elif comp==2:
    comp= "water"
    if you==2:
        print(f"Game is tie. Computer choose {(comp)}")
    elif you==3:
        print(f"Computer won. Computer choose {(comp)}")
    else:
        print(f"You won. Computer choose {(comp)}")
else:
    comp= "gun"
    if you==3:
        print(f"Game is tie. Computer choose {(comp)}")
    elif you==1:
        print(f"Computer won. Computer choose {(comp)}")
    else:
        print(f"You won. Computer choose {(comp)}")
