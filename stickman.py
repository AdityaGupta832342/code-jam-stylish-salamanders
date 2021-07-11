from rich import console
from rich.live import Live
from time import sleep
from rich.console import Console
character = {"Head":" O ","Chest":"/|\\","legs":"/ \\",}
console = Console(color_system='truecolor',height=10)

def getstring():
    return "\n".join(v for k,v in character.items())

with Live(console=console,renderable=getstring(),refresh_per_second=4,transient=True) as live:
    for _ in range(80):
        sleep(0.4)
        live.update(getstring())
        for k,v in character.items():
            v = " " + v
            character[k] = v
        
     