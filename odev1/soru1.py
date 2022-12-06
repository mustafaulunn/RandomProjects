ogrenci = {}
ort = 0
top = 0

# hızlı test etmek için range 1, 4 (3 öğrenci)
for i in range(1,4):
    
    print("******ogrenci {}*******".format(i))
    
    for n in range(1,6):
        puan = int(input(("ders {}: ".format(n))))
        top += puan
        
    ort = top/5
    ogrenci["ogrenci{}".format(i)] = (ort)
    ort, top = 0, 0

print("ogrencilerin not ortalamasi:", ogrenci)
print("ortalama siralamasi:", sorted(ogrenci.values(), reverse=True))
print("en yuksek ortalama:", max(ogrenci, key=ogrenci.get))
