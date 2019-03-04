import random

def permainan():
    a=random.randrange(0, 100)
    while(True):
        print('Permainan Tebak Angka.')
        print('Saya menyimpan sebuah angka bulat antara 1 sampai 100, Coba tebak')
        b=int(input("Masukkan tebakan : "))
        if(b>a):
            print("Itu terlalu besar. Coba lagi")
        elif(b<a):
            print("Itu terlalu kecil, Coba lagi")
        else:
            print("Ya. Anda Benar")
            break
        
permainan()
