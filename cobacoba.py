nama = input("Siapa nama kamu?:");
umur = input("Berapa umur kamu?:");
kelamin = input("Apa jenis kelamin kamu?:");
pekerjaan = input("Apa pekerjaan kamu?:");

print("Nama : " + nama);
print("Umur : " + umur);
print("Kelamin : " + kelamin);
print("Pekerjaan : " + pekerjaan);
 
# Solve 1 
# import math
# def solve(x,y,z):
#     hasil = (x+y*z)/(x*y)
#     # print (math.pow(hasil, z)); 
#     return (hasil**z)

# jawaban=solve(4,3,2);
# print(jawaban);

# # Solve 2
# angka1 = input("Silahkan masukkan angka berapapun : ");


try:
  print(2)
  print(20 / 0)
  print(2)
except ZeroDivisionError:
  print(3)
finally:
  print(4)

