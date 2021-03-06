import pygame

from view.item import Item


class Box(Item):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.clickable = True

        self.border = 2

    def update(self, _events):
        pass

    def draw(self, display_surface, theme):
        absolute_x, absolute_y = self.absolute_coords()
        color = theme.hl if self.level % 2 == 0 else theme.ll
        pygame.draw.rect(display_surface, color, (absolute_x, absolute_y, self.width, self.height))
        if self.is_hovered:
            pygame.draw.line(display_surface, theme.hov, (absolute_x, absolute_y),
                             (absolute_x + self.width, absolute_y))
            pygame.draw.line(display_surface, theme.hov, (absolute_x, absolute_y),
                             (absolute_x, absolute_y + self.height))
            pygame.draw.rect(display_surface, theme.hov, (absolute_x, absolute_y, 5, 5))
        if self.is_focused:
            pygame.draw.line(display_surface, theme.foc, (absolute_x + self.width, absolute_y + self.height),
                             (absolute_x + self.width, absolute_y))
            pygame.draw.line(display_surface, theme.foc, (absolute_x + self.width, absolute_y + self.height),
                             (absolute_x, absolute_y + self.height))
            pygame.draw.rect(display_surface, theme.foc,
                             (absolute_x + self.width - 5, absolute_y + self.height - 5, 5, 5))
        for key, child in self.children.items():
            child.draw(self.display_surface(), theme)

    def resize(self, top_left=None, bottom_right=None, size=None):
        if top_left is None:
            raise Exception('Must provide top right.')
        if bottom_right is None and size is None:
            raise Exception('Must provide bottom right or size.')
        if bottom_right is not None and size is not None:
            raise Exception('Cannot provide both bottom right and size.')
        self.x = top_left[0]
        self.y = top_left[1]
        if bottom_right is not None:
            if bottom_right[0] < top_left[0]:
                raise Exception('X coordinates in wrong order.')
            if bottom_right[1] < top_left[1]:
                raise Exception('Y coordinates in wrong order.')
            new_width = bottom_right[0] - top_left[0]
            new_height = bottom_right[1] - top_left[1]
        else:
            new_width = size[0]
            new_height = size[1]
        if new_height > self.parent.height:
            raise Exception(f'Height is greater than parent height! ({new_height} > {self.parent.height})')
        if new_width > self.parent.width:
            raise Exception(f'Width is greater than parent width! ({new_width} > {self.parent.width})')
        self.width = new_width
        self.height = new_height

    def orphan_self(self):
        invert_op = getattr(self.parent, "remove_view", None)
        if callable(invert_op):
            self.parent.remove_view(self.my_id)
            self.my_id = None
            self.parent = None
        else:
            super().orphan_self()
