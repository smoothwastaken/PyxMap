import json

class App(object):

    # App variables
    config = {}

    # Initialisation of the app
    def __init__(self) -> None:
        # Load the config file
        self._load_config()

    def _load_config(self) -> None:
        # Load the config file
        with open("config.json", "r") as f:
            self.config = json.load(f)
