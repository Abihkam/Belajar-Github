# print('Uhuy Sans!!');
# print('Kucing Sans!!');
# print adalah sebuah function dari python untuk menampilkan text
# print('kucing sans!!');
#
# angka1 = 5;
# print(angka1);
# angka1 = 9;
# print(angka1);

# nama = 'Andi'; 
# print(nama);
# usia = 22; 
# usia = 32; 
# print(usia);
# jomblo = True;
# print(jomblo);

# def test(angka1):
#     hasil = angka1 + angka1;
#     return hasil;

# def mumet(angka1):
#     hasil = angka1 + angka1;
#     print(hasil);
#     return 'HIHIHIHIHIHIHIHI UHUY';

# num1 = 5;
# ab = mumet (200);
# print(ab);

# nama = input("Nama kamu? : ");
# umur = input("Umur kamu? : ");
# kelamin = input("Kelamin kamu? : ");
# pekerjaan = input("Pekerjaan kamu? : ");

# print("Nama : " + nama);
# print("Umur : " + umur);
# print("Kelamin : " + kelamin);
# print("Pekerjaan : " + pekerjaan);

# usiaAbi = 20;
# usiaAbi += 3

# print(usiaAbi);

# usiaAbi = 20;
# usiaAbi = usiaAbi + 3

# print(usiaAbi);

# usiaAbi = 20;
# hasil = usiaAbi + 3

# print(usiaAbi);

# import math
# print(math.pi);
# print(math.fabs(-1.7));
# print(math.pow(2,7));
# print(math.sqrt(81));


# x = 5;
# y = '5'; 
# z = 6;
# print(x==int(y) and int(y)<z); 
# print(x==int(y) or int(y)<z); 
# print(not(x==int(y) or int(y)<z));

# if(False==False):
#     print('Hello');
# elif(False):
#     print('Apa Kabar');
# else : 
#     print('Salah lu semua hahahhaahhahaha'); 


# angka = 1;
# while(angka <= 10): 
#     print(angka); 
#     angka += 1;

# i = 1;
# while(i < 10):
#     print(i)
#     if i == 5: 
#      break
#     i += 2

# SLide 3 Loop
# nomorurut = [1,2,3,4,5,6,7,8,9,10]
# for x in nomorurut:
#   print( "Nomor Urut" + " " + str(x)); 

# u = 'Nomor Urut'
# for item in range (1,11):
#     print(u + " " + str(item))

# for x in range(6):
#   print("Nomor Urut" + " " + str(x)) 

# x = 0
# while(x<=20):
#     print("Nomor Urut" + " " + str(x))
#     x+=2

# listItem = list(range(1,11,2))
# print(listItem) 

# for x in range(0,21, 2):
#   print("Nomor Urut" + " " + str(x))

# for x in range(1,20, 2):
#   print("Nomor Urut" + " " + str(x))

# z = ''
# for x in range (0,1000):
#     z += '*'
# print(z)

# z = ''; 
# for x in range (0,20):
#     z += ' * \n'
# print(z)

# z = '';
# for x in range (5):
#     for y in range (5):
#         z += ' * '
#     z += '\n'
# print (z)

# Solveit Contoh Slide Loop
# z = '';
# for x in range (10):
#     for y in range (0, x+1):
#         z += ' * '
#     z += '\n'
# print (z)

# Solveit 1 Slide Loop
z = '';
for x in range (5):
    for y in range (x+1, 6):
        z += (' * ' + ' ')
    z += '\n'
print(z)

# Solve it 2 Slide Loop
z = '';
for x in range (4):
    for y in range (x+1, 6):
        z += (' * ' + ' ')
    z += '\n'
for a in range (5):
    for m in range (0,a+1):
        z += (' * ' + ' ')
    z += '\n'
print(z)

# Solve it 3 Slide Loop
# z = '';
# for x in range (0,10):
#     for y in range (1,20):
#         z += (' * ' + ' ')
#     z += '\n'
# print(z)