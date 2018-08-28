def printMainMenu():
   inputUser = input('1. Isi List\n'+'2. Lihat List\n'+'3. Keluar\n' + 'Pilih Menu :')
   return inputUser

mylist = []

def satu():

   x = input("Silahkan masukan angka: ")
   mylist.append(x)
   print (mylist)
   # return mylist

def dua():
   stringList = []
   print("\n\n\n")
   print("Isi list saat ini adalah: " + str(mylist))
   print("Isi list yang dicetak dalam bentuk score board adalah seperti berikut:")
   for i in range(3):
       for j in mylist:
           if(i == 0):
               stringList.append(sevenSegments(j, "upper"))
           elif(i == 1):
               stringList.append(sevenSegments(j, "middle"))
           elif(i == 2):
               stringList.append(sevenSegments(j, "lower"))
           stringList.append("\t")
       if(i != 2):
           stringList.append("\n")
   print("".join(stringList))
   input("Tekan ENTER untuk melanjutkan . . .")

def sevenSegments(number, part):
   if(part == "upper"):
       if(number == '1' or number == '4'):
           return "   "
       else:
           return " __"
   elif(part == "middle"):
       if(number == '1' or number == '7'):
           return "   |"
       elif(number == '0'):
           return "|  |"
       elif(number == '2' or number == '3'):
           return " __|"
       elif(number == '5' or number == '6'):
           return "|__ "
       else:
           return "|__|"
   elif(part == "lower"):
       if(number == '1' or number == '4' or number == '7'):
           return "   |"
       elif(number == '2'):
           return "|__ "
       elif(number == '3' or number == '5' or number == '9'):
           return " __|"
       else:
           return "|__|"

while True :
  pilihanuser = printMainMenu()
  if(pilihanuser == '1'):
      satu()
  elif(pilihanuser == '2'):
      dua()
  elif(pilihanuser == '3'):
      print('Terimakasih, Jangan Bosen dan Sampai Jumpa Lagi yaaa')
      break