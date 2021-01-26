
"""
Con questo metodo evitiamo di utilizzare variabili hard-coded negli operatori if
Inoltre, questo ci permette di avere tutti i parametri che vogliamo, senza necessità
di dover manualmente aggiungere un if per ogni condizione, in quanto vengono controllati dinamicamente
Es.: se ci fosse un parametro "30", col vecchio metodo bisogna mettere un apposito if. Così basta inserire
nel dizionario i parametri e la risposta verrà generata dinamicamente
"""

"""
COME FUNZIONA IL DIZIONARIO:
ha come chiave il parametro di eccesso, come valore una tupla contenente in corrispondenza:
- i punti che vengono tolti;
- una tupla contenente mesi di sospsensione minimo e massimo
- una tupla contenente la sanzione pecuniaria minima e massima
"""

SANZIONI = {
    10: (0, (), (41, 169)),
    40: (3, (), (169, 680)),
    60: (6, (1, 3), (532, 2127))  # 60 km/h: (6 punti, (da 1 a 3 mesi), (da 532 a 2127 euro))
}

# Questa è strutturata come i valori del dizionario, serve come fallback
MASSIMO = (10, (6, 12), (829, 3316))


# con questa funzione possiamo ricominciare come ci pare, basta inserirla a piacimento nel codice
def restart():
    ans = input("Vuoi ricominciare? ").lower()  # .lower() trasforma tutto in minuscolo, così eliminiamo il problema S/s
    if ans in ["si", "sì", "s"]:  # l'operatore in verifica l'appartenenza; usiamo questo anziché fare == s or == si
        calcola()
    else:
        print("Arrivederci!")
        exit()


def calcola():
    limite = int(input("Qual era il limite di velocità? "))
    velocita = int(input("A che velocità stavi viaggiando? "))  # evitiamo non-ascii characters nelle variabili, anche se sono permessi

    violazione = velocita - limite

    if violazione <= 0:  # verifichiamo da subito la condizione di uscita base, così non ci sporca la logica sotto
        print("Non hai superato i limiti")
        restart()

    # this is tricky in so many ways...
    # quando viene chiamato items() su un dizionario, viene restituita una lista di tuple
    # le tuple contengono al primo posto la chiave, al secondo il valore corrispondente
    # In questo modo iteriamo nel dizionario facendo unpacking
    # I nomi delle variabili sono self-explanatory per cosa accade
    for eccesso, (punti, sospensione, sanzione_pecuniaria) in SANZIONI.items():
        if violazione < eccesso:
            break  # now, this is really tricky and confusing. I know.
            # qua gli stiamo dicendo che se l'eccesso rientra nel parametro limite corrispondente
            # deve rompere il loop e l'else non verrà triggerato
            # in questo modo le variabili eccesso, punti, sospensione, sanzione_pecuniaria manterranno
            # l'ultimo valore preso dall'iterazione.
            # Es. l'eccesso è di 50, le variabili punti, sospensione, sanzione_pecuniaria saranno rispettivamente
            # 6, (1, 3), (532, 2127)
    else:
        # questo else viene eseguito quando il loop non viene rotto, e.g., quando la sanzione è massima
        punti, sospensione, sanzione_pecuniaria = MASSIMO

    risposte = []  # qui combiniamo le varie risposte in maniera dinamica
    # .append() aggiunge elementi a una lista
    if punti:
        risposte.append(f"decurtamento di {punti} punti dalla patente")
    if sospensione:  # una tupla vuota -> () darà false
        sos_min, sos_max = sospensione  # questo si chiama unpacking sos_min prenderà il valore di sospensione[0] e sos_max di sospensione[1]
        risposte.append(f"la sospensione della patente da {sos_min} a {sos_max} mesi")
    if sanzione_pecuniaria:  # same as above
        san_min, san_max = sanzione_pecuniaria  # same as above
        risposte.append(
            f"la sanzione amministrativa pecuniaria "
            f"da un minimo di euro {san_min:.2f} a un massimo di euro {san_max:.2f}"
        )

    if risposte:
        # la funzione join concatena diverse stringhe
        # es. "-".join(["uno", "due", "tre"]) --> "uno-due-tre"
        risposta = "Sono previste le seguenti sanzioni:\n- " + ";\n- ".join(risposte) + "."
    else:
        risposta = "Non è prevista nessuna sanzione"  # this is just for fallback reasons, shouldn't get triggered

    print(risposta)
    restart()


if __name__ == '__main__':
    calcola()
