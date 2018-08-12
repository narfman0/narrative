import json

import pyxel


TEXT_LINE_HEIGHT = 6
TEXT_COLOR = 7

class Text:
    def __init__(self, path):
        with open(path) as data:
            self.data = json.loads(data.read())
        self.step = 0
        self.alignment = {}

    def draw(self):
        chunk = self.current_chunk()
        if chunk is None:
            return
        y = .6 * pyxel.height
        pyxel.text(16, y, chunk["text"], TEXT_COLOR)
        if 'responses' in chunk:
            for index, response in enumerate(chunk['responses']):
                y += TEXT_LINE_HEIGHT
                text = '%d: %s' % (index+1, response["text"])
                pyxel.text(16, y, text, TEXT_COLOR)

    def update(self):
        chunk = self.current_chunk()
        if chunk is None:
            return
        if 'responses' in chunk:
            for key in [pyxel.KEY_1, pyxel.KEY_2, pyxel.KEY_3, pyxel.KEY_4]:
                if pyxel.btnp(key):
                    self.modify_alignment(chunk['responses'][key - pyxel.KEY_1]['alignment'])
                    self.increment()
        else:
            if pyxel.btnp(pyxel.KEY_N):
                self.increment()

    def increment(self, steps=1):
        self.step += steps

    def current_chunk(self):
        if self.step >= len(self.data):
            return None
        return self.data[self.step]

    def modify_alignment(self, decision):
        """ Given we have made a decision, add to alignment """
        current = self.alignment.get(decision, 0)
        self.alignment[decision] = current + 1