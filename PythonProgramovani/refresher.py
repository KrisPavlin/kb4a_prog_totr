def vypis_delitelu(cislo):
    print(f"Dělitelé čísla {cislo} jsou:")
    for i in range(1, cislo + 1):
        if cislo % i == 0:
            print(i)
    print()

vypis_delitelu(24)