def main ():

  print("Hai violato il Codice della Strada? Scopri quanti punti ti verranno decurtati e a quanto ammontano le sanzioni amministrative pecuniarie.")

  limite = int(input("Qual era il limite di velocità? "))
  velocità = int(input("A che velocità stavi viaggiando? "))

  differenza = velocità - limite

  if(differenza < 1):
    print("Hai rispettato i limiti di velocità. Bravo!")
  elif(differenza < 10):
    print("Non è previsto alcun decurtamento di punti")
  elif(differenza < 40):
    print("È previsto il decurtamento di 3 punti")
  elif(differenza < 60):
    print("È prevista la sospensione della patente da 1 a 3 mesi e il decurtamento di 6 punti")
  else: 
    print("È prevista  la sospensione della patente da 6 a 12 mesi e il decurtamento di dieci punti")

  if(differenza < 1):
    print("Guida sempre con prudenza!")
  elif(differenza < 10):
    print("È prevista una sanzione amministrativa che ammonta da un minimo di euro 41 a un massimo di euro 169")
  elif(differenza < 40):
    print("È prevista una sanzione amministrativa che ammonta da un minimo di euro 169 a un massimo di euro 680")
  elif(differenza < 60):
    print("È prevista una sanzione amministrativa che ammonta da un minimo di euro 532 a un massimo di euro 2.127")
  else:
    print("È prevista una sanzione amministrativa che ammonta da un minimo di euro 829 a un massimo di euro 3.316")
      
  restart=input("Vuoi calcolare di nuovo se hai violato il Codice della Strada? ")
  if restart == "sì" or if restart == "si":
    main()

  else:
    print("Arrivederci!")
    exit()

main ()
