from pathlib import Path
import os

class Site:

    def __init__(self, source, dest):
        source = self.source.Path()
        dest = self.dest.Path()

    def create_dir(self, path):
        directory = self.dest.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if os.path.isdir(path):
                create_dir(path)
            else:
                continue