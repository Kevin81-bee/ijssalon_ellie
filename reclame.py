#8.1.12
from algemene_functie import mijn_functie_2

#8.1.5
def aanbieding_1(smaak, prijs, korting):
    korting = prijs - (prijs * korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {korting}."

print(aanbieding_1("aardbei", 4, 0.1))


#8.1.6/8.1.7
def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal += bedrag
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

inkomsten_lijst = [220, 430, 125, 160, 205, 90, 345]
print(inkomsten_totaal(inkomsten_lijst, 0.09))


#8.1.8
def laag_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    resultaat = [laagste, hoogste]
    return resultaat

inkomsten_lijst = [220, 430, 125, 160, 205, 90, 345]
print(laag_hoog(inkomsten_lijst))


#8.1.9/8.1.10
def gemiddelde(mijn_lijst):
    optelling = 0
    for i in mijn_lijst:
        optelling += i
    gemiddeld_bedrag = optelling / 7
    return f"De gemiddelde inkomsten deze week zijn {gemiddeld_bedrag} euro."

inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(inkomsten))


#8.1.11
def meervoudig(invoer_lijst):
    return laag_hoog(invoer_lijst)

num_lijst = [10, 5, 3, 2, 1, 2, 9]
print(meervoudig(num_lijst))


#8.1.12
def combinatie(invoer_lijst_2):
    korte_lijst = laag_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)



