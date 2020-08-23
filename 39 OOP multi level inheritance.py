"""
Multi level inheritance

it will inherit one by one means 1st class properity goes -> into next and next and the last class can use
the properity of every class but not above class can use the properity of below class

"""


class electronic_device:
        current="5 AMP"


class gadeget(electronic_device):
        current = "10Amp"
        pocket="YES"



class phone(gadeget):
    current = "30 AMp"
    pocket = "YES"
    screen="it showw the screen"


e=electronic_device()
g=gadeget()
iphone=phone()
print(iphone.screen)
