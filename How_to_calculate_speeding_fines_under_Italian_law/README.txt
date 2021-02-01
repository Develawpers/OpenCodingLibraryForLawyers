🍾 1. Who is the develawpeer and how to credit him/her?

[Simone Cedrola](https://www.linkedin.com/in/simone-cedrola-ll-m-44662014b/) used this simple and easy code trick to automate the calculation of the amount of the fine and/or how many points must be subtracted from a penalty-points driving license when in violation of the speed limit.

There is no really need to credit the author as he used a very known standard script based on [this video](https://www.youtube.com/watch?v=JLhcmhMB0r4&feature=youtu.be). However, if you wish to send some kudos you can [contact him on LinkedIn](https://www.linkedin.com/in/simone-cedrola-ll-m-44662014b/).  

**[Learn the basic syntax →](https://develawpers.com/How-to-calculate-speeding-fines-under-Italian-law-a803201b6b954d11a59b7c0df4739f3f)**

**[Go to the full use case →](https://develawpers.com/How-to-calculate-speeding-fines-under-Italian-law-a803201b6b954d11a59b7c0df4739f3f)**

---

🐜 2. Known bugs

There are no known bugs for this code trick. Want to segnalate one? [Write the author here](https://www.linkedin.com/in/simone-cedrola-ll-m-44662014b/). 

---

➡️ 3. Wiki

Let’s assume you would like to automate the calculation of fines and penalty points following a breach of the speed limit under the Italian traffic regulation. Following you may find the complete Code Strings.


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


### Let's go more in depth

1. First of all, you want to set the following. This is basically the starting point of the program generally known as main function.


def main ():

	main ()


2. Let's print out the "welcome" message and set the 3 variables


  print("Hai violato il Codice della Strada? Scopri quanti punti ti verranno decurtati e a quanto ammontano le sanzioni amministrative pecuniarie.")

  limite = int(input("Qual era il limite di velocità? "))
  velocità = int(input("A che velocità stavi viaggiando? "))

  differenza = velocità - limite


3. Let's set our if-elif-else statements. This is not rocket science and it is very basic. We are saying that if the variable called "differenza" is smaller or bigger than the input number provided by the user the code strings will print different things accordingly. 


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


4. Now let's set our restart function which will allow the user to restart the entire script **if** he ****answers the question positively, otherwise (**else**) it will end. 

  restart=input("Vuoi calcolare di nuovo se hai violato il Codice della Strada? ")
  if restart == "sì" or "si":
    main()

  else:
    print("Arrivederci!")
    exit()


---

👨🏻‍💻 4. Use cases

This simple code trick allows the user, whether a jurist or a citizen, to know with just a few clicks what the legal consequences of violating speed limits are under Italian Law. It combines both the amount of the fine and the amount of points to be deducted from the driving license.

In addition, this could also be adapted based on other laws and to automate and streamline similar processes.
