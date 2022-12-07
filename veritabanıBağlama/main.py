import mysql.connector

veritabanim=mysql.connector.connect(
host="******",
user="root",
password="****",
database="contact"

)

baglanti = veritabanim.cursor()
sql = "INSERT INTO Contact(ali,123445,alimail,izmir) VALUES (%s,%s,%s,%s)"

baglanti.execute(sql, record)
veritabanim.commit()
baglanti.close()
print("kayit basarili\n")
