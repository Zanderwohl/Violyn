class Theme:
    def __init__(self, fg=None, bg=None, tg=None, pos=None, neg=None, hl=None, ll=None):
        self.fg = (0, 0, 0) if fg is None else fg           # Foreground
        self.bg = (255, 255, 255) if bg is None else bg     # Background
        self.tg = (0, 0, 255) if tg is None else tg         # Third-Ground
        self.pos = (0, 255, 0) if pos is None else pos      # Positive
        self.neg = (255, 0, 0) if neg is None else neg      # Negative
        self.hl = (50, 50, 50) if hl is None else hl        # Highlight
        self.ll = (200, 200, 200) if ll is None else ll     # Lowlight


DEFAULT = Theme()
CREME = Theme(fg=(81, 78, 55), bg=(215, 205, 143), tg=(60, 150, 60))
