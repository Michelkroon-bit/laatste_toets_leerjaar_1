from math import ceil , floor

def hoevaak_tanken (kilometers_per_liter, tankinhoud, te_rijden_afstand)-> int:
    aantal_kilometers_per_liter = tankinhoud * kilometers_per_liter
    afstand = te_rijden_afstand / aantal_kilometers_per_liter
    return (f"je moet {ceil(afstand)} keer tanken\n")
    

print(f"Test 1: {hoevaak_tanken(7 , 60 , 1690)}")
print(f"Test 2: {hoevaak_tanken(9 , 60 , 920)}")
print(f"Test 3: {hoevaak_tanken(12 , 60 , 132)}")
print(f"Test 4: {hoevaak_tanken(4 , 60 , 1140)}")
print(f"Test 5: {hoevaak_tanken(6 , 60 , 150)}")
print(f"Test 6: {hoevaak_tanken(4 , 60 , 329)}")
print(f"Test 7: {hoevaak_tanken(6 , 60 , 242)}")
print(f"Test 8: {hoevaak_tanken(12 , 60 , 132)}")
print(f"Test 9: {hoevaak_tanken(12 , 60 , 140)}")
print(f"Test 10: {hoevaak_tanken(5 , 60 , 75)}")


