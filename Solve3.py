
import math

# def solve3 (hari):
#     tahun = math.floor(hari/360)
#     sisahari = hari%360
#     bulan = math.floor(sisahari/30)
#     sisahari2 = sisahari%30
#     minggu = math.floor(sisahari2/7)
#     hari = math.floor(sisahari2%7)

#     print("{} tahun {} bulan {} minggu {} hari".format(tahun,bulan,minggu,hari));

# solve3(485)

# total = 485
# tahun = math.floor(total/360)
# bulan = math.floor((total%360)/30)
# minggu = math.floor((((total%360)%30)/7))
# hari = math.floor (((((total%360)%30)%7))

# print(str(total)) + 'hari adalah' )
# print(str(tahun)) + 'tahun' )
# print(str(bulan)) + 'bulan' )
# print(str(minggu)) + 'minggu') 
# print(str(hari)) + 'hari ' )

listMakanan = ''
tharga = 0
text = "Selamat Datang di HOKI HOKI BENTO ";
text1 = "Main Menu\n";
print(text)
print(text1)

listMenu= ('1. Lihat Menu\n'+'2. Lihat Cart\n'+'3. Checkout\n'+'4. Keluar\n')
print(listMenu)

angka = input("Silahkan Masukkan Nomor Menu :")

# if (angka == "1"):
#     print('List Menu\n' '1. Paket Hoki A Rp. 20.000\n' '2. Paket Hoki B Rp. 25.000\n' '3. Paket Hoki C Rp. 30.000')
# elif (angka == "2"):
#     print('Lihat Cart') 
# elif (angka == "3"):
#     print('Checkout')
# else :
#     print('Keluar')

def LihatMenu():
    global listMakanan
    global tharga

    print('List Menu')

    NamaPaket1 = '1. Hoki Hoki Bento '
    NamaPaket2 = '2. Hoki Hoki Bento '
    NamaPaket3 = '3. Hoki Hoki Bento '
    Hargapaket1 = 20000
    Hargapaket2 = 25000
    Hargapaket3 = 30000

    print(f"{NamaPaket1}Rp{Hargapaket1}")
    print(f"{NamaPaket2}Rp{Hargapaket2}")
    print(f"{NamaPaket3}Rp{Hargapaket3}")
    
    
    angka = int(input("Silahkan Masukkan Pilihan Menu :"))

    while (angka > 0):
        if(angka==1):
            listMakanan += NamaPaket1 + str(Hargapaket1) + 'RP' + '\n'
            print(listMakanan, tharga)
            tharga += Hargapaket1
            LihatMenu()
            break
        elif(angka==2):
            listMakanan += NamaPaket2 + str(Hargapaket2)+ 'RP' + '\n'
            print(listMakanan, tharga)
            tharga += Hargapaket2
            LihatMenu()
            break
        elif(angka==3):
            listMakanan += NamaPaket3 + str(Hargapaket3)+ 'RP' + '\n'
            print(listMakanan, tharga)
            tharga += Hargapaket3
            LihatMenu()
            break
        else :
            print('Silahkan pilih menu lain nya lagi yaa. Lagi abis hehe\n')
            print('')
            LihatMenu()
            break 



if (True):
    LihatMenu()