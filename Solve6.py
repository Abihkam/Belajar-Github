# import time
# etd = '09.00 AM'
# miles = 120;
# a miles per hour = 60;
# b miles per hour = 40;

# text = "I'm Baron, nice to meet you";
# print(text[1]); 
# print(text[2:]); 
# print(text[:4]); 
# print(text[2:5]); 
# print(text[:]);

# angka1 = input("Masukkan Angka 1 : "); 
# angka2 = input("Masukkan Angka 2 : ");

# print(angka1 + angka2);
# print(int(angka1) + int(angka2));

# usia = 21;
# nama1 = 'Abi';
# nama2 = 'Mila';
# print(usia + usia);
# print(nama1 + ' ' + nama2); 
# print(nama1 + nama2 + ' ' + str(usia));

import math
# nomor 6
# jamawal = 9;
# jarak = 120
# kecepatantotal = 100/3600;
# lamadetik = jarak/kecepatantotal
# lamajam = math.floor(lamadetik/3600);
# lamamenit = math.floor ((lamadetik%3600)/60);

# print('Lama jam = ' + str(lamajam) + ' ' + "Lama menit = " + str(lamamenit));
# print('Tabraknya pukul = ' + str(jamawal + lamajam)) + 'dan menit ke' + str(lamamenit) + 'dan detik ke' + str(lamadetik);


# u = 'Nomor Urut'
# for x in range (1,11):
#     print(u + ' ' + str(x))

# for x in range (0,21,2):
#     print(u + ' ' + str(x))

# listTipe = ['Sans', 22, 'Uhuy', 30, 'Okedeh' ]
# for x in listTipe :
#     print(x)

# z = ''
# for x in range (5):
#     for y in range (5):
#         z += '*' + ' '
#     z += '\n'
# print(z)

# z = ''
# for x in range (10):
#     for y in range (0, x+1):
#         z += '*' + ' '
#     z += '\n'
# print(z)

# Solve 2 input by User
# angka1 = input(" Masukkan angka : ")
# angka2 = input(" Masukkan angka : ")
# angka3 = input(" Masukkan angka : ")
# angka4 = input(" Masukkan angka : ")
# z = ''
# for x in range (int(angka1)):
#     for y in range (x+1,int(angka2)):
#         z += (' * ' + ' ')
#     z += '\n'

# for a in range (int(angka3)):
#     for m in range (int(angka4),a+1):
#         z += (' * ' + ' ')
#     z += '\n'

# print(z)

# Solve it 3
# def full_pyramid(rows):
#     for i in range(rows):
#         print(' '*(rows-i-1) + ' ' + '*'*(2*i+1))
# full_pyramid(6)

# # Solve it 4
# def inverted_pyramid(uhuy):
#     for x in reversed (range(uhuy)):
#         print(' '*(uhuy-x-1) + ' ' + '*'*(2*x+1))
# inverted_pyramid(6)
# # ------------------------------------------------------------------------------------------------

# # Solve it 5
# def puul_pyramid(rows):
#     for i in range(rows):
#         print(' '*(rows-i-1) + ' ' + '*'*(2*i+1))

# def kebalik_pyramid(uhuy):
#     for x in reversed (range(uhuy)):
#         print(' '*(uhuy-x-1) + ' ' + '*'*(2*x+1))

# puul_pyramid(7)
# kebalik_pyramid(7)

# x = int(input(" Masukkan size : "));
# z = ' '

# for a in range (x):
#     for m in range(0, x-1-a):
#         z += "   "
#     for h in range(0, (a*2)+1):
#         z += " * "
#     z += "\n"
# print(z)

size = int(input(" Masukkan size : "))
z = ' '

for num in range (size):
    for num1 in range(num,size):
        z += " * "
    for num2 in range(0,(num*2,-1)):
        z += "  "
    for num3 in range(size,num,-1):
        if(num3 == 1):
            break
        z += " * "
    z += '\n'

print(z)





