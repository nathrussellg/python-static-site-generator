import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):

    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @classmethod
    def load(self, cls, string):
        _, fm, content = __regex.split(string, 2)
        load(fm, Loader = FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data if "type" else None

    @type.setter
    def type(self, val):
        type = self.data["type"]

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        # Self.data interator method

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        return str(data)

    