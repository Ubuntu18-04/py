s="""
def C_to_F(celsius):
  Farenheit=((9/5)*celsius)+32
  return Farenheit
def F_to_C(Farenheit):
   celsius=((5/9)*(Farenheit-32))
   return celsius
"""
with open("util.py","x+")as Module:
    Module.writelines(s)