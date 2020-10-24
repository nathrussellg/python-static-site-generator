from typing import List
from pathlib import Path
import shutil

class Parser:

    def __init__(self):
        self.extensions: List[str] = []

    def valid_extensions(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, rt) as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / with_suffix(path + ext).name
        with open(full_path, wt) as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / relative_to(source))

    class ResourceParser:

        extensions = [".jpg", ".png", ".gif", ".css", ".html"]

        def parse(self, path: Path, source: Path, dest: Path):
            Parser.copy(path, source, dest)
