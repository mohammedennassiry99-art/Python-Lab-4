seuil = 10  

try:
    note = float(input("Entrez la note de l'étudiant : "))
except ValueError:
    print("Saisie invalide.")
    exit(1)

if note >= seuil and note <= 12:
     print("Admis")
elif note > 12 and note <= 16:
    print("Bien");
elif note > 16 and note <= 20:
    print("Tres bien")

else:
    print("Refusé")