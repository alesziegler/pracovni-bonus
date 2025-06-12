print("Tohle je vypocet pracovniho bonusu podle paragrafu 41 zakona c. 151/2025 Sb., o davce statni socialni pomoci, v jeho originalnim zneni.")

print(
    """
Pro vypocet pracovniho bonusu je nutne znat 3 hodnoty:
1) aktualni zakonem nebo narizenim vlady stanovene zivotni minimum,
2) rozhodny mesicny prijem domacnosti ve smyslu paragrafu 2 odst. 4 zakona c. 151/2025 Sb. (tento paragraf se odkazuje na radu dalsich ustanoveni).
    Zjednodusene receno jde o celkovy prijem domacnosti s urcitymi odchylkami.
3) mesicny prijem domacnosti zohlednovany pro pracovni bonus, definovany v paragrafu 40 odst. 2 zakona c. 151/2025 Sb.
    Zjednodusene receno jde o prijem domacnosti z prace a z rodicovskeho prispevku.
"""
)

done = False
while done == False:
    try:
        zivotni_minimum = int(input("zivotni minimum: "))
        rozhodny_prijem = int(input("rozhodny prijem: "))
        prijem_pro_bonus = int(input("prijem pro bonus: "))
        done = True
    except Exception as e:
        print("Zadavejte pls cela cisla bez mezer. Zadne zlomky apod. slozitosti")

hranice = zivotni_minimum*1.6

zaklad = rozhodny_prijem - hranice

castka_z_par_41_odst_2_pism_a = 0.4*(prijem_pro_bonus - zaklad)
if castka_z_par_41_odst_2_pism_a < 0:
    castka_z_par_41_odst_2_pism_a = 0

castka_z_par_41_odst_2_pism_b = 0.3*(zaklad - hranice)
if castka_z_par_41_odst_2_pism_b < 0:
    castka_z_par_41_odst_2_pism_b = 0

if prijem_pro_bonus <= 0:
    bonus = 0
    tracker = "Domacnost nema zadny prijem pro bonus."
# nize situace z paragrafu 41 odst 1:
elif zaklad <= 0: 
    bonus = prijem_pro_bonus*0.4
    tracker = "Domacnost ma rozhodny prijem pod hranici 1,6 zivotniho minima."
# nize situace z paragrafu 41 odst 3:
elif castka_z_par_41_odst_2_pism_b > castka_z_par_41_odst_2_pism_a: 
    bonus = 0
    tracker = "Domacnost je v situaci z paragrafu 41 odst. 3."
# nize situace z paragrafu 41 odst. 2:
else: 
    bonus = castka_z_par_41_odst_2_pism_a + castka_z_par_41_odst_2_pism_b
    tracker = "Domacnost je v situaci z paragrafu 41 odst. 2."

print(f"Vyse pracovniho bonusu na zaklade zadanych castek je {bonus} Kc. {tracker}")