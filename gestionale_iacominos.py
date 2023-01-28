import sys
import os
from termcolor import colored, cprint
import time 
from fpdf import FPDF

res_marker = bool(False)

grower_name = []
grower_prod = []
grower_var = []
grower_measure = []
grower_color = []

global i

def main():
    i = 0
    while(1):
        string_menu1 = '''

                                                 .H                                                 
                                                 ╫╫≥                                                
                                                ╟╫╫╫≥                                               
                                               ╬╫╫╫╫╫≥                                              
                                              ╫╫╫╫╫╫╫╫≥                                             
                                             j╫╫╫Ñ'╫╫╫Ñ                                             
                                             j╫╫Ñ  ╙╫╫Ñ                                             
                             %╦╦NNÑ╫╫╫╫╫╫╫Ñ╦, ╫╫`jÑ ╟╫░,╔╦╫╫╫╫╫╫╫ÑÑNNNN*                            
                               ╙╫╫╫╫╫╫Ñ╩╩╩╩╩╩╩NH:╫╫N ╩╩╩╩╩╩╩╩╩╫╫╫╫╫╫╩`                              
                                 "╩╫╫╫╫Nw '«╦╦╦╦╦«≈═─:,,»  ,╦╫╫╫╫Ñ╨                                 
                                   `╨╫╫╫╫╫N╥``«╦╦╦░░╨░» ,╦╫╫╫╫╫╩"                                   
                                       `"""░╫⌐:╨░░╦░░╦ ╦░"""``                                      
                                         ╔╫╫Ñ.╦░╨` ╨╫╫N╙╫╫N.                                        
                                       :╫╫╫Ñ ╚`,╦╫jNw`╨ ]╫╫╫N                                       
                                       ╫╫╫╫`,╦╫╫╫" ╫╫╫Nw ╬╫╫╫H                                      
                                      j╫╫╫╫╫╫╫╫Ñ`   ╨╫╫╫╫╫╫╫╫Ñ                                     
                                      ╫╫╫╫╫╫Ñ╩"      `╨╫╫╫╫╫╫╫                                      
                                     j╫╫Ñ╩"`             `╨Ñ╫╫N                                     
                                     ╩╨`                     "╨H                                    
                                                                                                    

 ,▄▓██▓▓▄   ▓▓▓▓▓▓▓▓▓▓▓▓m    ╓▓m        ▓▓▓▓▓▓▓▓▄,    ╢▓▓         ▓▓▓   ║▓,        ╫▓▓   ▐▓▓▓▓▓▓▓▓▓▓
.▓██""▀▀"   ````╟██▌````    .▓██w       ▓██"""╙▀██▄   ║██         ▓██   ║██▓,      ╫██   ║██▌```````
 ███▄           j██▌       .▓████       ▓██     ║██   ║██         ▓██   ║████▓,    ╫██   ║██M       
  ╙███▄,        j██▌       ▓██`███      ▓██    ,▓█▌   ║██         ▓██   ║██M▀██▓,  ╫██   ║██▓▓▓▓▓▓H 
    ╙▀██▓w      j██▌      ▓██"  ███     ▓██▓▓▓▓██▀    ║██         ▓██   ║██m `▀██▓w╫██   ║██▀╨╨╨╨╨^ 
      `███      j██▌     ╣███▓▓▓███▌    ▓██╙╙▀██▄     ║██         ▓██   ║██m   `▀█████   ║██M       
╓▄▓▄╓╓▄███      j██▌    ╣██▀"""""╙██▌   ▓██   ╙██▓,   ║██,,,,,,,  ▓██   ║██m     `▀███   ║██Ω,,,,,, 
 ╙▀████▀╨       j██▌   ║██▌       ╙██▌  ▓██     ▀██▄  ╢█████████M ▓██   ║██m       `▀█   ║██████████
                                                                                                    
                                                                                                  
                         ▓╜╙    ▓     ╓Φ╨╨╦    ▓ .▄ ╔▀   :▓╜╙    ▓╜╫╕   j▓╨                         
                         ▓"^    ▌     ╣φ  ║M    ▓▓╙▓▌    :▓"^    ▓K▓`    "╫╕                        
                         ╜      ╜╜╜    "╨╨`     '` ╙      ▀╜╜    ╨ ╙^    ╙╨       

        '''
        string_menu2 = '''
        =================== menu principale ===================

        Scegli cosa fare:

        |=============|     |=============|     |=============| 
        | 1. aggiungi |     | 2. modifica |     | 3.   crea   |
        | coltivatore |     | coltivatore |     |    ordine   |
        |=============|     |=============|     |=============|

        |=============|     |=============|     |=============| 
        | 4.  stampa  |     | 5. modifica |     | 6.logistica |
        |    ordine   |     |    ordine   |     |             |
        |=============|     |=============|     |=============|    
        

                                *
        
        -------------------------------------------------------
                    -- PREMI '0' PER USCIRE --
        -------------------------------------------------------

        '''

        menu_title = colored(string_menu1, 'magenta')
        print(menu_title)
        time.sleep(0.25)

        menu = colored(string_menu2, 'yellow')
        print(menu)
        time.sleep(0.25)

        menu_nav = input("Digita la scelta: ")
        
        if menu_nav == "1":
            print(colored('\n 1. aggiungi coltavore - selezionato. \n\n', 'red'))
            add_grower = '''
        =================== (1) add grower ====================

        Aggiungi coltivatore ed esplicita gli articoli che
        produce e le varietà.
                                * * *
        
        '''
            print(colored(add_grower, 'yellow'))
            if i in range(0,255):
                temp_string = input("Nome coltivatore: ")
                grower_name.insert(i, temp_string)
                time.sleep(0.1)

                temp_string = colored(input("Prodotto: "), 'yellow')
                grower_prod.insert(i, temp_string)
                time.sleep(0.1)
                        
                temp_string = colored(input("Varietà: "), 'yellow')
                grower_var.insert(i, temp_string)
                time.sleep(0.1)
                        
                print(colored('Inserisci le lunghezze degli steli seguiti da virgola...', 'yellow'))
                print(colored('*ESEMPIO: L45, L40, L35 ecc...*', 'red'))
                temp_string = colored(input("Lunghezza: "), 'yellow')
                grower_measure.insert(i, temp_string)
                time.sleep(0.1)

                print(colored('Inserisci i colori seguiti da virgola...', 'yellow'))
                print(colored('*ESEMPIO: blue, red, pink ecc...*', 'red'))
                temp_string = colored(input("Colori: "), 'yellow')
                grower_color.insert(i, temp_string)
                time.sleep(0.1)

                print(colored('* nuovo coltivatore aggiunto *\n\n', 'green'))
                print(colored('=== Coltivatore ' + str(i+1) + ' ===\n', 'yellow'))
                print(colored('Nome: ' + grower_name[i], 'yellow'))
                print(colored('Prodotto: ' + grower_prod[i], 'yellow'))
                print(colored('Varietà: ' + grower_var[i], 'yellow'))
                print(colored('Lunghezza ' + grower_measure[i], 'yellow'))
                print(colored('Colori: ' + grower_color[i] + ' cm \n', 'yellow'))
                print(colored(' *** ritorno al menu principale... *** \n\n', 'green'))
                i = i+1

            #clear screen after 5 seconds
            time.sleep(5)
            os.system('clear')

        elif menu_nav == "2":
            i = 0

            print("\n 2. modifica coltavore - selezionato. \n\n")

            modify_grower = '''
        ================= (2) modify grower ===================

        Modifica o visiona coltivatore precedentemente inserito
        digitando il numero coltivatore oppure il nome

                                * * *
        
        '''

            print(colored(modify_grower, 'yellow'))
            #choose grower to modify
            temp_string = input(colored('Digita coltivatore da modificare: ', 'magenta'))
            temp_str2 = "Ricerca in corso"
            
            for i in range(0, 255):
                if temp_string in grower_name:
                    res_marker = True
                    print(colored('** Coltivatore trovato **', 'green'))
                    time.sleep(0.2)
                    print(colored('=== Coltivatore ' + str(i+1) + ' ===\n', 'yellow'))
                    print(colored('Nome: ' + grower_name[i], 'yellow'))
                    print(colored('Prodotto: ' + grower_prod[i], 'yellow'))
                    print(colored('Varietà: ' + grower_var[i], 'yellow'))
                    print(colored('Lunghezza ' + grower_measure[i], 'yellow'))
                    print(colored('Colori: ' + grower_color[i] + ' cm \n', 'yellow'))
                    time.sleep(0.5)
                    temp_string = input("Vuoi modificare coltivatore? [y/n]")
    
                else:
                    res_marker = False
                    print(colored(temp_str2, 'grey'))
                    time.sleep(0.1)
                    temp_str2 = temp_str2 + "."
                    os.system('clear')
                    i=i+1
                    if len(temp_str2) >= 20:
                        os.system('clear')
                        temp_str2 = "Ricerca in corso"

        
            if temp_string == "y":
                temp_string = input("Nome coltivatore: ")
                grower_name.insert(i, temp_string)
                time.sleep(0.25)     
                temp_string = input("Prodotto: ")
                grower_prod.insert(i, temp_string)
                time.sleep(0.25)
                temp_string = input("Varietà: ")
                grower_var.insert(i, temp_string)
                time.sleep(0.25)
                temp_string = input("Lunghezza: ")
                grower_measure.insert(i, temp_string)
                time.sleep(0.25)
                temp_string = input("Colori: ")
                grower_color.insert(i, temp_string)
                time.sleep(0.25)
                print(colored('** modifica eseguita con successo **\n', 'green'))
                time.sleep(1)
                i = i+1

            elif temp_string == "n":
                print(colored('** ritorno al menù principale... \n\n', 'green'))
                time.sleep(1)

            if res_marker == False & i == 255:
                print(colored('** Esito ricerca: NEGATIVO - coltivatore non trovato. **\n\n','red'))
                time.sleep(0.5)
                print(colored('*\n', 'cyan'))
                time.sleep(0.5)
                print(colored('** ritorno al menù principale... **', 'green'))
                i = 0
                
        elif menu_nav == "3":
            print(colored('\n 3. "Crea ordine" - selezionato. \n\n', 'red'))
            add_grower = '''
        =================== (3) new order ====================

        Genera il file pdf per l'etichettatura e immagazzina
        i dati per la successiva gestione in logistica

                                * * *
        
        '''
            temp_string = input(colored('Coltivatore: ', 'yellow'))
            i = 0
            for i in range(0, 255):
                if temp_string in grower_name:
                    print(colored('** coltivatore presente in db. - SUCCESS ** ', 'green'))
                    time.sleep(0.5)
                    nome = grower_name
                    prodotto = grower_prod[i]
                    variety = grower_var[i]
                else:
                    i = i+1
            
            if temp_string not in grower_name:
                print(colored('** coltivatore NON presente in db. ** ', 'red'))
                nome = input(colored('Nuovo coltivatore: ', 'yellow'))
                time.sleep(0.3)

            pianali = input(colored('pianali tot: '))
            j = 0
            if j <= pianali:
                print(colored('Pianale '+str(j)+': ', 'yellow'))
                secchi = input(colored('Secchi: ', 'yellow'))
                steli = input(colored('steli: ', 'yellow'))


        elif menu_nav == "4":
            print("\n 4. stampa ordine - selezionato. \n\n")
        
        elif menu_nav == "5":
            print("\n 5. modifica ordine - selezionato. \n\n")
        
        elif menu_nav == "6":
            print("\n 6. logistica - selezionato. \n\n")
        
        elif menu_nav == "0":
            print(colored('\n ** EXIT CODE 0 - chiusura in corso... **', 'green'))
            time.sleep(1.5)
            os.system('clear')
            break    
        
        else:
            print("#ERR01 - input errato, RIPROVA.")
            
if __name__ == "__main__":
    main()

