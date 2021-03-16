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
