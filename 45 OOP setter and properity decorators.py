
"""
READ FULLL DOCUMENTION CAREFULLY

"""


class Employe:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f"{self.fname}.{self.lname}@gmail.com"
        """
        this self.email is used because for setting the email but if we want to change the email it will 
        not change the email so for this we are useing the  @property method which is a setter whcih will be 
        use for setting the new name if we want to change the name
        WHY WE USE PROPERTY
        so why we using the property because if we not use the property then we print em1.email we must have 
        gave email as funcrion means emp1.email() but we did not want to use it as function so we use property
        """

    @property
    def email(self): # made a setter which is used for changing the email
        if self.fname==None or self.lname==None:
            return f"Email is deleted and  set agian the email "
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter # made a setter for changing the names and gmail if we want
    def email(self,string):
        name=string.split("@")[0] # split cuts the email between the @ and it will take the index side [0]
        self.fname=name.split(".")[0]
        self.lname=name.split(".")[1]
    @email.deleter  # it is used for deleting the email
    def email(self):
        self.fname=None
        self.lname=None
emp1=Employe("Rehman", "Ali")
print(emp1.email)
emp1.fname="jutt"  # here we change the first name and for that is we used the setter
print(emp1.email)

# what if we want to change the email and or if email is changed also our name will be changed
emp1.email="RA.Jutt@gmail.com" # if we write like this then it will gave error of cant set the attribute
print(emp1.email)
del emp1.email # here we delete the  email
print(emp1.email)