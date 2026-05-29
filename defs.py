import sqlite3 as sql
vt=sql.connect("veritabani.db")
imlec=vt.cursor()
"""İŞLEM FONKSİYONLARI"""
def baslangicmenu():
    soru=input(""" 
    1-Müşteri Üyeliği
    2-Müşteri Girişi
    3-Resepsiyon Girişi
    4-Çıkış
    TUŞLAYINIZ : 
    """)
    return soru

def musterimenu():
    soru=input("""
    Müşteri Menüsü
    1-Rezervasyon al
    2-Rezervasyon güncelle
    3-Rezervasyon iptal
    4-Rezervasyon listele
    5-Çıkış
    TUŞLAYINIZ :
    """)
    return soru

def resepsiyonmenu():
    soru=input("""
    Resepsiyonist Menüsü
    1-Kayıt iptal
    2-Çıkış
    TUŞLAYINIZ :
    """)
    return soru



""" VERİTABANI FONKSİYONLARI"""
"""
1.kısım
"""
"""giris işlem"""
def tabloyap():
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    imlec.execute(""" CREATE TABLE IF NOT EXISTS musteribilgi(ID integer PRIMARY KEY,ad TEXT,tel TEXT,tc TEXT,sifre TEXT )""")
    imlec.execute(""" CREATE TABLE IF NOT EXISTS resepsiyonistbilgi(ID integer PRIMARY KEY,ad TEXT,tel TEXT,tc TEXT,sifre TEXT )""")
    imlec.execute(""" CREATE TABLE IF NOT EXISTS rezervasyonbilgi(tc TEXT,ad TEXT,tel TEXT,oda_tipi TEXT,kac_kisi TEXT,rezervasyon_tarih TEXT,rezervasyon_fiyat TEXT)""")
    vt.commit()
    vt.close()

def kayit(ad,tel,tc,sifre):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    ekleme="""INSERT INTO musteribilgi(ad,tel,tc,sifre) VALUES {}"""
    veri=(ad,tel,tc,sifre)
    imlec.execute(ekleme.format(veri))
    vt.commit()
    vt.close()

def musterigiris(ad,sifre):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    arama="""SELECT *FROM musteribilgi where ad = '{}' and sifre='{}'"""
    imlec.execute(arama.format(ad,sifre))
    liste=imlec.fetchone()
    if liste!=None:
        vt.close()
        return liste[1],liste[2],liste[3]   
    else:
        bos=""
        vt.close()
        return bos

def resepsiyongiris(ad,sifre):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    arama="""SELECT *FROM resepsiyonistbilgi where ad = '{}' and sifre='{}'"""
    imlec.execute(arama.format(ad,sifre))
    liste=imlec.fetchone()
    
    if liste!=None:
        vt.close()
        return liste[1],liste[2],liste[3]    
    else:
        bos=""
        vt.close()
        return bos
    
"""
2.kısım
"""
"""hasta işlem"""
def rezervasyonkayit(ad,tel,tc,odatipi,kisisayisi,tarih,fiyat):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    rkayit="""INSERT INTO rezervasyonbilgi(tc,ad,tel,oda_tipi,kac_kisi,rezervasyon_tarih,rezervasyon_fiyat) VALUES ('{}','{}','{}','{}','{}','{}','{}')"""
    imlec.execute(rkayit.format(tc,ad,tel,odatipi,kisisayisi,tarih,fiyat))
    vt.commit()
    vt.close()

def guncelara(tc,ad,tarih):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    ara="""SELECT *FROM rezervasyonbilgi where tc='{}'and ad='{}'and rezervasyon_tarih='{}'"""
    imlec.execute(ara.format(tc,ad,tarih))
    liste=imlec.fetchone()
    if liste!=None:
        vt.close()
        return 1
    else:
        vt.close()
        return 0
    
def rezervasyonguncelle(ad,tel,tc,odatip,kisisayisi,tarih,eskitarih,fiyat):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    guncelle="""UPDATE rezervasyonbilgi SET oda_tipi='{}' , kac_kisi='{}' , rezervasyon_tarih='{}' , rezervasyon_fiyat='{}' where tc='{}' and ad='{}' and tel='{}' and rezervasyon_tarih='{}'"""
    imlec.execute(guncelle.format(odatip,kisisayisi,tarih,fiyat,tc,ad,tel,eskitarih))
    vt.commit()
    vt.close()

def silmeara(tc,ad,tarih):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    ara="""SELECT *FROM rezervasyonbilgi where tc='{}'and ad='{}' and rezervasyon_tarih='{}'"""
    imlec.execute(ara.format(tc,ad,tarih))
    liste=imlec.fetchone()
    if liste!=None:
        vt.close()
        return 1
    else:
        vt.close()
        return 0
    
def rezervasyonsilme(tc,ad,tarih):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    silme="""DELETE FROM rezervasyonbilgi where tc='{}' and ad='{}' and rezervasyon_tarih='{}' """
    imlec.execute(silme.format(tc,ad,tarih))
    vt.commit()
    vt.close()

def listele(ad,tel,tc):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    gorme="""SELECT *FROM rezervasyonbilgi where ad='{}' and tel='{}' and tc='{}'"""
    imlec.execute(gorme.format(ad,tel,tc))
    liste=imlec.fetchone()
    vt.close()
    return liste 

"""3.kısım"""
"""resepsiyonist"""
def resepsiyonistsilmeara(tc,ad,tarih):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    ara="""SELECT *FROM rezervasyonbilgi where tc='{}' and ad='{}' and rezervasyon_tarih='{}'"""
    imlec.execute(ara.format(tc,ad,tarih))
    liste=imlec.fetchone()
    if liste!=None:
        vt.close()
        return 1
    else:
        vt.close()
        return 0

def resepsiyonistsilme(tc,ad,tarih):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    silme="""DELETE FROM rezervasyonbilgi where tc='{}' and ad='{}' and rezervasyon_tarih='{}'"""
    imlec.execute(silme.format(tc,ad,tarih))
    vt.commit()
    vt.close()

