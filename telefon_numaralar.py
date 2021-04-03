def telfonuyg():
    d=1
    degisken=0
    liste=[]
    while d==1:
        print(""" 
        Yeni Kişi Eklemek :1
        Kişi Sil Silmek   :2
                Kişi Bul  :3
            Kişi Düzenle  :4
        programdan Çıkış  :5
        """)


        while True:
            try:
                gir=int(input("\n"))
            except:
                print("rakam gir....\n")
            continue
            break
        



        if gir==1:
            z=input(" ad soyad    ")
            while True:
                try:
                    x=int(input(" telefon nnumara   "))            
                except:
                    print("dogru yaz... \n  ")
                    continue
                break
            if len(liste)!=0:
                ppp=0
                for q in liste:
                    ppp+=1
                    ok=0
                    if(x==q[1]):
                        print("\n.... numara daha önce kayıt edilmiş\n")
                        ok=78
                        continue
                    elif ppp==len(liste) and ok==0:
                        liste=liste+[[z,x]]
                        degisken+=1
                        print("basarili sekilde eklendi ")
            else:
                liste=liste+[[z,x]]
                degisken+=1
                print("basarili sekilde eklendi ")







        if gir==2:
            kok=0
            while True:
                try:
                    x=int(input(" silmek isdediginiz kisinin numarasini giriniz    "))
                except:
                    print("dogru yaz.....\n")
                    continue
                break
            if len(liste)!=0:
                for q in liste:
                    kok+=1
                    if(x==q[1]):
                        liste.remove(q)
                        degisken-=1
                        kok=89989
                        print("basarili sekilde silindi")
                    elif kok==len(liste):
                        print("numara bulunamadi")
            else:
                print("numara yok")






        if gir==3:
            print("numarami ile arama yapmak icin 1 \n ad soyad la arama yapmak icin 2")  
            x=int(input())
            if(x==1):
                lil=int(input("numarayi giriniz:   "))
                if len(liste)!=0:
                    lop=0
                    for q in liste:
                        lop+=1
                        if(lil==q[1]):    
                            print(f"isim soyisim :{q[0]} numara: {q[1]}")
                            lop=56656
                        elif(lop==len(liste)):
                            print("numara bulunamadi")
                else:
                    print("numara yok")    
            if(x==2):
                lil=input("ad soyad giriniz:   ")
                if len(liste)!=0:
                    lop=0
                    for q in liste:
                        lop+=1
                        if(lil==q[0]):    
                            print(f"isim soyisim :{q[0]} numara: {q[1]}")
                            lop=56656
                        elif(lop==len(liste)):
                            print("numara bulunamadi")
                else:
                    print("numara yok") 










        if gir==4:
            
            while True:
                try:
                    print("numarami ile  1 \n veya \n ad soyad  icin 2")
                    x=int(input())            
                except:
                    print("dogru yaz... \n  ")
                    continue
                break  
            if(x==1):
                while True:
                    try:
                        m=int(input("numarayi giriniz:   "))          
                    except:
                        print("dogru yaz... \n  ")
                        continue
                    break        
                if len(liste)!=0:
                    lop=0
                    j=0
                    for q in liste:
                        lop+=1
                        if(m==q[1]):    
                            print(f"isim soyisim :{q[0]} numara: {q[1]} duzenle:")
                            x=input("isim soyisim")
                            y=int(input("numara gir"))
                            liste[j]=[x,y]
                            lop=56656
                        elif(lop==len(liste)):
                            print("numara bulunamadi")
                        j+=1
                else:
                    print("numara yok")    
            if(x==2):
                m=input("ad soyad giriniz:   ")
                if len(liste)!=0:
                    lop=0
                    j=0
                    for q in liste:
                        lop+=1
                        if(m==q[0]):    
                            print(f"isim soyisim :{q[0]} numara: {q[1]}")
                            x=input("isim soyisim")
                            y=int(input("numara gir"))
                            liste[j]=[x,y]
                            lop=56656
                        elif(lop==len(liste)):
                            print("numara bulunamadi")
                        j+=1
                else:
                    print("numara yok")      
        


        if gir==5:
            print(f" {degisken} kadar numara var cikarsaniz silinicek eminseniz 1 girin isdemesensinizse 2 ye basin")
            x=int(input(""))
            if x==1:
                d=89

telfonuyg()

