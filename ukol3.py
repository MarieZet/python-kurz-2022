from string import digits
from unicodedata import digit


telefonni_cislo = input('Uvedte telefonni cislo:')

def check_cislo():
    digits = len(telefonni_cislo)

    if digits == 9 or (digits == 13 and '+420' in telefonni_cislo):
        zprava = input ('Napiste Vasi zpravu')
        znaky_zprava = len(zprava) // 180 + 1

        def total_cena(znaky_zprava, cena_msg=3):
            cena = znaky_zprava * cena_msg
            len(zprava % 180 !=0:)
            print(f'Zprava odeslana prijemci. Celkova cena je {cena} korun')

        total_cena(znaky_zprava)

    else:
        print(f'Nespravne zadane cislo. Zkuste opakovat')



        
