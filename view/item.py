

class Item:
    def __init__(self, parent=None):
        self.clickable = False
        self.visible = True
        self.children = {}
        self.child_id = 0
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.my_id = None
        self.parent = parent
        self._display_surface = None
        self.level = 0

    def absolute_coords(self):
        if self.parent is None:
            return 0, 0
        par_x, par_y = self.parent.absolute_coords()
        return self.x + par_x, self.y + par_y

    def display_surface(self):
        if self._display_surface is not None:
            return self._display_surface
        elif self.parent is not None:
            return self.parent.display_surface()
        return None

    def add_child(self, child):
        key = f'Child {self.child_id}'
        child.my_id = key
        self.child_id += 1
        self.children[key] = child
        child.parent = self
        child.set_level(self.level + 1)
        return key

    def remove_child(self, child_id):
        del self.children[child_id]

    def set_level(self, level):
        self.level = level
        for child in self.children:
            child.set_level(level + 1)

    def orphan_self(self):
        self.parent.remove_child(self.my_id)
        self.my_id = None
        self.parent = None
