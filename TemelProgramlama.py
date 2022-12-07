##soru1
import random
zarmap={1:0,2:0,3:0,4:0,5:0,6:0}
for i in range(100):
   zar=random.randrange(1,7)
    print(zar)
    zarmap[zar]=zarmap[zar]+1
print("Sayıların dağılımı şu şekildedir=",zarmap)




##soru2
##def faktöriyel(sayi):
##    fakt=1
        
##    for i in range(1,sayi +1):
            
##        fakt*=i
##        faktliste.append(sayi)
##    print(fakt)
##sayi = int(input("Faktoriyeli Hesaplanacak Sayı: "))
##faktöriyel(sayi)
##print(faktliste)







##soru3
##saatlikucret = 20
##iscimap={}
##ort,top,count = 0,0,0

##while True:
##    count += 1
##    isimsoyad = input("isim, soyad: ")
    
##    if isimsoyad == "0":
##        break
##    
##    calismaSaati = int(input("calisma saati: "))
##    maas = calismaSaati*saatlikucret
##    iscimap[count] = [isimsoyad,maas]
##    top += iscimap[count][1]

##ort = top/(count-1)

##enyuksek = iscimap[1]

##for i in range(1,len(iscimap)+1):
##    if iscimap[i][1] > enyuksek[1]:
##        enyuksek = iscimap[i]
        
##print("isci:", iscimap)
##print("en yuksek maas alan isci:", enyuksek)
##print("ortalamadan yuksek alan isciler:")
##for i in range(1, len(iscimap)+1):
##    if iscimap[i][1] > ort:
##      print(iscimap[i])






#soru4
#def fonksiyon(x,y,z):
#    return (x**z+(x+y)**z/2**z)
#x=int(input("1.değeri giriniz="))
#y=int(input("2.değeri giriniz="))
#z=int(input("3.değeri giriniz="))
#print("Sonucunuz=",fonksiyon(x,y,z))
