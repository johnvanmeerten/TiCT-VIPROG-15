studentencijfers = [[95,92,86],[66,75,54],[89,72,100],[34,0,0]]

def gemiddelde_per_student(studentencijfers):
    lijst1 = []
    for student in studentencijfers:
        gemiddelde = sum(student)/len(student)
        lijst1.append(gemiddelde)

    return lijst1


def gemiddelde_van_alle_studenten(studentencijfers):
    gemstuden = gemiddelde_per_student(studentencijfers)
    antwooord = sum(gemstuden)/len(gemstuden)

    return antwooord


print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))