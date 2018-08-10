import json

import pyxel


class Text:
    def __init__(self, path):
        with open(path) as data:
            self.data = json.loads(data.read())
        self.step = 0

    def increment(self, steps=1):
        self.step += steps

    def draw(self):
        chunk = self.data[self.step]
        pyxel.text(16, pyxel.height / 2, chunk["text"], 7)
