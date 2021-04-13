class Ucak:
    def __init__(self,Ucak_Adı,Ucak_Kodu,Uçak_Türü,Üretim_Yılı,Yolcu_Kapasitesi):
        self.Ucak_Adı=Ucak_Adı
        self.Ucak_Kodu=Ucak_Kodu
        self.Uçak_Türü=Uçak_Türü
        self.Üretim_Yılı=Üretim_Yılı
        self.Yolcu_Kapasitesi=Yolcu_Kapasitesi
        self.durum=True
    def Ucak_Bakim_Tanımla(self,durum):
        self.durum=durum
        return durum
    def Ucak_Bakim_Durum(self):
        if self.durum==True:
            return f"ucagin bakim durumu iyi."
        elif self.durum==False:
            return f" ucga uzun suredir bakim yapilmadi."
        

class Yolcu:
    def __init__(self,Yolcu_Adı_Soyadı,Yolcu_TC,Yolcu_Yaşı):
        self.Yolcu_Adı_Soyadı=Yolcu_Adı_Soyadı
        self.Yolcu_TC=Yolcu_TC
        self.Yolcu_Yaşı=Yolcu_Yaşı
        self.mil=0
    def Mil_Ekle(self,ödediği_tutarın):
        self.mil=self.mil+ödediği_tutarın*0.1
        return self.mil
    def Mil_Goster(self):
        print(self.mil)
    def Yolcu_Bilgi_Goster(self):
        print(f"{self.Yolcu_Adı_Soyadı} {self.Yolcu_Yaşı} {self.Yolcu_TC} ")   

class Ucus:
    

    def __init__(self,Uçuş_Adı,Uçuş_Kodu,Uçuş_Tarihi,Kalkış_Yeri, İniş_Yeri):  
        self.Uçuş_Adı=Uçuş_Adı
        self.Uçuş_Kodu=Uçuş_Kodu
        self.Uçuş_Tarihi=Uçuş_Tarihi
        self.Kalkış_Yeri=Kalkış_Yeri
        self.İniş_Yeri=İniş_Yeri
        self.yolcu_listesi=[]
        self.ucak_bilgi=[]
        self.ucak_kapatsite=0
        self.yolcu_sayi=0
    def Ucus_Ucagi_Ekle(self,Ucak_Adı,Ucak_Kodu,Uçak_Türü,Üretim_Yılı,Yolcu_Kapasitesi):
        self.ucak_bilgi=[Ucak_Adı,Ucak_Kodu,Uçak_Türü,Üretim_Yılı,Yolcu_Kapasitesi]
        self.ucak_kapatsite=Yolcu_Kapasitesi
        d=Ucak(Ucak_Adı,Ucak_Kodu,Uçak_Türü,Üretim_Yılı,Yolcu_Kapasitesi)
        return d
    def Yolcu_Ekle(self,Yolcu_Adı_Soyadı,Yolcu_TC,Yolcu_Yaşı):
        self.yolcu_sayi+=1
        if self.yolcu_sayi<=self.ucak_kapatsite:
            self.yolcu_listesi.append([Yolcu_Adı_Soyadı,Yolcu_TC,Yolcu_Yaşı])
            f=Yolcu(Yolcu_Adı_Soyadı,Yolcu_TC,Yolcu_Yaşı)
            return f
        else:
            raise "kapasite ashildi"
    def Yolcu_Goster(self):
        for x in self.yolcu_listesi:
            print(f'yolcu adı soyadı:{x[0]} \n Yolcu TC :{x[1]} \n Yolcu yaşı: {x[2]}\n')

    def Ucus_Bilgi_Goster(self):
        print(f'uçuş bilgileri \n uçuş adı{self.Uçuş_Adı}, uçuş kodu {self.Uçuş_Kodu}\n uçuş tarihi{self.Uçuş_Tarihi}\n kalkış yeri{self.Kalkış_Yeri}\n,iniş yeri{self.İniş_Yeri}')
        


uc_1=Ucus("TK223",54665,"23 nisan","italya","iran")
ucak=uc_1.Ucus_Ucagi_Ekle("goksin",323432,"motorlu",2019,5)

yolcu_1=uc_1.Yolcu_Ekle("ozge",2532534,18)
mil_1=yolcu_1.Mil_Ekle(230)
yolcu_1.Mil_Goster()

yolcu_2=uc_1.Yolcu_Ekle("deniz",344343,23)
mil_1=yolcu_2.Mil_Ekle(240)
yolcu_2.Mil_Goster()

yolcu_3=uc_1.Yolcu_Ekle("halime",65467675,14)
mil_1=yolcu_1.Mil_Ekle(440)
yolcu_1.Mil_Goster()
yolcu_1=uc_1.Yolcu_Ekle("goknur",7677676,56)
mil_1=yolcu_1.Mil_Ekle(440)
yolcu_1.Mil_Goster()
yolcu_1=uc_1.Yolcu_Ekle("ilahe",5665656,45)
mil_1=yolcu_1.Mil_Ekle(440)
yolcu_1.Mil_Goster()
uc_1.Yolcu_Goster()


