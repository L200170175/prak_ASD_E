class MhsTIF(object):
    def __init__(self, nama, umur, kota, us):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__(self):
        x = self.nama + ', umur' + str(self.umur) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku ' + str(self.uangSaku) \
            + 'tiap bulannya.'
        return x

    def ambilNama(self):
        return self.nama
    def ambilUmur(self):
        return self.umur
    def ambilKota(self):
        return self.kotaTinggal
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF('Listian', 10, 'Sukoharjo', 240000)
c1 = MhsTIF('Tidhar', 14, 'Klaten', 250000)
c2 = MhsTIF('Annas', 12, 'Surakarta', 295000)
c3 = MhsTIF('Yoga', 21, 'Wonogiri', 235000)
c4 = MhsTIF('Rendra', 20, 'Salatiga', 350000)
c5 = MhsTIF('Faisal', 65, 'Purworejo', 140000)
c6 = MhsTIF('Ino', 11, 'Bandung', 440000)
c7 = MhsTIF('Dandi', 43, 'Surabaya', 2750000)
c8 = MhsTIF('Fredi', 56, 'Purwodadi', 220000)
c9 = MhsTIF('Rifqi', 6, 'Salatiga', 165000)
c10 = MhsTIF('Rozin', 20, 'Purwodadi', 140000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def cariKota(target):
    y = []
    for i in Daftar:
        if i.kotaTinggal == target:
            hasil = Daftar.index(i)
            y.append(hasil)
    return y
#No2
def cariTerkecil(Daftar):
    n = len(Daftar)
    #Anggap item pertama adalah yang terkecil
    terkecil = Daftar[0]
    #tentukan apakah item lain lebih kecil
    for i in range(1,n):
        if Daftar[i].uangSaku < terkecil.uangSaku:
            terkecil = Daftar[i]

    return terkecil

#No3
def cariTerkecil(Daftar):
    n = len(Daftar)
    #Anggap item pertama adalah yang terkecil
    terkecil = [Daftar[0]]
    #tentukan apakah item lain lebih kecil
    for i in range(1,n):
        if Daftar[i].uangSaku < terkecil[0].uangSaku:
            terkecil = [Daftar[i]]
        elif Daftar[i].uangSaku == terkecil[0].uangSaku:
            terkecil.append(Daftar[i])
    return terkecil

#No4
def cariDaftarUangSakuKurang(kumpulan):
    b = []  
    for i in kumpulan:
        if i.uangSaku < 250000:
            terkecil = i.uangSaku
            b.append(kumpulan.index(i))
    return b
