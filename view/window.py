import pygame

from view.cursor import Cursor
from view import theme


class Window:

    def __init__(self):
        pygame.init()
        self.running = True

        self.theme = theme.CREME

        # Screen area in characters
        self.WIDTH = 80
        self.HEIGHT = 24

        # Screen area in pixels
        self.pixel_height = 1080
        self.pixel_width = 1920

        # Not real pixels. Aspect ratio of character.
        self.BLOCK_WIDTH = 5
        self.BLOCK_HEIGHT = 7

        # Real pixels each character takes up.
        self.block_pixel_width = 0
        self.block_pixel_height = 0

        self.display_surface = None
        self.resize(self.pixel_width, self.pixel_height, fullscreen=True)
        pygame.display.set_caption('Violyn')

        self.cursor = Cursor(self)
        pygame.mouse.set_visible(False)

        self.children = [self.cursor]

    def resize(self, width, height, fullscreen=False):
        self.pixel_width = width
        self.pixel_height = height

        # Estimate real pixels sizes of each character. Based on width. Excess height can be given a scrollbar.
        self.block_pixel_width = width // self.WIDTH  # TODO: Subtract scrollbar width?
        self.block_pixel_height = round(((width / self.WIDTH) / self.BLOCK_WIDTH) * self.BLOCK_HEIGHT)

        if fullscreen:
            self.display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.display_surface = pygame.display.set_mode((self.pixel_width, self.pixel_height))

    def frame(self):
        if self.running:
            self.process_events()
            if self.running:
                self.draw_screen()

    def process_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_SLASH:
                    self.cursor.toggle_visibility()
            if event.type == pygame.QUIT:
                self.quit()
        if self.running:
            for child in self.children:
                child.update(events)

    def draw_screen(self):
        self.display_surface.fill(self.theme.bg)
        for child in self.children:
            child.draw(self.display_surface)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        self.running = False
