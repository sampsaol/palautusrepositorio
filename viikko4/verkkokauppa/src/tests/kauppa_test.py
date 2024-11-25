import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 5
            elif tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "muna", 3)
            elif tuote_id == 3:
                return Tuote(3, "jogurtti" , 8)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        kauppa = self.kauppa
        pankki_mock = self.pankki_mock

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        kauppa = self.kauppa
        pankki_mock = self.pankki_mock

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreillä
        pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)

    def test_kahden_ostoksen_jalkeen_tilisiirtoa_kutsutaan_oikeilla_parametreilla(self):
        kauppa = self.kauppa
        pankki_mock = self.pankki_mock
        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreillä
        pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 8)

    def test_kahden_saman_ostoksen_jalkeen_tilisiirtoa_kutsutaan_oikeilla_parametreilla(self):
        kauppa = self.kauppa
        pankki_mock = self.pankki_mock

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreillä
        pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 10)

    def test_yhden_varastossa_ja_yhden_ei_varastossa_olevan_tuotteen_ostoksen_jalkeen_tilisiirtoa_kutsutaan_oikeilla_parametreilla(self):
        kauppa = self.kauppa
        pankki_mock = self.pankki_mock

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreillä
        pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)

    def test_ostosten_jalkeen_asioinnin_aloittaminen_nollaa_ostokset(self):
        kauppa = self.kauppa
        pankki_mock = self.pankki_mock

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 8)


    def test_kauppa_pyytaa_uuden_viitenumeron_eri_maksutapahtumille(self):
        kauppa = self.kauppa
        pankki_mock = self.pankki_mock
        viitegeneraattori_mock = self.viitegeneraattori_mock
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 1)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 2)    