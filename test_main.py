from unittest import TestCase
from main import otworz_Plik,daj_Plik,daj_wartosc_wyrazenia
no_regex="(?<=no\.\s)\d{1,5}|(?<=No\.\s)\d*|(?<=nr\s)\d{1,5}|(?<=Nr\s)\d{1,5}|(?<=num\.\s)\d{1,5}|(?<=iss\.\s)\d{1,5}|(?<=issue\s)\d{1,5}|(?<=Issue\s)\d{1,5}|(?<=Issue:\s)\d{1,5}"
vol_regex="(?<=vol\.\s)\d*|(?<=Vol\.\s)\d*"
article_no_regex=""
pages_in_range_regex="(?<=\ss\.\s)(?:\d+-\d+)|(?<=S\.\s)(?:\d+-\d+)|(?<=s\.\s)(?:\d+-\d+)"
publisher_name_regex="(?<=\:\s)(\s*\D+)"
publisher_location_regex="(?:[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]*)"
publisher_year_regex="(?<=\,\s)(?:\d{1,4})(?=\;)"
zawartosc = otworz_Plik(daj_Plik())
class Test(TestCase):
    def test_daj_wartosc_NUMER(self):
        for wiersz in zawartosc:
            with self.subTest():
                self.assertEqual(daj_wartosc_wyrazenia(wiersz[1], no_regex), wiersz[3])
   # def test_daj_wartosc_vol(self):
    #    for wiersz in zawartosc:
     #       with self.subTest():
      #          self.assertEqual(daj_wartosc_wyrazenia(wiersz[1], vol_regex), wiersz[4])
    #def test_daj_wartosc_pages(self):
     #   for wiersz in zawartosc:
      #      with self.subTest():
       #         self.assertEqual(daj_wartosc_wyrazenia(wiersz[1], pages_regex), wiersz[2])