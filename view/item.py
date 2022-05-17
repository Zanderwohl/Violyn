

class Item:
    def absolute_coords(self):
        if self.parent is None:
            return 0, 0
        par_x, par_y = self.parent.absolute_coords()
        return self.x + par_x, self.y + par_y
