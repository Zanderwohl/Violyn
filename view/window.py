import pygame

from view.cursor import Cursor
from view import theme
from view.item import Item


class Window(Item):

    def __init__(self):
        pygame.init()
        super().__init__()
        self.running = True

        self.theme = theme.CREME

        # Screen area in characters
        self.WIDTH = 80
        self.HEIGHT = 24

        # Screen area in pixels
        self.height = 1080
        self.width = 1920

        # Not real pixels. Aspect ratio of character.
        self.BLOCK_WIDTH = 5
        self.BLOCK_HEIGHT = 7

        # Real pixels each character takes up.
        self.block_pixel_width = 0
        self.block_pixel_height = 0

        self._display_surface = None
        self.resize(self.width, self.height, fullscreen=False)
        pygame.display.set_caption('Violyn')

        self.cursor = Cursor(self)
        self.cursor.hide()
        self.cursor.set_pos(self._display_surface.get_size()[0] // 2, self._display_surface.get_size()[1] // 2)
        pygame.mouse.set_visible(False)

        self.current_hover = None
        self.current_focus = None

        self.add_child(self.cursor)
        self.views = {}
        self.view_id = 0

        self.click_start = None

    def resize(self, width, height, fullscreen=False):
        # Estimate real pixels sizes of each character. Based on width. Excess height can be given a scrollbar.
        self.block_pixel_width = width // self.WIDTH  # TODO: Subtract scrollbar width?
        self.block_pixel_height = round(((width / self.WIDTH) / self.BLOCK_WIDTH) * self.BLOCK_HEIGHT)

        if fullscreen:
            self._display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.width, self.height = pygame.display.get_window_size()
        else:
            self.width = width
            self.height = height
            self._display_surface = pygame.display.set_mode((self.width, self.height))

    def add_view(self, view):
        key = super().add_child(view)
        self.views[key] = view
        return key

    def remove_view(self, view_key):
        super().remove_child(view_key)
        del self.views[view_key]

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
            if event.type == pygame.MOUSEMOTION:
                if self.cursor.visible:
                    position = pygame.mouse.get_pos()
                    hits = self.list_hits(position)
                    prev_hover = self.current_hover
                    if prev_hover is not None:
                        prev_hover.hover_out()
                    if len(hits) > 0:
                        top_hit = hits[0]
                        self.current_hover = top_hit
                        top_hit.hover_in()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.cursor.visible:
                    position = pygame.mouse.get_pos()
                    hits = self.list_hits(position)
                    if len(hits) > 0:
                        top_hit = hits[0]
                        self.click_start = top_hit
                    else:
                        self.click_start = None
            if event.type == pygame.MOUSEBUTTONUP:
                if self.cursor.visible:
                    position = pygame.mouse.get_pos()
                    hits = self.list_hits(position)
                    if len(hits) > 0:
                        top_hit = hits[0]
                        if self.click_start == top_hit:
                            self.set_focus(top_hit)
                            top_hit.click(position)
            if event.type == pygame.QUIT:
                self.quit()
        if self.running:
            for _key, child in self.children.items():
                child.update(events)

    def set_focus(self, element):
        if self.current_focus is not None:
            self.current_focus.focus_out()
        self.current_focus = element
        self.current_focus.focus_in()

    def draw_screen(self):
        self._display_surface.fill(self.theme.bg)
        for key in reversed(self.children):
            child = self.children[key]
            child.draw(self._display_surface, self.theme)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        self.running = False
