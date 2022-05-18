
class Item:
    def __init__(self, parent=None):
        self.clickable = False
        self.is_focused = False
        self.is_hovered = False

        self.visible = True
        self.children = {}
        self.children_keys = []
        self.child_id = 0
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.my_id = None
        self.parent = parent
        self._display_surface = None
        self.level = 0

        self.click_handler = lambda position: print(position)

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
        self.children_keys = list(self.children)
        return key

    def remove_child(self, child_id):
        del self.children[child_id]
        self.children_keys = list(self.children)

    def set_level(self, level):
        self.level = level
        for child in self.children:
            child.set_level(level + 1)

    def orphan_self(self):
        self.parent.remove_child(self.my_id)
        self.my_id = None
        self.parent = None

    def is_inside(self, position):
        x, y = position
        my_x, my_y = self.absolute_coords()
        return my_x <= x <= my_x + self.width and my_y <= y <= my_y + self.height

    def list_hits(self, position):
        hits = []
        if self.is_inside(position):
            for key in reversed(self.children):
                child = self.children[key]
                if not child.clickable:
                    continue
                child_hits = child.list_hits(position)
                if child_hits is not None and len(child_hits) > 0:
                    hits.extend(child_hits)
            if self.clickable:
                hits.append(self)
        return hits

    def click(self, position):
        x, y = position
        my_x, my_y = self.absolute_coords()
        rel_x, rel_y = x - my_x, y - my_y
        self.click_handler((rel_x, rel_y))

    def hover_in(self):
        self.is_hovered = True

    def hover_out(self):
        self.is_hovered = False

    def focus_in(self):
        self.is_focused = True

    def focus_out(self):
        self.is_focused = False

    def previous_sibling(self, focusable=False):
        return self.parent.previous_child(self.my_id, focusable)

    def next_sibling(self, focusable=False):
        return self.parent.next_child(self.my_id, focusable)

    def next_child(self, child_key, focusable=False):
        try:
            next_key = self.children_keys[self.children_keys.index(child_key) + 1]
        except (ValueError, IndexError):
            next_key = self.children_keys[0]
        candidate = self.children[next_key]
        return candidate if candidate.clickable or not focusable else self.next_child(next_key, focusable=focusable)

    def previous_child(self, child_key, focusable=False):
        try:
            prev_key = self.children_keys[self.children_keys.index(child_key) - 1]
        except (ValueError, IndexError):
            prev_key = self.children_keys[-1]
        candidate = self.children[prev_key]
        return candidate if candidate.clickable or not focusable else self.previous_child(prev_key, focusable=focusable)

    def first_child(self, focusable=False):
        if len(self.children_keys) == 0:
            return None
        last_key = self.children_keys[-1]
        first_child = self.next_child(last_key, focusable=focusable)
        return first_child
