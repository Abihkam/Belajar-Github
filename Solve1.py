# Solve 1 
# import math
# def solve(x,y,z):
#     hasil = (x+y*z)/(x*y)
#     # print (math.pow(hasil, z)); 
#     return (hasil**z)

# jawaban=solve(4,3,2)
# print(jawaban)

# # no 1
# # x = 4;
# # y = 3;
# # z = 2;

# # w = ((x+y*z)/(x*y))**z;

# def namaku(nama) : 
#     print(nama + ' Susilo');

# namaku ('Adi'); 
# namaku('Budi'); 
# namaku('Caca'); 
# namaku('Dedi');

# z = 0
# def total(x,y):
#     z = x+y
#     # print(z) kalau ini ga di print gada 9
#     # return z kalau ga direturn nanti jadi none

# print(total(5,4))
# print(z)

# Fn Inside Fn
# def kali(x) :
#     if (x < 2) :
#        return 1;
#     else :
#        return (x * tiga());
# # tiga() sudah bisa dipanggil karena sudah defined dan print(kali) setelahnya.
# def tiga() :
#     return 3; 

# print(kali(5));

# Recursive Function

# def pangkat(a,m):
#     if(m == 1):
#         return a
#     else :
#         m -= 1
#         return a * pangkat(a,m)
# print(pangkat(2,4))

# def kali(angka1 = 5, angka2 = 2) : 
#     return angka1 * angka2;
# print(kali(angka2=4))

# buah = ['Jeruk', 'Nanas', 'Apel'];

# for item in buah :
#     print(item);

# Contoh append.pop
buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga'];
buah.append('Kelapa'); 
# append untuk masukkin
# pop untuk mengeluarkan
# print(buah); 
buah.pop();
# print(buah) 
buah.pop(); 
print(buah);

# List Inside List and Difference Type Data
# listTest = [1, 'hi', ['hello', 2, True, [0, 1]]]
# print(listTest[1]);
# print(listTest[:2]);
# print(listTest[2]);
# print(listTest[2][1:]);
# print(listTest[2][2]);
# print(listTest[2][3][0]);

def minMac (theList):
    min = 0
    max = 0
    return [min,max]

x = [40,100,5,25,10]
max_value = max(x)
min_value = min(x)
avg_value = sum(x)/len(x)

