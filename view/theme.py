class Theme:
    def __init__(self, fg=None, bg=None, tg=None, pos_fg=None, pos_bg=None, neg_fg=None, neg_bg=None, hl=None, ll=None,
                 hov=None, foc=None):
        self.fg = (0, 0, 0) if fg is None else fg           # Foreground
        self.bg = (255, 255, 255) if bg is None else bg     # Background
        self.tg = (0, 0, 255) if tg is None else tg         # Third-Ground
        self.pos_fg = (0, 255, 0) if pos_fg is None else pos_fg      # Positive foreground
        self.pos_bg = (0, 60, 0) if pos_bg is None else pos_bg      # Positive background
        self.neg_fg = (255, 0, 0) if neg_fg is None else neg_fg      # Negative foreground
        self.neg_bg = (60, 0, 0) if neg_bg is None else neg_bg      # Negative background
        self.hl = (50, 50, 50) if hl is None else hl        # Highlight
        self.ll = (200, 200, 200) if ll is None else ll     # Lowlight
        self.hov = (0, 200, 0) if hov is None else hov      # Hover
        self.foc = (0, 0, 200) if foc is None else foc      # Focus


DEFAULT = Theme()
CREME = Theme(fg=(81, 78, 55), bg=(215, 205, 143), tg=(60, 150, 60))
