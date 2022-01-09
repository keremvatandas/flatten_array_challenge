
import os
import configparser

# Project BaseDIR
config_file_path = os.path.abspath(os.path.join("..", os.getcwd()))
print(config_file_path)
config = configparser.ConfigParser()
config.read(f"{config_file_path}/config.ini")

# FASTAPI Settings
PROJECT_NAME: str = config["FASTAPI"].get("PROJECT_NAME", "")
API_PREFIX: str = config["FASTAPI"].get("API_PREFIX", "/api")
API_VERSION: str = config["FASTAPI"].get("API_VERSION", "v.0.1")
DEBUG: bool = True if config["FASTAPI"].get("DEBUG") else False
