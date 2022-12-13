import tkinter.filedialog
import os
import re
import csv


no_regex="(?<=no\.\s)\d{1,5}|(?<=No\.\s)\d*|(?<=nr\s)\d{1,5}|(?<=Nr\s)\d{1,5}|(?<=num\.\s)\d{1,5}|(?<=iss\.\s)\d{1,5}|(?<=issue\s)\d{1,5}|(?<=Issue\s)\d{1,5}|(?<=Issue:\s)\d{1,5}"
vol_regex="(?<=vol\.\s)\d*|(?<=Vol\.\s)\d*"
article_no_regex=""
pages_in_range_regex="(?<=\ss\.\s)(?:\d+-\d+)|(?<=S\.\s)(?:\d+-\d+)|(?<=s\.\s)(?:\d+-\d+)"
publisher_name_regex="(?<=\:\s)(\s*\D+)"
publisher_location_regex="(?:[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]*)"
publisher_year_regex="(?<=\,\s)(?:\d{1,4})(?=\;)" #NIE DZIAŁĄ
global wartosci
wartosci=[]
def daj_Plik():
    sciezka = tkinter.filedialog.askopenfilename()
    return sciezka
def otworz_Plik(sciezka):
    plik = open(sciezka, 'r', encoding ='utf-8')
    zawartosc = csv.reader(plik)
    return zawartosc
def daj_wartosc_wyrazenia(wyrazenie, tekst):
    zawartosc = re.findall(wyrazenie,tekst)
    if len(zawartosc) == 0:
        return ''
    else:
        return zawartosc[0]
def wybierz_Dane(zawartosc):
    for wiersz in zawartosc:
        numer = daj_wartosc_wyrazenia(no_regex, wiersz[1])
        volume = daj_wartosc_wyrazenia(vol_regex, wiersz[1])
        numer_artykulu = daj_wartosc_wyrazenia(article_no_regex, wiersz[1])
        przedzial_stron = daj_wartosc_wyrazenia(pages_in_range_regex, wiersz[1])
        nazwa_wydawnictwa = daj_wartosc_wyrazenia(publisher_name_regex, wiersz[0])
        lokalizacja_wydawnictwa = daj_wartosc_wyrazenia(publisher_location_regex, wiersz[0])
        rok_wydania = daj_wartosc_wyrazenia(publisher_year_regex, wiersz[0])
        wiersz_wartosci = [numer, volume, numer_artykulu, przedzial_stron, nazwa_wydawnictwa, lokalizacja_wydawnictwa, rok_wydania]
        tworz_Liste_Wartosci(wiersz_wartosci)
def tworz_Liste_Wartosci(wierszWartosci):
    wartosci.append(wierszWartosci)
def zapisz_Liste_Wartosci():
    plik_wartosci = open('wartosci.csv', 'a+', encoding='utf-8')
    do_zapisu = csv.writer(plik_wartosci)
    do_zapisu.writerows(wartosci)
def usun_Plik_Wartosci():
    if os.path.exists('wartosci.csv'):
        os.remove('wartosci.csv')
usun_Plik_Wartosci()
wybierz_Dane(otworz_Plik(daj_Plik()))
#print(wartosci)
zapisz_Liste_Wartosci()
