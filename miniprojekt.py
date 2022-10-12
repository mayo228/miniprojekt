import turtle
import math
gus=turtle.Turtle()                                         #zvola sa Turtle, vytvori sa novy objekt typu turle a vrati ho, ten je priradeny k nazvu gus
gus.speed(0)                                                #nastavi rychlost korytnacky na max
gus.pensize(1)                                              #nastavy sirku ciary pera
                           
def krivka(t, n, dlzka, uhol):                              #zadefinovanie funkcie pre krivku
    for i in range(n):
        t.fd(dlzka)                                         
        t.lt(uhol)
        
def obluk(t, r, uhol):
    dlzka_obluka = 2 * math.pi * r * abs(uhol) / 360        #vzorec na vypocet dlzky obluka pomocou vzorca na obvod kruhu krat uhol useku  
    n = int(dlzka_obluka / 4) + 4                           #nastavim kvalitu vykreslenia - cim vacsie n, tym viac vykreslenia
    krok_dlzka = dlzka_obluka / n
    krok_uhol = float(uhol) / n
    krivka(t, n, krok_dlzka, krok_uhol)                     #pomocou funkcie krivka postupne vykreslim pozadovany obluk 
    
def lupen(t, r, uhol,color1,color2):                        #zadefinuje funkciu ktora vykresli lupienok z dvoch oblukov
    t.color(color1,color2)                                  #zvolenie farby, color1 ciara, color2 vnutro objektu
    t.begin_fill()                                          #zaciatok plnenie objektu farbou
    for i in range(2):                                      #loop v rozsahu 2 pre 2 obluky lupienka
        obluk(t, r, uhol)                                   #pouzijem funkciu obluk pre vykreslenie dvoch kriviek lupna
        t.lt(180-uhol)                                      #otocim turtle tak aby sa vykreslil druhy obluk do opacneho smeru
    t.end_fill()                                            #koniec plnenia farbou
    
def kvet(t, n, r, uhol,color1,color2):                      #zadefinovanie funckcie pre vykreslenie kvetu s n lupienkami a farbami lupnov
    for i in range(n):                                      #loop sa vykona tolko krat kolko lupienkov chceme mat
        lupen(t, r, uhol,color1,color2)                     #pomocu funkcie lupen vykreslim 1 lupen pozostavajuci z 2 oblukov
        t.lt(360.0/n)                                       #pointer sa otoci vlavo o X stupnou podla toho, kolko lupienkov chcem mat na kvete

def stonka(t, r, uhol):                                     #zadefinovanie funkcie pre vykreslenie stonky 
    t.color("darkgreen")                                    #nastavenie plniacej farby 
    t.seth(270)                                             #nastavte orientaciu korytnacky do defaultneho smeru
    t.rt(uhol/2)                                            #nastavenie uhla korytnacky tak aby sa mi vykreslila z x do x
    obluk(t, r, uhol)                                       #pouzitie funkcie obluk na vykreslenie stonky
    t.seth(90)                                              #nastavi smer korytnacky na sever
    
def listy(t, r, uhol, uhol_listov):                         #zadefinovanie funkcie na vykreslenie listov 
    t.color("darkgreen","green")                            #nastavenie plniacej farby
    t.begin_fill()                                          
    t.lt(uhol_listov/2)                                     #natocenie korytnacky o polovicu uhla medzi nimi pre dosiahnutie symetrie
    for j in range(2):
        for i in range(2):                                  #loop v rozsahu 2 pre 2 obluky lupienka
            obluk(t, r, uhol)                               #pouzijem funkciu obluk pre vykreslenie dvoch kriviek lupna
            t.lt(180-uhol)                                  
        uhol=uhol*(-1)                                      #otoci poradie v ktorom sa listy vykresluju
        t.rt(uhol_listov)                                   
    t.end_fill()

    

def pozicia(t, dlzka_posunu):                               #zadefinovanie funkcie pre posun pera 
    t.pu()                                                  #zdvih pera
    t.setpos(0,0)                                           #nastavenie pozicie na suradnice x=0;y=0
    t.seth(0)                                               #nastavenie smeru pera na sever (vratenie do povodnej pozicie)
    t.fd(dlzka_posunu)                                      #posun doprava o zadanu vzdialenost
    t.pd()                                                  #polozenie pera
#----------------------------------------------------------------------------------
#   vykreslenie
#   pozicia(gus, vzdialenost)
#   kvet(gus, pocet lupienkov, polomer, uhol)
#   stonka(gus, polomer, uhol)
#   listy(gus, polomer, sirka (uhol) listu, uhol 2 listov)
#----------------------------------------------------------------------------------

pozicia(gus, -250.0)

kvet(gus, 7, 60.0, 60.0,"maroon","orange")
stonka(gus, 100.0, 90.0)
listy(gus, 90.0, 30.0, 100.0)

pozicia(gus, 0.0)

kvet(gus, 10, 50.0, 75.0,"gold", "yellow")
stonka(gus, 300.0, 45.0)
listy(gus, 280.0, 20.0, 30.0)

pozicia(gus, 200.0)

kvet(gus, 20, 140.0, 20.0, "indigo","indigo")
stonka(gus, 350.0, 25.0)
listy(gus, 90.0, 85.0, 1.0)

"""
kvet(gus, 13, 50.0, 70.0, "darkred","red")
stonka(gus, 300.0, 45.0)
listy(gus, 80.0, 70.0, 30.0)
"""

gus.hideturtle()
turtle.mainloop()
