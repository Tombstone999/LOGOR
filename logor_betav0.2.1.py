from fpdf import FPDF
import os
import time
from datetime import datetime
from termcolor import colored, cprint
from dataclasses import dataclass
@dataclass

# reading from grower database
# record array struct 
class grower():
    growerID:int
    name:str
    prod:str
    len:str

# Length of grower register
R_LEN = int(32)

logor_logo = '''

    ______                                
    ___  / ______ _______ _______ ________
    __  /  _  __ \__  __ `/_  __ \__  ___/
    _  /___/ /_/ /_  /_/ / / /_/ /_  /    
    /_____/\____/ _\__, /  \____/ /_/     
                  /____/                  
                            v0.2.1
                                made by R. Esp

                  - - -

LOGOR è un software gestionale ed organizzativo 
per la logistica floricola. 
Aiuta e velocizza le operazioni di etichettatura
per la gestione logistica di carico e scarico.

                    designed for Starline flowers

                  - - -
                    

'''

'''
print(colored(stline_logo, 'magenta'))
time.sleep(1.5)
os.system('clear')
'''

print("** Lettura database locale... **\n")
time.sleep(0.5)

# grower record array structure setup
growerArray = [grower(x+1, "", "", "") for x in range(R_LEN)]

# opening grower list DB and store in grower
with open("/storage/emulated/0/Download/LOGOR_v0.2.1/gest_iacomino/grower_list.txt", 'r') as f:
    f.seek(0)
    for x in range(R_LEN):
        #growerArray[x].growerID = f.readline()
        growerArray[x].name = f.readline()
        growerArray[x].prod = f.readline()
        growerArray[x].len = f.readline()
        null_line = f.readline()
        print("** Coltivatore n.", x, "aggiunto con successo. **")
        time.sleep(0.05)
        os.system('clear')

print(colored(logor_logo, 'green'))

# main function that execute algorithm
def main():
    
    f = open("/storage/emulated/0/Download/LOGOR_v0.2.1/gest_iacomino/label_report.txt", 'a+')
    if os.stat("/storage/emulated/0/Download/LOGOR_v0.2.1/gest_iacomino/label_report.txt").st_size == 0:
        f.seek(0)
        f.write("0\n")    
    f.close()

    ## MAIN PIECE - MOST IMPORTANT -- determine file length and point the cursor to last position of the file
    #  to allow to increment index and read content of that line of the file
    index = int()
    with open("/storage/emulated/0/Download/LOGOR_v0.2.1/gest_iacomino/label_report.txt", 'r') as f:
        index = len(f.readlines())
        #print("File length: " + str(index))

    # pdf class creation
    pdf = FPDF('P', 'mm', 'A4')
    
    #file.pdf page setup and creation of new page
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()
    pdf.image('/storage/emulated/0/Download/LOGOR_v0.2.1/gest_iacomino/bin/Logo-Starline-Flowers_alpha027.png', x = 10, y = 75, h = 140, w = 193)

    pdf.set_font('Helvetica', '', 15)
    pdf.cell(190, 10, 'Cliente:', ln=True, border='L, R, T', align='L')
    str_gIn = input("Cliente:\n> ")
    gIn = int(str_gIn)
    pdf.set_font('Helvetica', 'B', 50)
    pdf.cell(190, 20, growerArray[gIn].name,ln=True, border='L, R, B', align='L')

    pdf.set_font('Helvetica', '', 15)
    pdf.cell(190, 10, 'Prodotto:', ln=True, border='L, R, T', align='L')
    pdf.set_font('Helvetica', 'B', 50)
    pdf.cell(190, 20, growerArray[gIn].prod, ln=True, border='L, R, B', align='L')

    str_t_pl = input("Quanti pianali hai? -> ")

    curr_pl = int()
    curr_ct = int()
    plane = [[]]
    
    #conversion from stirng to int()
    t_pl = int(str_t_pl)

    #cart equation from total planes
    t_cart = int(t_pl / 4)

    pdf.cell(190, 10, '', ln=True, border='L,R', align='L')
    t_pl = t_pl - 1
    cart_plane = int()

    while (t_pl >= curr_pl):
        plane = input("articolo: ")
        print("current plane: " + str(curr_pl+1) + "  |  " + "current cart: " + str(curr_ct+1) + '\n')
        pdf.set_font('Helvetica', '', 28)
        pdf.cell(190, 5, '', ln=True, border='L,R', align='L')
        pdf.cell(190, 10, 'P' + str(curr_pl+1) + ' ' + str(plane), ln=True, border='L,R', align='L')
        pdf.cell(190, 5, '', ln=True, border='L,R', align='L')
        tmp_choice = input("Pianale terminato? [y/n] -> ")
            
        if tmp_choice == "y":
            curr_pl += 1
            cart_plane += 1
        if (cart_plane >= 4):
            print("total planes: " + str(t_pl+1) + "  |  " + "total cart: " + str(t_cart) + "\n")
            time.sleep(0.25)
            pdf.cell(190, 10, '', ln=True, border='L, R, B', align='c')
            pdf.set_font('Helvetica', '', 25)   
            pdf.cell(190, 10, 'Carrello ' + str(curr_ct+1) + ' di ' + str(t_cart+1), ln=True, border='L, R', align='c')
            pdf.cell(190, 10, '', ln=True, border='L, R, B', align='c')
            curr_ct += 1
            cart_plane = 0
            
            #file.pdf page setup and creation of new page
            pdf.set_auto_page_break(auto=True, margin=10)
            pdf.add_page()
            pdf.image('/storage/emulated/0/Download/LOGOR_v0.2.1/gest_iacomino/bin/Logo-Starline-Flowers_alpha027.png', x = 10, y = 75, h = 140, w = 193)

            pdf.set_font('Helvetica', '', 15)
            pdf.cell(190, 10, 'Cliente:', ln=True, border='L, R, T', align='L')
            pdf.set_font('Helvetica', 'B', 50)
            pdf.cell(190, 20, growerArray[gIn].name,ln=True, border='L, R, B', align='L')

            pdf.set_font('Helvetica', '', 15)
            pdf.cell(190, 10, 'Prodotto:', ln=True, border='L, R, T', align='L')
            pdf.set_font('Helvetica', 'B', 50)
            pdf.cell(190, 20, growerArray[gIn].prod, ln=True, border='L, R, B', align='L')

            print("** CART ADD - success **\n")
            time.sleep(0.5)
        
    if cart_plane < 4:
        pdf.cell(190, 10, '', ln=True, border='L, R, B', align='c')
        pdf.set_font('Helvetica', '', 25)   
        pdf.cell(190, 10, 'Carrello ' + str(curr_ct+1) + ' di ' + str(t_cart+1), ln=True, border='L, R', align='c')
        pdf.cell(190, 10, '', ln=True, border='L, R, B', align='c')
        cart_plane = 0

    print("** Generazione ordine n." + str(index) + " in corso...  **\n")
    time.sleep(0.25)
    dt = datetime.now()
    ts = datetime.timestamp(dt)

    if(f):
        print("** /storage/emulated/0/Download/LOGOR_v0.2.1/gest_iacomino/label_report.txt aggiornato con successo! **\n")

    #name with incremental enumeration
    l_name = "ORDINE_N0"+str(index)+".pdf"
    
    #write new line on report file
    with open('/storage/emulated/0/Download/LOGOR_v0.2.1/gest_iacomino/label_report.txt', 'a+') as f:
        f.write(str(index) + ' | #LABEL_REPORT_N'+ str(index) +' del'+ str(dt) + str(ts)+"\n")

    #debug string
    print(str(index) + ' | #LABEL_REPORT_N'+ str(index) +' del'+ str(dt) + str(ts)+"\n")
    
    #creation of final .pdf file
    pdf.output('/storage/emulated/0/Download/LOGOR_v0.2.1/gest_iacomino/RTP_labels/' + l_name)
    
    #quick pause between two files generation
    time.sleep(1)

    #  Creation of logistic label
    ##
    pdf = FPDF('L', 'mm', 'A5')

    #file.pdf page setup and creation of new page
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()
    pdf.image('/storage/emulated/0/Download/LOGOR_v0.2.1/gest_iacomino/bin/Logo-Starline-Flowers_alpha027.png', x = 10, y = 40, h = 100, w = 138)

    pdf.set_font('Helvetica', 'B', 50)
    pdf.cell(190, 30, ' STARLINE FLOWERS ', ln=True, border=1, align='C')

    pdf.set_font('Helvetica', '', 25)
    pdf.cell(190, 10, 'Cliente:', ln=True, border='L, R', align='L')
    pdf.set_font('Helvetica', '', 40)
    pdf.cell(190, 20, growerArray[gIn].name, ln=True, border='L, R, B', align='L')
    pdf.set_font('Helvetica', '', 40)
    pdf.cell(190, 30, 'TOT. CARRELLI: ' + str(t_cart+1), ln=True, border=1, align='L')
    
    log_l_name = "ET_LOG_N0"+str(index)+".pdf"

    #creation of final .pdf file
    pdf.output('/storage/emulated/0/Download/LOGOR_v0.2.1/gest_iacomino/RTP_labels/logistic_labels/' + log_l_name)

    print(" ** etichetta logistica generata con successo **\n\n")
    time.sleep(0.5)

    print(" ** EOF - code breaking ** ")
   
if __name__ == "__main__":
    main()