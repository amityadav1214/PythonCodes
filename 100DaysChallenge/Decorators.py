#Decorators
# def greet(fx):
#   def mfx(*args,**kwargs):
#     fx(*args,**kwargs)
#     print("Thanks for using this function")
#   return mfx

# @greet
# def hello():
#   print("Hello World")

# hello()
# #Can be written as below also
# #greet(hello)()

# @greet
# def add(a,b):
#   print( a + b )

# add(9,9)

#Decorators are basically used when we have to add logs in the functions

import logging
def log_fun(func):
  def mfx(*args,**kwargs):
    logging.info(f"{func.__name__} with args = {args} and kwargs = {kwargs}")
    result = func(*args,**kwargs)
    logging.info(f"{func.__name__} returned {result}")
    return result
  return mfx

@log_fun
def add(a,b):
  print( a + b )

add(5,6)
