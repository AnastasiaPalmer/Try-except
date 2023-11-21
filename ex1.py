"""введення користувачем тексту замість цифр;"""

def inputNumber() :
   y = 0

   print("Demo: alpha-symbols instead numeric only for function int('0...9')")

   try:
      x = input('Please number: ')
      y = int(x);

   except ValueError:
      print("Catch ValueError :-(")
      exit(1)
   except:
      print("Unknown Error :-(")
      exit(1)

   print('Int y = ', y);


if __name__ == '__main__':
   inputNumber()

