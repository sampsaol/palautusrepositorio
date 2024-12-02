KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        try:
            self.kapasiteetti = int(kapasiteetti) if kapasiteetti is not None else KAPASITEETTI
        except ValueError:
            raise Exception("Väärämuotoinen kapasiteetti")

        try:
            self.kasvatuskoko = int(kasvatuskoko) if kasvatuskoko is not None else OLETUSKASVATUS 
        except ValueError:
            raise Exception("Väärämuotoinen kasvatuskoko")

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, haettava_luku):
        kuuluu_listaan = 0

        for i in range(0, self.alkioiden_lkm):
            if haettava_luku == self.ljono[i]:
                return True
        return False

    def lisaa(self, lisattava_luku):
        if not self.kuuluu(lisattava_luku):
            if self.alkioiden_lkm == len(self.ljono):
                self._pidenna_listaa()
            self.ljono[self.alkioiden_lkm] = lisattava_luku
            self.alkioiden_lkm += 1
            return True
        return False

    def _pidenna_listaa(self):
        taulukko_old = self.ljono
        self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(taulukko_old, self.ljono)
        return

    def poista(self, poistettava_luku):
        poistettavan_luvun_indeksi = -1
        apu = 0

        for i in range(self.alkioiden_lkm):
            if poistettava_luku == self.ljono[i]:
                self.ljono[i:self.alkioiden_lkm-1] = self.ljono[i+1:self.alkioiden_lkm]
                self.ljono[self.alkioiden_lkm-1] = 0
                self.alkioiden_lkm -= 1
                return True
        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
