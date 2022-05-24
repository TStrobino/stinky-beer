## (c) 2022 ASTRO YEAST
from multiprocessing.connection import wait
from rich import print
from rich.progress import Progress
from rich.panel import Panel
from rich.text import Text
import PhotoActivation
import time
import signal
import sys
import config
import subprocess

def main():
    subprocess.run(["clear"])
    print("Init...")
    # SETUP
    signal.signal(signal.SIGINT, handle_sigint)

    print(Panel(Text("ASTRO YEAST STINKY BEER", justify="center", style="bold green")))
    PhotoActivation.setup_GPIO()
    PhotoActivation.setBlue(255)
    PhotoActivation.setGreen(255)
    PhotoActivation.setRed(255)
    print("Exiting...")
    PhotoActivation.stop_GPIO()



def handle_sigint(sig, frame):
    print('Stopping...')
    PhotoActivation.stop_GPIO()
    sys.exit(0)


if __name__ == "__main__":
    main()