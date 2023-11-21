import re

"""введення користувачем неправильної відповіді (потрібно самостійно "підняти" виключення)"""
# 2023-05-31
template = re.compile('^20\d\d-\d\d-\d\d$')

def enterDate():
   x = input('Enter a date:')
   # print(f' -- entered [{x} - type {type(x)}]')
   if x==None or x=='':
      raise ValueError("VrongDate: empty string")
   elif len(''+x)!=10:
      raise Exception("VrongDate: should be 10 symbols")
   elif re.search(template,x)==None:
      raise Exception("VrongDate: should match yyyy-mm-dd")
   elif x[5:7]<'01' or x[5:7]>'12':
      raise ValueError
   elif x[8:10]<'01' or x[8:10]>'31':
      raise ValueError('Not a day')
   else:
      return x

def inputDate():
   try:
      x = enterDate()
   except ValueError as ve:
      print(f"Wrong value: [{ve}]")
      exit(1)
   except Exception as err:
      print("Unknown Error :-(", err)
      exit(1)
   else:
      print('Date = ', x);

if __name__ == '__main__':
   inputDate()


