valores = [True, False]

print("Lei 1: ¬(A ∧ B) ≡ (¬A) ∨ (¬B)")
for A in valores:
    for B in valores:
        esquerda = not (A and B)
        direita = (not A) or (not B)
        print(f"A={A}, B={B} -> {esquerda == direita}")

print("\nLei 2: ¬(A ∨ B) ≡ (¬A) ∧ (¬B)")
for A in valores:
    for B in valores:
        esquerda = not (A or B)
        direita = (not A) and (not B)
        print(f"A={A}, B={B} -> {esquerda==direita}")