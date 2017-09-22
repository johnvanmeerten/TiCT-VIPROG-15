def standaardprijs(afstandKM):

    if afstandKM > 0 and afstandKM <= 100:
        prijs = 0.80 * afstandKM
        return prijs

    elif afstandKM > 100:
        prijs = 15 + (0.60 * afstandKM)
        return prijs

    else:
        prijs = 0
        return prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if weekendrit == "ja" and leeftijd >= 65 or leeftijd <= 12 :
        korting = (prijs / 100) * 35
        prijs = prijs - korting

    elif weekendrit == "nee" and leeftijd >=65 or leeftijd <= 12 :
        korting = (prijs / 100) * 30
        prijs = prijs - korting

    elif weekendrit == "ja" and leeftijd >= 65 or leeftijd <=12 :
        korting = (prijs / 100) * 40
        prijs = prijs - korting

    elif weekendrit =="nee" and leeftijd <= 65 or leeftijd >=12:
        prijs = prijs
    return prijs


afstandKM = eval(input("hoe veel km is je reis: "))
leeftijd = eval(input("wat is je leeftijd, antwoord in een cijfer: "))
weekendrit = input("is het weekend? antwoord met ja of nee: ")

print(ritprijs(leeftijd, weekendrit, afstandKM))
# print(ritprijs(35, 'ja', 6))