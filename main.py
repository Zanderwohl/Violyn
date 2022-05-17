from view import window
from view.view import View

if __name__ == "__main__":
    window = window.Window()
    test_view = View()
    window.add_view(test_view)
    test_view.resize(top_left=(10, 10), size=(50, 50))
    while window.running:
        window.frame()
    quit()
