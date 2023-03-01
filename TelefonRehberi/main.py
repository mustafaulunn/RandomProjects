import mysql.connector

veritabanim=mysql.connector.connect(
host="",
user="",
password="",
database="contact"

)



def kisi_ekle(): ##kisi ekleme fonksiyonu
    isim= input()
    numara= input()
    mail= input()
    memleket= input()
    baglanti = veritabanim.cursor()
    sql = "INSERT INTO Contact(isim,numara,mail,memleket) VALUES (%s,%s,%s,%s)"
    record = (isim, numara, mail, memleket)
    baglanti.execute(sql, record)
    veritabanim.commit()
    baglanti.close()
    print("kayit basarili\n")



def kayit_sil(isim):
    baglanti= veritabanim.cursor()
    sql = "DELETE from Contact WHERE isim = %s"
    value=(isim)
    baglanti.execute(sql, value)
    veritabanim.commit()
    if baglanti.rowcount(0):
        print("kayit bulunamadi")
    else:
        print("kayit silindi")
        veritabanim.close()



def kayit_ara(isim):
    baglanti=veritabanim.cursor()
    sql="select * from contact where isim = %s"
    value=(isim)
    baglanti.execute(sql,value)
    kayit = baglanti.fetchone()
    if kayit== None:
        print("No such record exists")
    else:
        print('isim:', kayit[0])
        print('adres:', kayit[1])
        print('numara:', kayit[2])
        print('mail:', kayit[3])
        print('memleket',kayit[4])


def kayitlari_goster(kayit=None):
    baglanti = veritabanim.cursor()
    baglanti.execute("select * from Contact")
    print('{0:20}{1:30}{2:15}{3:30}'.format('isim','adres','numara','mail','memleket'))
    for record in baglanti:
        print('{0:20}{1:30}{2:15}{3:30}{4:30}'.format(kayit[0], kayit[1], kayit[2], kayit[3], kayit[4]))
    baglanti.close()




def kayit_duzenle(isim):
    baglanti=veritabanim.cursor()
    baglanti.execute("select * from Contact")
    value=(isim,)
    record=baglanti.fetchone()
    if record==None:
        print("Bsyle bir sey bulamadik")
    else:
        while True:
            print("istegin ne gardas")
            print("1-Ad degistireceim gardas ne sandin")
            print("2-numaramin telleri")
            print("3--Adres degistirecegim")

            print("4-Mail degistirecegim")
            print("5-Memleklet degisir mi hiç")
            print("6- Geri Dsn")
            print()
            ch = int(input("Seç bakim (1-5): "))
            if ch==1:
                yeni_isim=input("yeni isim giriniz")
                sql = "UPDATE kisiler SET isim = %s WHERE isim = %s"
                values = (yeni_isim, isim)
                baglanti.execute(sql,values)
                veritabanim.commit()
                print(baglanti.rowcount, "kaydiniz guncellendi")

            elif ch==2:
                yeni_numara = input("yeni numara giriniz")
                sql = "UPDATE Contact SET numara = %s WHERE isim = %s"
                values = (yeni_numara, isim)
                baglanti.execute(sql, values)
                veritabanim.commit()
                print(baglanti.rowcount, "kaydiniz guncellendi")


            elif ch==3:
                yeni_adres= input("yeni adres giriniz")
                sql="UPDATE kisiler SET adres =%s WHERE isim= %s"
                valued=(yeni_adres,isim)
                baglanti.execute(sql,isim)
                veritabanim.commit()
                print(baglanti.rowcount,"kaydin guncellendi")
            elif ch==4:
                yeni_mail = input("yeni mail giriniz")
                sql = "UPDATE contact SET mail =%s WHERE isim= %s"
                valued = (yeni_mail, isim)
                baglanti.execute(sql, isim)
                veritabanim.commit()
                print(baglanti.rowcount, "kaydin guncellendi")


            elif ch==5:
                yeni_memleket= input("memleketini degistir")
                sql = "UPDATE contact SET memleket =%s WHERE isim= %s"
                valued = (yeni_memleket, isim)
                baglanti.execute(sql, isim)
                veritabanim.commit()
                print(baglanti.rowcount, "kaydin guncellendi")


            elif ch==6:
                break

            else:
                baglanti.close()


def menu(isim=5):
    print("Ana Menuye Hosgeldiniz")
    print("Kisi Eklemek icin 1'e basiniz")
    print("kayit silmek icin 2'ye basiniz")
    print("kayit aramak icin 3'e basiniz")
    print("kayitlari gsstermek için 4'e basin")
    print("kayit duzenlemek için 5' basin")
    input("sayi giriniz")

kisi_ekle()




        
##menu()

































