import sqlite3
from defs import *



tabloyap()

istemci=0
sayi=0
dosya=open("uyesayi.txt","r")
sayi=int(dosya.read())
dosya.close()
bilgi=[]
while(1):
    if istemci!=1 and istemci!=2:
        sorgu=int(baslangicmenu())
        if sorgu==1:
            while 1:
                musteri_ad=input("Adınızı giriniz : ")
                musteri_tel=input("Telefon no giriniz : ")
                musteri_tc=input("TC no giriniz : ")
                musteri_sifre=input("Şifre giriniz : ")
                if musteri_ad!="" and len(musteri_tc)==11 and musteri_sifre!="":
                    kayit(musteri_ad,musteri_tel,musteri_tc,musteri_sifre)
                    print("kayıt başarılı")
                    break
                else:
                    print("yanlış giriş yaptınız")
        elif sorgu==2:
            while 1:
                giris_ad=input("Adınızı giriniz : ")
                giris_sifre=input("Şifrenizi giriniz : ")
                if giris_ad!="" and giris_sifre!="":
                    ad_bilgi,tel_bilgi,tc_bilgi=musterigiris(giris_ad,giris_sifre)
                    if ad_bilgi!=None:
                        print("girişiniz başarıyla yapılmıştır sayın {}".format(ad_bilgi))
                        istemci=1
                        break
                    else:
                        print("böyle bir hesap bulunamadı")
                else:
                    print("isim veya şifre boş geçilemez ")
                
        elif sorgu==3:
            while 1:
                giris_ad=input("Adınızı giriniz : ")
                giris_sifre=input("Şifrenizi giriniz : ")
                if giris_ad!="" and giris_sifre!="":
                    ad_bilgi,tel_bilgi,tc_bilgi=resepsiyongiris(giris_ad,giris_sifre)
                    if ad_bilgi!=None:
                        print("girişiniz başarıyla yapılmıştır sayın {}".format(ad_bilgi))
                        istemci=2
                        break
                    else:
                        print("böyle bir hesap bulunamadı")
                else:
                    print("isim veya şifre boş geçilemez ")
        elif sorgu==4:
            break
        else:
            print("yanlış tuşlama yaptınız tekrar deneyiniz")
    else:
        break


if istemci==1:
    while 1:
        sorgu=int(musterimenu())
        if sorgu==1:      
            fiyat=0     
            print("bilgi kral suit harici kişi sayısı fiyatı etkilemektedir")
            rezervasyon_odatipi=int(input("oda tipi tuşlayınız standart (1) 1000tl , vip (2) 4000tl , kral suit (3) 20.000tl : "))
            rezervasyon_kisisayisi=int(input("kişi sayısı giriniz : "))
            rezervasyon_tarih=input("Rezervasyon tarihi giriniz : ")
            if rezervasyon_odatipi==1:
                fiyat=1000*rezervasyon_kisisayisi
            elif rezervasyon_odatipi==2:
                fiyat=4000*rezervasyon_kisisayisi
            elif rezervasyon_odatipi==3:
                fiyat=20000
            else:
                print("yanlış tuşlama yaptınız ")
                break
            if rezervasyon_odatipi!=None and rezervasyon_kisisayisi!=None and rezervasyon_tarih!=None :
                rezervasyonkayit(ad_bilgi,tel_bilgi,tc_bilgi,rezervasyon_odatipi,rezervasyon_kisisayisi,rezervasyon_tarih,fiyat)
                print("rezervasyonunuz oluşturuldu")
                dosya1=open("uyesayi.txt","w")
                sayi+=1
                dosya1.write(str(sayi))
                dosya1.close()
            else:
                print("yanlış giriş yaptınız menüye yönlendiriliyorsunuz : ")

        elif sorgu==2:
            print("hangi rezervasyonu güncellemek istiyorsanız ona ait tarihi giriniz . ")
            eski_tarih=input("Rezervasyon tarihi giriniz : ")
            onay=int(guncelara(tc_bilgi,ad_bilgi,eski_tarih))
            if onay==1:
                fiyat=0    
                print("YENİ BİLGİLER") 
                print("bilgi kral suit harici kişi sayısı fiyatı etkilemektedir")
                rezervasyon_odatipi=int(input("oda tipi tuşlayınız standart (1) 1000tl , vip (2) 4000tl , kral suit (3) 20.000tl : "))
                rezervasyon_kisisayisi=int(input("kişi sayısı giriniz : "))
                rezervasyon_tarih=input("Rezervasyon tarihi giriniz : ")
            if rezervasyon_odatipi==1:
                fiyat=1000*rezervasyon_kisisayisi
            elif rezervasyon_odatipi==2:
                fiyat=4000*rezervasyon_kisisayisi
            elif rezervasyon_odatipi==3:
                fiyat=20000
            else:
                print("yanlış tuşlama yaptınız ")
                break
            if rezervasyon_odatipi!=None and rezervasyon_kisisayisi!=None and rezervasyon_tarih!=None :
                rezervasyonguncelle(ad_bilgi,tel_bilgi,tc_bilgi,rezervasyon_odatipi,rezervasyon_kisisayisi,rezervasyon_tarih,eski_tarih,fiyat)
                print("rezervasyonunuz guncellendi")
            else: 
                print("bu bilgilere sahip rezervasyon bulunamadı . ")  

        elif sorgu==3:              
            print("hangi rezervasyonu silmek istiyorsanız ona ait tarihi giriniz . ")
            rezervasyon_tarih=input("Rezervasyon tarihi giriniz : ")
            onay=int(silmeara(tc_bilgi,ad_bilgi,rezervasyon_tarih))
            if onay==1:
                rezervasyonsilme(tc_bilgi,ad_bilgi,rezervasyon_tarih)
                print("rezervasyonunuz silindi")
            else: 
                print("bu bilgilere sahip rezervasyon bulunamadı . ")  

        elif sorgu==4:
            liste=listele(ad_bilgi,tel_bilgi,tc_bilgi)
            if liste!=None:
                print("Sayın {} , Rezervasyon bilgileriniz ; Oda tipi : {} , Kişi sayısı : {} , Tarihi : {} , Fiyatı : {}".format(liste[1],liste[3],liste[4],liste[5],liste[6]))
            else:
                print("malesef rezervasyon bulunamadı")
        elif sorgu==5:
            break
        else:
            print("düzgün tuşlayınız")

if istemci==2:
    while 1:
        sorgu=int(resepsiyonmenu())
        if sorgu==1:
            print("hangi rezervasyonu iptal etme istiyorsanız ona ait bilgileri giriniz . ")
            rezervasyon_tarih=input("rezervasyon tarihi giriniz : ")
            musteri_ad=input("iptal etmek istediğiniz müşteriye ait ad giriniz : ")
            musteri_tc=input("iptal etmek istediğiniz müşteriye ait tc giriniz : ")
            onay=int(resepsiyonistsilmeara(musteri_tc,musteri_ad,rezervasyon_tarih))
            if onay==1:
                resepsiyonistsilme(musteri_tc,musteri_ad,rezervasyon_tarih)
                print("rezervasyon iptal edildi")
            else: 
                print("bu bilgilere sahip rezervasyon bulunamadı . ")  

        elif sorgu==2:
            dosya2=open("uyesayi.txt","r")
            sayi=dosya2.read()
            print("şu ana kadar rezervasyon yapan kişi sayısı : {}".format(sayi))
            dosya2.close()
            
        else:
            break