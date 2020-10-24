from pathlib import Path
import ssg.parsers

class Site:

    def __init__(self, source, dest, parsers=""):
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = parsers or []

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                run_parser(path)

    def load_parser(self, extension):
        for parser in self.parsers:
            if ssg.parsers.Parser.valid_extension(extension):
                return parser

    def run_parser(self, path):
        parser = load_parser(path.suffix)
        if parser != None:
            parser.parse(path, parser.path.source, parser.path.dest)
        else:
            print("Not Implemented")