# Nomor 4

# total = 49
# ratiototal = 14
# satuan = total/ratiototal

# usiaandi = 4 * satuan;
# usiabudi = 10 * satuan;

# print('Usia andi 2 tahun lagi = ' + str(int(usiaandi)+ 2));
# print('Usia budi 2 tahun lagi = ' + str(int(usiabudi)+ 2));

# angka = input("Masukkan angka? : ");

# if(int(angka)%2==1):
#     print('Angka ini tergolong bilangan ganjil');
# else :
#     print('Angka ini tergolong bilangan genap');

Massa = int(input("Masukkan Massa(kg)? : "));
Tinggi = int(input("Masukkan Tinggi(cm)? : "));
imt = Massa / ((Tinggi/100)**2);

text = " ";

if(imt < 18.5) :
    text = 'BERAT BADAN KURANG!';
elif(imt >= 18.5 and imt <= 24.9):
    text = 'BERAT BADAN IDEAL!';
elif(imt >= 25.0 and imt <= 29.9):
    text = 'BERAT BADAN BERLEBIH!';
elif(imt >= 30.0 and imt <= 39.9):
    text = 'BERAT BADAN SANGAT BERLEBIH!';
else :
    text = 'BERAT BADAN OBESITAS!';

print("Massa : " + str(Massa) + 'kg & Tinggi' + ' ' + str(Tinggi/100) + 'M' )
print('imt = ' + str(imt) + ' ' + text);