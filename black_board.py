from asciimatics.screen import ManagedScreen
# import pyautogui


def demo() -> None:
    """Wrapper function for a blackboard"""
    stack = []
    with ManagedScreen() as screen:
        while True:
            screen.wait_for_input(30)
            a = screen.get_event()

            if hasattr(a, 'key_code'):
                if a.key_code == 99:  # c
                    screen.clear()
                    stack.clear()
                elif a.key_code == 113:  # q
                    break
            elif hasattr(a, 'buttons'):
                if a.buttons == 2:  # right_click
                    stack.append([a.x, a.y])
                    if len(stack) >= 2:
                        screen.move(*stack[-2])
                        screen.draw(*stack[-1], char='.', thin=True)
                elif a.buttons == 0:  # scroll/triple_left/double_right
                    stack.clear()
                elif a.buttons == 4:  # double_left
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            screen.print_at('*', a.x + i, a.y + j)
                else:  # left_click
                    screen.print_at('*', a.x, a.y)
            else:
                screen.print_at("Didn't detect key press or button")
            screen.refresh()


# Hack for small fontsize on Ubuntu
# for i in range(7):
#     pyautogui.hotkey('ctrl', '-')
demo()
# pyautogui.hotkey('ctrl', '0')
