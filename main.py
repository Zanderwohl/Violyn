from view import window
from view.box import Box

if __name__ == "__main__":
    window = window.Window()

    test_view = Box()
    window.add_child(test_view)
    test_view.resize(top_left=(10, 10), size=(400, 400))

    test_subview = Box()
    test_view.add_child(test_subview)
    test_subview.resize(top_left=(10, 10), size=(300, 300))

    test_subsubview = Box()
    test_subview.add_child(test_subsubview)
    test_subsubview.resize(top_left=(10, 10), size=(200, 200))

    while window.running:
        window.frame()
    quit()
