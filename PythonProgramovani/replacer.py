#Vytvoř program, který umí nahradit všechna výskyty určitého slova v textovém souboru jiným slovem (ve stylu "najdi a nahraď").

#1. Načti libovolný delší textový soubor, např. `1984.txt`.
#2. Od uživatele načti dvě slova:
 #  - **původní slovo** (např. `newspeak`),
  # - **nové slovo** (např. `novomluva`).
#3. Program:
 #  - načte obsah souboru,
  # - nahradívšechny výskyty původního slova slovem novým,
  # - výsledek zapíše do nového souboru.

cesta = r"C:\Users\st025567\kb4a_prog_totr\2. prace_se_soubory\data\1984.txt"
puvodni_slovo = input("Zadejte původní slovo: ")
nove_slovo = input("Zadejte nové slovo: ")
with open(cesta, "r", encoding="utf-8") as file:
    obsah = file.read()
    novy_obsah = obsah.replace(puvodni_slovo, nove_slovo)

with open("1984_upraveno.txt", "w", encoding="utf-8") as file:
    file.write(novy_obsah)
print(f"Všechny výskyty slova '{puvodni_slovo}' byly nahrazeny slovem '{nove_slovo}' a uloženy do '1984_upraveno.txt'.")

print(novy_obsah)