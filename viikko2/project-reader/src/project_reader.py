from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        formatted_content = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(formatted_content["tool"]["poetry"]["name"], formatted_content["tool"]["poetry"]["description"],
                    formatted_content["tool"]["poetry"]["license"], formatted_content["tool"]["poetry"]["authors"],
                    formatted_content["tool"]["poetry"]["dependencies"],
                    formatted_content["tool"]["poetry"]["group"]["dev"]["dependencies"],)

