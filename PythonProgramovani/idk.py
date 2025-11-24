import random

vybrani_studenti = []

cesta = r"C:\Users\st025567\kb4a_prog_totr\2. prace_se_soubory\data\studenti.txt"
with open(cesta, "r", encoding="utf-8") as file:
    studenti = file.readlines()
    while len(vybrani_studenti) < 5:
        student = random.choice(studenti).strip()
        if student not in vybrani_studenti:
            vybrani_studenti.append(student)

vybrani_studenti.sort()
print(vybrani_studenti)


with open("vybrani_studenti.txt", "w", encoding="utf-8") as file:
    for student in vybrani_studenti:
        file.write(student + "\n")