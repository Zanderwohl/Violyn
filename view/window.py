import pygame


class Window:

    def __init__(self):
        pygame.init()
        self.running = True

        self.fg = (0, 0, 0)
        self.bg = (215, 205, 143)

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
        pygame.display.set_caption('Zandytext')

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

    def process_events(self):
        self.display_surface.fill(self.bg)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                    return
            if event.type == pygame.QUIT:
                self.quit()
                return

        pygame.display.update()

    def quit(self):
        pygame.quit()
        self.running = False
