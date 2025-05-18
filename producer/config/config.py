import yaml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "../config.yml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

config = load_config()
