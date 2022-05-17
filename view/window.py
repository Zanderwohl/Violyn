import pygame

from view.cursor import Cursor
from view import theme
from view.item import Item


class Window(Item):

    def __init__(self):
        pygame.init()
        self.running = True
        self.parent = None

        self.theme = theme.CREME

        # Screen area in characters
        self.WIDTH = 80
        self.HEIGHT = 24

        # Screen area in pixels
        self.height = 1080
        self.width = 1920

        self.x = 0
        self.y = 0

        # Not real pixels. Aspect ratio of character.
        self.BLOCK_WIDTH = 5
        self.BLOCK_HEIGHT = 7

        # Real pixels each character takes up.
        self.block_pixel_width = 0
        self.block_pixel_height = 0

        self.display_surface = None
        self.resize(self.width, self.height, fullscreen=True)
        pygame.display.set_caption('Violyn')

        self.cursor = Cursor(self)
        self.cursor.hide()
        self.cursor.set_pos(self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] // 2)
        pygame.mouse.set_visible(False)

        self.children = {'cursor': self.cursor}
        self.views = {}
        self.view_id = 0

    def resize(self, width, height, fullscreen=False):
        # Estimate real pixels sizes of each character. Based on width. Excess height can be given a scrollbar.
        self.block_pixel_width = width // self.WIDTH  # TODO: Subtract scrollbar width?
        self.block_pixel_height = round(((width / self.WIDTH) / self.BLOCK_WIDTH) * self.BLOCK_HEIGHT)

        if fullscreen:
            self.display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.width, self.height = pygame.display.get_window_size()
        else:
            self.width = width
            self.height = height
            self.display_surface = pygame.display.set_mode((self.width, self.height))

    def add_view(self, view):
        key = f'View {self.view_id}'
        self.view_id += 1
        self.children[key] = view
        self.views[key] = view
        view.parent = self
        return key

    def remove_view(self, view_key):
        del self.views[view_key]
        del self.children[view_key]

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
            for _key, child in self.children.items():
                child.update(events)

    def draw_screen(self):
        self.display_surface.fill(self.theme.bg)
        for _key, child in self.children.items():
            child.draw(self.display_surface, self.theme)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        self.running = False
