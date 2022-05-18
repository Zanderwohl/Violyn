import pygame

from view.item import Item


class Cursor(Item):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.offset = 10
        self.length = 30
        self.radius = 2

        self.left_down = False
        self.right_down = False

    def update(self, _events):
        if self.visible:
            self.x, self.y = pygame.mouse.get_pos()
            self.left_down = pygame.mouse.get_pressed()[0]
            self.right_down = pygame.mouse.get_pressed()[1]

    def draw(self, display_surface, theme):
        if not self.visible:
            return
        pygame.draw.line(display_surface, theme.fg, (self.x - self.length - self.offset, self.y), (self.x - self.offset, self.y))
        pygame.draw.line(display_surface, theme.fg, (self.x + self.length + self.offset, self.y), (self.x + self.offset, self.y))
        pygame.draw.line(display_surface, theme.fg, (self.x, self.y - self.length - self.offset), (self.x, self.y - self.offset))
        pygame.draw.line(display_surface, theme.fg, (self.x, self.y + self.length + self.offset), (self.x, self.y + self.offset))
        pygame.draw.line(display_surface, theme.fg, (self.x, self.y), (self.x, self.y))
        pygame.draw.circle(display_surface, theme.fg if not self.left_down else theme.tg, (self.x, self.y), self.radius)

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        pygame.mouse.set_pos(x, y)

    def hide(self):
        self.visible = False

    def show(self, x=None, y=None):
        self.visible = True
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        self.set_pos(x, y)

    def toggle_visibility(self, x=None, y=None):
        if self.visible:
            self.hide()
        else:
            self.show(x=x, y=y)
