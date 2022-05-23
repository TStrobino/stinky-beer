## (c) 2022 ASTRO YEAST
from multiprocessing.connection import wait
from rich import print
from rich.progress import Progress
from rich.panel import Panel
from rich.text import Text
import PhotoActivation
import time
def main():
    print("Init...")
    print(Panel(Text("ASTRO", justify="center", style="bold green")))
    PhotoActivation.setup_GPIO()
    PhotoActivation.setBlue(255)
    time.sleep(1)
    PhotoActivation.setGreen(255)
    time.sleep(1)
    PhotoActivation.setRed(255)
    time.sleep(20)
    print("Exiting...")






if __name__ == "__main__":
    main()