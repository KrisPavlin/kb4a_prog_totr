## 2) **Chatlog – souborový chat**

##Naprogramuj jednoduchý textový "chat", který ukládá zprávy do souboru `data/chatlog.txt`.

##Program by měl fungovat takto:

##1. Uživatel zadá **uživatelské jméno** (např. `cichna-smrdi25`).
##2. Uživatel zadá **text zprávy**.
##3. Program zprávu **přidá na konec souboru** ve formátu například:
   ##`cichna-smrdi25: Ahoj, cítíte to taky?`
##4. Program se ptá opakovaně na další zprávy (a uživatelská jména), dokud uživatel nenapíše speciální příkaz (např. `konec`) místo zprávy.

##Bonus:
##- Přidej k každé zprávě čas odeslání (např. `2025-10-03 14:32:10 - cichna-smrdi25: Ahoj, cítíte to taky?`).

import datetime
cesta = r"C:\Users\st025567\kb4a_prog_totr\2. prace_se_soubory\data\chatlog.txt"
with open(cesta, "a", encoding="utf-8") as file:
    while True:
        uzivatelske_jmeno = input("Zadejte uživatelské jméno: ")
        zprava = input("Zadejte text zprávy (nebo 'konec' pro ukončení): ")
        if zprava.lower() == "konec":
            print("Chat ukončen.")
            break
        cas_odeslani = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatovana_zprava = f"{cas_odeslani} - {uzivatelske_jmeno}: {zprava}\n"
        file.write(formatovana_zprava)
        print("Zpráva byla přidána do chatlogu.")