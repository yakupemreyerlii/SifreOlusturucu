import random

#KULLANACAĞI KARAKTERLER
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
#Uzunluk Alınıyor
parola_uzunlugu = int(input("Parolanın uzunluğunu girin: "))

olusturulan_parola = ""


for i in range(parola_uzunlugu):
    olusturulan_parola += random.choice(karakterler)

#Kod Çıktısı Veriliyor
print("Oluşturulan Parola:", olusturulan_parola)
