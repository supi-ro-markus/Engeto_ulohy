# aim of the exercise to combine int and str
mercedes = 150_000
rolls_royce = '400000'
vybava = 50_000

sleva_merc=input("Aku slevu chces?")
merc_se_slevou=int(sleva_merc)

print("O kolik USD slevnime Mercedes? ",sleva_merc)
print("Cena za dva Mercedesy je:",mercedes*2)
print("Cena za Mercedes a Rolls-Royce:",mercedes+int(rolls_royce))
print("Cena za dva Rolls-Royce s priplatkovou vybavou:",(int(rolls_royce)+vybava)*2)
print("Cena za Mercedes s priplatkovou vybavou je:",mercedes+vybava)
print("Cena za Mercedes po sleve je:",mercedes-merc_se_slevou)


#sleva_merc
#merc_se_slevou=int(mercedes)*sleva_merc