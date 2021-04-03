class ticket_plaim:
    def __init__(self):
        self.liste=[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0]]
    def ticket_buy(self):
        print("merhabalar bilet revarvasyonuzu yapin \n eger sigara icilen bo;ume isdiyorsaniz 1 \n icilmeyen bolume isdiyorsaniz 2\n basin.")
        x=int(input(" "))
        k=0
        liste=self.liste
        for d in liste:
                if d[1]==1:
                        k+=1
        if (k==10):
            print(" bos yer yok . gelecek uçuş 3 saat sonra")
            x=0
        if (x==1):
            a=0
            print(' 0 la yazilan yer bos 1 le yazilan yer dolu')
            print(f" 1 nci yer:{liste[0][1]} \n 2 in ci yer {liste[1][1]} \n 3 in ci yer {liste[2][1]} \n 4 in ci yer {liste[3][1]} \n 5 in ci yer {liste[4][1]}")
            for x in range(5):
                if liste[x][1]==1 :
                    a+=1
            if(a==5):
                print( "yerler dolu sigarasiz bolume gecmek isdiyormusunuz?(evet ve ya hayir girin.)")
                d=input()
                s=d.lower()
                if s=="evet":
                    x=2
                else:
                    print("gelecek uçuş 3 saat sonra")  
            else:     
                j=int(input("hangi yeri isdiyorsunuz?"))
                if (liste[j-1][1]==0):
                    liste[j-1]=[j,1]
                    print(f"{j} yeriniz. rezarve edildi iyi")
                else:
                    print(" bu yer tutuludur. yanlis akt") 
        if(x==2):
            a=0
            print(' 0 la yazilan yer bos 1 le yazilan yer dolu')
            print(f" 6 nci yer:{liste[5][1]} \n 7 in ci yer {liste[6][1]} \n 8 in ci yer {liste[7][1]} \n 9 in ci yer {liste[8][1]} \n 10 in ci yer {liste[9][1]}")
            for x in range(5,10):
                if liste[x][1]==1:
                    a+=1
            if(a==5):
                    print( "yerler dolu sigarali bolume gecmek isdiyormusunuz?(evet ve ya hayir girin.)")
                    d=input()
                    s=d.lower()
                    if s=="evet":
                        print(' 0 la yazilan yer bos 1 le yazilan yer dolu')
                        print(f" 1 nci yer:{liste[0][1]} \n 2 in ci yer {liste[1][1]} \n 3 in ci yer {liste[2][1]} \n 4 in ci yer {liste[3][1]} \n 5 in ci yer {liste[4][1]}")
                        j=int(input("hangi yeri isdiyorsunuz?"))
                        if (liste[j-1][1]==0):
                            liste[j-1]=[j,1]
                            print(f"{j} yeriniz. rezarve edildi iyi")
                        else:
                            print(" bu yer tutuludurç yanlıs akt.")
                    else:
                        print("gelecek uçuş 3 saat sonra")  
            else:     
                j=int(input("hangi yeri isdiyorsunuz?"))
                if (liste[j-1][1]==0):
                                liste[j-1]=[j,1]
                                print(f"{j} yeriniz. rezarve edildi iyi")
                else:
                                print(" bu yer tutuludurç yanlıs akt.")
s=ticket_plaim
print(s.ticket_buy)