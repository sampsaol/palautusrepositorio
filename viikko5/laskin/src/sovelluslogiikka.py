class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen_arvo = None

    def miinus(self, operandi):
        self._tallenna_edellinen()
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._tallenna_edellinen()
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._tallenna_edellinen()
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def kumoa(self):
        if self._edellinen_arvo is not None:
            self._arvo = self._edellinen_arvo
            self._edellinen_arvo = None

    def _tallenna_edellinen(self):
        self._edellinen_arvo = self._arvo