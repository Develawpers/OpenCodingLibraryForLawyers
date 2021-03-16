## 🍾 1. Who is the develawpeer and how to credit him/her?

[Giacomo Bertelli](https://www.linkedin.com/in/giacomo-bertelli-2209753b/) used this simple and easy code trick to automate the calculation of the amount of the fine and/or the possible penalties related to the driving under the influence of alcohol.  There is no really need to credit the author as he used a very known standard script based on this video. However, if you wish to send some kudos you can [contact him on LinkedIn.](https://www.linkedin.com/in/giacomo-bertelli-2209753b/)  

## 🐜 2. Known bugs

There are no known bugs for this code trick. Want to segnalate one? [Write the author here.](https://www.linkedin.com/in/giacomo-bertelli-2209753b/) 

---

## ➡️ 3. Wiki

Let’s assume you would like to automate the calculation of fines and penalty points following a breach of the speed limit under the Italian traffic regulation. Following you may find the complete Code Strings.

```python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys

def main ():
    print("Hai guidato in stato di ebbrezza? Inserisci il tuo tasso alcolemico" 
      " per scoprire il tipo di sanzione:")

    #controllare che la variabile sia un numero
    try: 
        
        #Input da utente (tasso alcolemico)
        iTassoAlcolemico = float(input());
        
    except:
        print("valore inserito invalido")
        sys.exit(0)
        
    print("Sei neopatentato/a? S per Sì, N per No")    
    
    iPatentato = input()
    
    if ( 0 <= iTassoAlcolemico <= 10) :
        print("dato inserito corretto")
    
        if (iTassoAlcolemico <= 0.5) :
            
            if(iPatentato == 'S'):
                
                print("Il tuo tasso alcolemico deve essere sempre pari a zero")
                
            else:   
            
                print("Sei all'interno del limite di tolleranza. Non sono previste sanzioni, ma guida con prudenza")
        
        elif (iTassoAlcolemico <= 0.8) :
            print("Sanzione amministrativa da euro 544 a euro 2.174 e sospensione della patente di guida da tre a sei mesi")
        elif (iTassoAlcolemico <= 1.5) :
            print("Ammenda da euro 800 a euro 3.200 e arresto fino a sei mesi. All'accertamento del reato consegue in ogni caso la sanzione amministrativa accessoria della sospensione della patente di guida da sei mesi ad un anno")
        
        else:
            print("Ammenda da euro 1.500 a euro 6.000 e arresto da sei mesi ad un anno. All'accertamento del reato consegue in ogni caso la sanzione amministrativa accessoria della sospensione della patente di guida da uno a due anni. Se il veicolo appartiene a persona estranea al reato, la durata della sospensione della patente di guida è raddoppiata. La patente di guida è sempre revocata in caso di recidiva nel biennio.")
        
    else:
        print("dato inserito non corretto")

    #verifica dato inserito
    print("Tasso alcolemico d'ingresso",iTassoAlcolemico)

    restart=input("Vuoi inserire un altro valore? S per continuare, altro per uscire")
    
    if restart == 'S':
        main ()
    else:
        print("Arrivederci!")

if __name__ == "__main__": main()
```
