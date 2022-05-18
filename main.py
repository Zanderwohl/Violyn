from view import window
from view.box import Box

if __name__ == "__main__":
    window = window.Window()

    test_view = Box()
    window.add_child(test_view)
    test_view.resize(top_left=(10, 10), size=(400, 400))

    test_second_view = Box()
    window.add_child(test_second_view)
    test_second_view.resize(top_left=(420, 10), size=(400, 400))

    test_second_sub_one = Box()
    test_second_view.add_child(test_second_sub_one)
    test_second_sub_one.resize(top_left=(10, 10), size=(50, 50))

    test_second_sub_two = Box()
    test_second_view.add_child(test_second_sub_two)
    test_second_sub_two.resize(top_left=(70, 10), size=(50, 50))

    test_second_sub_three = Box()
    test_second_view.add_child(test_second_sub_three)
    test_second_sub_three.resize(top_left=(10, 70), size=(50, 50))

    test_second_sub_four = Box()
    test_second_view.add_child(test_second_sub_four)
    test_second_sub_four.resize(top_left=(70, 70), size=(50, 50))

    test_third_view = Box()
    window.add_child(test_third_view)
    test_third_view.resize(top_left=(840, 10), size=(400, 400))

    test_subview = Box()
    test_view.add_child(test_subview)
    test_subview.resize(top_left=(10, 10), size=(300, 300))

    test_subsubview = Box()
    test_subview.add_child(test_subsubview)
    test_subsubview.resize(top_left=(10, 10), size=(200, 200))

    while window.running:
        window.frame()
    quit()
