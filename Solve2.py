# Solve 2
# import math
# angka = input("Silahkan masukkan angka berapapun : ")
# angka = int(angka)
# print(math.pow(angka, 2))
# a = int(input("Masukkan angka berapapun : "));
# print("Kuadrat dari " + str(a) + " = " + str((int(a)**2)));

# Hoki Hoki Bento

def printMainMenu():
    inputUser = input('1. Lihat Menu\n'+'2. Lihat Cart\n'+'3. Checkout\n'+'4. Keluar\n' + 'Pilih Menu :')
    return inputUser

def printMenu(menuList):
    print('Pilihan Menu : ')
    for x in range(0, len(menuList)):
        print(str(x+1) + ". " + menuList[x])
    inputUser = input("Mau yang mana ? : ")
    return [int(inputUser)-1, menuList[int(inputUser)-1]]

def printCart(cartList):
    print("Isi Cart : \n")
    for x in range (0, len(cartList)):
        print(str(x+1) + ". " + cartList[x][1])

def checkout(cartList, hargaList):
    while True :
        totalHarga = 0
        print('Item yang dipilih : ')
        for x in range (0, len(cartList)):
            print(str(x+1) + '. ' + cartList[x][1])
            totalHarga += hargaList[cartList[x][0]]
        inputDuit = input('Total Harga Rp.' + str(totalHarga) + '\n\n Punya Duit Berapa ciiii :')
        if(int(inputDuit)<(totalHarga)):
            print(' Lagi kere ya? minta aja ke iqbalgazali')
        else :
            print(" Kembaliaan nya segini nih : Rp." + str(int(inputDuit) - totalHarga))
            break

listMenu = ['Paket Hoki A Rp. 20.000','Paket Hoki B Rp. 25.000','Paket Hoki C Rp. 30.000']
listHarga = [20000, 25000, 30000]
listCart = []

while True :
    pilihanuser = printMainMenu()
    if(pilihanuser == '1'):
        listCart.append(printMenu(listMenu))
    elif(pilihanuser == '2'):
        printCart(listCart)
    elif(pilihanuser == '3'):
        checkout(listCart, listHarga)
        listCart = []
    elif(pilihanuser == '4'):
        print('Terimakasih, Jangan Bosen dan Sampai Jumpa Lagi yaaa')
        break
