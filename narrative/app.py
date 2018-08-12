import pyxel

from narrative.text import Text


TEXT = "Hello, Pyxel!"


class App:
    def __init__(self):
        self.text = Text("data/text.json")
        pyxel.init(256, 192, caption="narrative")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.text.update()

    def draw(self):
        pyxel.cls(1)
        pyxel.text(
            pyxel.width / 2 - 4 * len(TEXT) / 2, 16, TEXT, pyxel.frame_count % 16
        )
        self.text.draw()


App()
