from asciimatics.screen import ManagedScreen
from time import sleep

mat = [[".    ● . ..   .               . "],
       ["●  . ..   ●  .... .  ●  ..    . "]]


def render(screen=None):
    for idx,i in enumerate(mat):
        screen.print_at(i[0],0,idx)
    screen.refresh()

@ManagedScreen
def demo(screen=None):
    render(screen)
    screen.wait_for_input(10)
    a = screen.get_event()
    if mat[a.y][0][a.x] == "●":
        mat[a.y][0] = mat[a.y][0][:a.x] + "◉" + mat[a.y][0][a.x+1:]
    render(screen)
    screen.refresh()
    sleep(10)
    screen.close()

demo()
