from view import window

if __name__ == "__main__":
    window = window.Window()
    while window.running:
        window.process_events()
    quit()
