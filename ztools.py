from textual.app import App, ComposeResult, RenderResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Header, Footer, Static, Input, TextLog
from textual.widget import Widget
from textual import events
import socket
import datetime
import getpass
import os
from libs.Keyring import Keys
from mods.Zscanner import ZScan
from mods.Bryce import Bryce

class Banner(Widget):

    def get_user(self):
        """
        If the getpass module is available, use it to get the username, otherwise use the os module
        :return: The username of the user running the script.
        """
        try:
            username = getpass.getuser()
        except:
            username = os.getlogin()
        return username

    def get_ip(self):
        """
        It returns the IP address of the machine.
        :return: The IP address of the machine.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def get_time(self):
        """
        It returns the current time in the format of 'YYYY-MM-DD HH:MM:SS'
        :return: The current time in the format of YYYY-MM-DD HH:MM:SS
        """
        current_time = datetime.datetime.now()
        time_string = current_time.strftime('%Y-%m-%d %H:%M:%S')
        return time_string

    def render(self) -> RenderResult:
        """
        It returns a string that contains the IP address, time, and username of the user
        :return: The return value is a string.
        """
        return f"""
                       ░▀▀█░▀█▀░█▀█░█▀█░█░░░█▀▀
                       ░▄▀░░░█░░█░█░█░█░█░░░▀▀█
                       ░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀░▀▀▀
                            
━─━────༺ 🌐 {self.get_ip()}  ⌛ {self.get_time()}  👤 {self.get_user()} ༻────━─━
        """


class Tools(Widget):
    # A dictionary of tools and their descriptions.
    tools_list = {
        "zScan": "A subdomain scanner",
        "QMC": "A Quick Mac Address Changer.",
        "lameScan": "A Multi-threaded port scanner.",
        "zFuzz": "A Multi-threaded Fuzzer."
    }

    def available_tools(self):
        """
        It takes a dictionary of tools and their descriptions, and returns a menu of those tools
        :return: The menu is being returned.
        """
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
        """
        It returns a list of all the tools that are available to the user
        :return: The available_tools() function is being returned.
        """
        return self.available_tools()


class Wiki(Widget):
    mr_bryce = Bryce()
    
    def askGPT(self, question):    
        return self.mr_bryce.ask(question)
        
    def compose(self) -> ComposeResult:
        yield Input(id='question', placeholder='What do you want to know?')
        yield TextLog(highlight=True, markup=True, wrap=True, id="Answer")
        
    
    def action_set_background(self, color: str) -> None:
        self.screen.styles.background = color

    def on_key(self, event: events.Key) -> None:
        self.query_one(TextLog).clear()
        if event.key == "enter":
            self.query_one(TextLog).refresh
            ask = self.query_one(Input).value
            response = self.mr_bryce.ask(ask)
            self.query_one(TextLog).clear()
            self.query_one(TextLog).write(response)
            self.query_one(Input).value = ""
            self.refresh


# The SubScan class is a widget that has a compose method that returns a ComposeResult. The
# ComposeResult is a generator that yields an Input and a Button
class SubScan(Widget):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Target_Domain", id='target_subdomain')
        yield Button('Scan', id='start_scan', variant='success')

class Ztools(App):
    # The CSS_PATH is the path to the CSS file that is being used to style the app. The BINDINGS is a
    # list of tuples that contain the key that is being pressed, the function that is being called,
    # and the description of the function.
    CSS_PATH = "styles.css"
    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode")]

    def compose(self) -> ComposeResult:
        """
        The compose function is a generator that yields the Header, Footer, and Container components
        """
        # we create the main areas of the app
        yield Header()
        yield Footer()
        # yield Container(Banner(), Tools(), Wiki())
        yield Container(Banner(), Wiki())

    def action_toggle_dark(self) -> None:
        """
        It toggles the dark mode on and off.
        """
        self.dark = not self.dark


# we start our app main loop
if __name__ == "__main__":
    app = Ztools()
    app.run()
