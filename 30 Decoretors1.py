""""
Decorator:

decorators are the function or a function in which we take an argument as an function and made another
function in the decorators just in example we take func1 which is function and also argument of the
function decorator and we made another function exe in decorator function
"""



def decoretor(func1):
  def exe():
      print("YR before decoretor")
      func1()#callinf function which we take as anrgument
      print("yr ni this is after decorator")
  return exe #here we returning the function exe


@decoretor #this is also way which is used to call the decorator
def show():

    print("Rehman ALi RA")

#show=decoretor(show)--> we can also write this if we want not to write the @decorator
show()

