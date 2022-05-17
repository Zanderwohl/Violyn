import pygame


class Cursor:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.offset = 10
        self.length = 30
        self.radius = 2

        self.left_down = False
        self.right_down = False

    def update(self, _events):
        self.x, self.y = pygame.mouse.get_pos()
        self.left_down = pygame.mouse.get_pressed()[0]
        self.right_down = pygame.mouse.get_pressed()[1]

    def draw(self, display_surface, fg, bg, tg):
        pygame.draw.line(display_surface, fg, (self.x - self.length - self.offset, self.y), (self.x - self.offset, self.y))
        pygame.draw.line(display_surface, fg, (self.x + self.length + self.offset, self.y), (self.x + self.offset, self.y))
        pygame.draw.line(display_surface, fg, (self.x, self.y - self.length - self.offset), (self.x, self.y - self.offset))
        pygame.draw.line(display_surface, fg, (self.x, self.y + self.length + self.offset), (self.x, self.y + self.offset))
        pygame.draw.line(display_surface, fg, (self.x, self.y), (self.x, self.y))
        pygame.draw.circle(display_surface, fg if not self.left_down else tg, (self.x, self.y), self.radius)
