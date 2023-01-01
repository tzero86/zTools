from time import monotonic
from textual.app import App, ComposeResult, RenderResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Header, Footer, Static
from textual.widget import Widget
import socket
import time
import datetime
import getpass
import os


class Banner(Widget):
    """Display a greeting."""

    def get_user(self):
        try:
            username = getpass.getuser()
        except:
            username = os.getlogin()
        return reactive(username)

    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return reactive(ip)

    def get_time(self):
        current_time = datetime.datetime.now()
        time_string = reactive("")
        time_string = current_time.strftime('%Y-%m-%d %H:%M:%S')
        return time_string

    def render(self) -> RenderResult:
        return f"""
                     ░▀▀█░▀█▀░█▀█░█▀█░█░░░█▀▀
                     ░▄▀░░░█░░█░█░█░█░█░░░▀▀█
                     ░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀░▀▀▀
                            
━─━────༺ 🌐 {self.get_ip()}  ⌛ {self.get_time()}  👤 {self.get_user()} ༻────━─━
        """


class Tools(Widget):
    tools_list = {
        "zScan": "A subdomain scanner",
        "QMC": "A Quick Mac Address Changer.",
        "lameScan": "A Multi-threaded port scanner.",
        "zFuzz": "A Multi-threaded Fuzzer."
    }

    def available_tools(self):
        menu = ""
        menu_index = 0
        menu += '╚⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤╗ MAIN MENU ╔⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤╝\n\n'
        for tool, description in self.tools_list.items():
            menu += f"      [{menu_index}] {tool}: {description} \n"
            menu_index += 1
        menu += f"      [999] Exit.\n\n"
        menu += '\n\n'
        return menu

    def render(self) -> RenderResult:
        return self.available_tools()


class Ztools(App):
    """Tzero86's Personal Toolkit"""
    CSS_PATH = "styles.css"
    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode")]

    def compose(self) -> ComposeResult:
        # we create the main areas of the app
        yield Header()
        yield Footer()
        yield Container(Banner(), Tools())

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark


# we start our app main loop
if __name__ == "__main__":
    app = Ztools()
    app.run()
