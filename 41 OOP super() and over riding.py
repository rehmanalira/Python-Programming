class jutt:
    name1="JUtt class"
    def __init__(self):
        self.name1="JUTT Sb class jutt"
        self.l = "lope"
class shaka(jutt):
    name2="Shaka class"
    def __init__(self):
        super().__init__()
        self.name1="JUTT Sb class shaka"


j=jutt()
s=shaka()
#print(s.name1)#over ride the variable
print(s.l)