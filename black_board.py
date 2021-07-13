from time import sleep

from asciimatics.screen import ManagedScreen


def demo() -> None:
    """Wrapper function for creating a screen as black board."""
    a = None
    with ManagedScreen() as screen:
        while a is None:
            screen.wait_for_input(30)
            a = screen.get_event()
            if a.buttons in (1, 4):
                screen.print_at("*", a.x, a.y)
                screen.refresh()
                a = None
            else:
                a = "yo"
    sleep(3)


demo()
