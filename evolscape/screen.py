# -*- coding: utf-8 -*-

class Screen(object):
    def __init__(self, game):
        self.game = game
        self.background = None

    def show():
        raise NotImplementedError

    def hide():
        raise NotImplementedError

    def update(self, dt):
        raise NotImplementedError

    def draw(self, dt):
        raise NotImplementedError

    def get_background(self):
        return self.background


class MainMenuScreen(Screen):
    def __init__(self, game):
        Screen.__init__(self, game)

    def show(self):
        # init crap
        pass

    def update(self, dt):
        # if button is clicked, show game screen
        # self.game.set_screen(GameScreen(self.game))
        pass

    def draw(self, dt):
        pass


class GameScreen(Screen):
    def __init__(self, game):
        Screen.__init__(self, game)

    def show(self):
       pass

    def update(self, dt):
        pass

    def draw(self, dt):
        pass
