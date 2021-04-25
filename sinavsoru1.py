class YazOkuluDersler :
    def __init__(self,dersinadı, kodu, Esogükontenjanı, dersingünvesaat):
        self.dersinadi=dersinadı
        self.kodu=kodu
        self.Esogükontenjanı=Esogükontenjanı
        self.dersingünvesaat=dersingünvesaat
        self.ogrencibilgi=[]
    def KontenjanGuncelle(self,yabancıöğrencikontenjanı):
            if yabancıöğrencikontenjanı/100*50<self.Esogükontenjanı:
                self.yabancıöğrencikontenjanı=yabancıöğrencikontenjanı
            else:
                input("yabancıöğrencikontenjanı dogru gir")
        
        
    def OgrenciEkle (self,ÖğrenciNo,isimsoyisim,Ögrencitürü):
        self.ogrencibilgi.append([ÖğrenciNo,isimsoyisim,Ögrencitürü])
        print("eklendi")
    def OgrenciSil(self,numaragir):
        a=0
        for x in self.ogrencibilgi:
            if x[0]==numaragir:
                self.ogrencibilgi.pop(a)
                return f"silindi "
            a+=1
        return " ogrenci yok"    
    def KayitliOgrencileriGoster(self):
        if len(self.ogrencibilgi)==0:
            print("Kayıtlı öğrenci bulunmamaktadır")
            return f"Kayıtlı öğrenci bulunmamaktadır"
        for x in self.ogrencibilgi:
            print(f"{x[0]} {x[1]} {x[2]} ")
    def DersTakvimGuncell(self,isdediyiniztakvim):
        self.dersingünvesaat=isdediyiniztakvim
        print("guncelendi")
d=YazOkuluDersler("Yapay Ağlar",121618505,50,"saat 3 pazar")
x=YazOkuluDersler("Bilgisayar Programlama II",121618503,67 ,"pazar 2")
d.OgrenciEkle(1234567 ,"Ali Demir" ,"ESOGÜ")
d.DersTakvimGuncell("3 saat  cuma")
d.KontenjanGuncelle(67)

d.KayitliOgrencileriGoster()


x.OgrenciEkle(1324567,"Ayşe Erdemir " ,"Dumlupınar")




        




        
        


