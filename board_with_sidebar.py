from asciimatics.screen import ManagedScreen
# import pyautogui


def export() -> None:
    """Literally does nothing but here's a docstring (can you tell i'm slightly salty)"""
    pass


def was_color_clicked(x: int, y: int) -> bool:
    """Checks if the click was within bounds of the color selection box"""
    x_end = screen.width
    y_end = ((((screen.height//2)//4)*2)+2)-1
    x_start = screen.width-(((screen.width//5)//4)*(4))
    y_start = 2
    return x <= x_end and x >= x_start and y <= y_end and y >= y_start


def which_color(x: int, y: int) -> int:
    """Returns the color which was clicked on provided there was one."""
    w = screen.width
    h = screen.height
    colour_spot_w = (w//5)//4
    colour_spot_h = ((h//2)//4)

    for k in range(4):
        if (x <= w-(colour_spot_w*k) and x >= w-(colour_spot_w*(k+1))
                and y >= 2 and y <= colour_spot_h+2):
            return k
        if (x <= w-(colour_spot_w*k) and x >= w-(colour_spot_w*(k+1))
                and y >= colour_spot_h+2 and y <= (colour_spot_h*2)+2):
            return k+4


def which_marker(x: int, y: int) -> int:
    """Returns the marker clicked on or None"""
    for index, value in enumerate(["*", ".", "@", "$", "o", "▇"]):
        if x == screen.width-(screen.width//5)+(index*2) and y == (((screen.height//2)//4)*2)+4:
            return value
    return None


def which_button(x: int, y: int) -> str:
    """Returns the button that was clicked"""
    w = screen.width
    h = screen.height
    if x >= w//5*4+1 and y < h//2+3 and x <= w-1 and y >= h//2+1:
        return "clear"
    if x >= w//5*4+1 and y >= h//2+4 and x <= w-1 and y < h//2+6:
        return "export"
    return None


def print_sidebar(screen: ManagedScreen) -> None:
    """Displays the sidebar"""
    w = screen.width
    h = screen.height
    colour_spot_w = (w//5)//4
    colour_spot_h = ((h//2)//4)

    screen.fill_polygon([[(w//5*4, 0), (w, 0), (w, h//2), (w//5*4, h//2)]], bg=7)
    screen.fill_polygon([[(w//5*4, h), (w, h), (w, h//2), (w//5*4, h//2)]], bg=6, colour=6)
    screen.print_at("Select color:", w-(colour_spot_w*4), 0, 5)

    # Colors
    for i in range(4):
        screen.fill_polygon([[
            (w-(colour_spot_w*(i+1)), 2),
            (w-(colour_spot_w*i), 2),
            (w-(colour_spot_w*i), colour_spot_h+2),
            (w-(colour_spot_w*(i+1)), colour_spot_h+2)
        ]], bg=i, colour=i)
        screen.fill_polygon([[
            (w-(colour_spot_w*(i+1)), colour_spot_h+2),
            (w-(colour_spot_w*i), colour_spot_h+2),
            (w-(colour_spot_w*i), (colour_spot_h*2)+2),
            (w-(colour_spot_w*(i+1)), (colour_spot_h*2)+2)
        ]], bg=i+4, colour=i+4)

    # Markers
    screen.print_at("Select marker:", w-(colour_spot_w*4), (colour_spot_h*2)+3, 6)
    for index, value in enumerate(["*", ".", "@", "$", "o", "▇"]):
        screen.print_at(value, w-(colour_spot_w*(4))+(index*2), (colour_spot_h*2)+4, 0, bg=7)

    # Other buttons
    screen.fill_polygon([[(w//5*4+1, h//2+3), (w-1, h//2+3), (w-1, h//2+1), (w//5*4+1, h//2+1)]],
                        bg=4, colour=4)
    screen.fill_polygon([[(w//5*4+1, h//2+6), (w-1, h//2+6), (w-1, h//2+4), (w//5*4+1, h//2+4)]],
                        bg=5, colour=5)
    screen.print_at("Clear", w//5*4+1, h//2+1, 7, bg=4)
    screen.print_at("Export", w//5*4+1, h//2+4, 7, bg=5)

    screen.refresh()


stack = []
with ManagedScreen() as screen:
    print_sidebar(screen)
    current_color = 7
    current_marker = "*"

    while True:
        screen.wait_for_input(5)
        a = screen.get_event()

        if hasattr(a, 'key_code'):
            if a.key_code == 99:  # c
                screen.clear()
                stack.clear()
                print_sidebar(screen)

            elif a.key_code == 113:  # q
                break
        elif hasattr(a, 'buttons'):
            if a.x >= screen.width//5*4:
                if was_color_clicked(a.x, a.y):
                    current_color = which_color(a.x, a.y)
                else:
                    temp = which_marker(a.x, a.y)
                    if temp is not None:
                        current_marker = temp
                    temp = which_button(a.x, a.y)
                    if temp == "export":
                        export()
                    elif temp == "clear":
                        screen.clear()
                        stack.clear()
                        print_sidebar(screen)
            else:
                if a.buttons == 2:  # right_click
                    stack.append([a.x, a.y])
                    if len(stack) >= 2:
                        screen.move(*stack[-2])
                        screen.draw(*stack[-1], char=current_marker, thin=True, colour=current_color)
                elif a.buttons == 0:  # scroll/triple_left/double_right
                    stack.clear()
                elif a.buttons == 4:  # double_left
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            screen.print_at(current_marker, a.x + i, a.y + j, current_color)
                else:  # left_click
                    screen.print_at(current_marker, a.x, a.y, current_color)
        else:
            # screen.print_at("Didn't detect key press or button",0,0)
            pass

        screen.refresh()
