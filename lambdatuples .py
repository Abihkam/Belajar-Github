# d = { "key1" : "item1", "key2" : "item2",
# "kucing" : [3, "jerapah"] };
# print(d["key1"]);
# print(d["key2"]);
# print(d["kucing"]);
# print(d["kucing"][1]);

# d = { "key1" : { "key2" : "item2" }, "kucing" : [3, "jerapah"] };
# print(d["key1"]); 
# print(d["key1"]["key2"]);

# t = (1, [0, "test"], { "a1" : True })
# print(t[2]["a1"]);
# print(t[1][1]);
# t[1][1] = "akan";
# print(t[1][1]);
# t[1] = "mark"; Tuples doesnot support item assignment
# print(t[1]);

# s = { 1, 3, 1, 2, 2, 3 };
# print(s);
# print(list(s)[2]);

# newList = [ 1, 3, "test1", "test2" , 2, 3, "test1" ]; s = set(newList);
# print(s);
# print(list(s)[2]);

# listNum = [ 1, 2, 3, 4, 5];
# listNum = [item * 2 for item in listNum]; 
# print(listNum);

# List Comprehension
# def times2(num) : 
#     return num * 3;

# listNum = [ 1, 2, 3, 4, 5];
# listNum = [times2(item) for item in listNum];
# print(listNum);

# Without Lambda
# def times2(num) : 
#     return num * 2;
# listNum = [ 1, 2, 3, 4, 5];
# listNum = set(map(times2, listNum));
# print(listNum);

# def genap(num) :
#     return num % 2 == 0;
# listNum = [ 1, 2, 3, 4, 5];
# listNum = list(filter(genap, listNum));
# print(listNum);

# With Lambda

# listNum = [ 1, 2, 3, 4, 5];
# listNum = list(map(lambda num: num * 2, listNum)); 
# print(listNum);

# listNum = [ 1, 2, 3, 4, 5];
# listNum = list(filter(lambda num: num % 2 == 0, listNum)); 
# print(listNum);

# numList = [1,2,3]; 
# input = 'x';
# check1 = input in numList; 
# check2 = 'x' in ['x','y','z']; 
# check3 = 'ka' in 'kurakas';
# print(check1); 
# print(check2); 
# print(check3);

# Cara Buat Search Key
# listCuy = [ 'Merdeho', 'Hoho', 'Hehehe', 'Inhomie']
# print(listCuy)
# inputUser = input('Search Key :')

# def searchList(keyword,listCuy):
#    newList = list(filter(lambda item: keyword.lower() in item.lower(), listCuy));
#    return newList;

# searchedList = searchList(inputUser,listCuy);
# print(searchedList);

def mainMenu():
    return input('1. Lihat Semua Dictionary\n'+'2. Tambahkan New Dictionary\n'+'3. Filtering Isi Dictionary\n'+'4. Keluar\n' + 'Pilih Menu :')

def lihatFullDictionary (theDictionary):
    print('Full Dictionary : ')
    print('___________________________________________')
    print('|        Key        |        Value        |')
    print('____________________|______________________')
    for key in theDictionary :
        if(str(type(theDictionary[key])) == "<class 'str'>") :
            print("|    " + key + "  |   '" + theDictionary[key] + "'   |" )
        elif(str(type(theDictionary[key])) == "<class 'int'>") :
            print("|    " + key + "  |   '" + str(theDictionary[key]) + "'   |" )

def isiDictionary (theDictionary):
    inputKey = input("Isi Key :")
    inputJenis = input ("Value input 1 untuk string, 2 untuk number ? : ")
    if(inputJenis=='1'):
        inputValue = input("Valuenya : ")
        theDictionary[inputKey] = inputValue
    elif(inputJenis=='2') :
        inputValue = input("Valuenya : ")
        theDictionary[inputKey] = inputValue
    else :
        print( 'Bandel ya balik lagi gih ke menu')

def searchDictionary (theDictionary):
    inputSearch = input("Key Search : ")
    newDDictionary = {}
    for key in theDictionary:
        if(inputSearch.lower() in key.lower()):
            newDDictionary[key] = theDictionary[key]

    lihatFullDictionary(newDDictionary)

newDictionary = {}
while True :
    check = mainMenu()
    if(check == '1'):
        lihatFullDictionary(newDictionary)
    elif(check == '2'):
        isiDictionary(newDictionary)
    elif(check == '3'):
        searchDictionary(newDictionary)
    elif(check == '4'):
        print('Terimakasih, Jangan Bosen dan Sampai Jumpa Lagi yaaa')
        break