import configparser                             # import configparser used to parse together the system constants from settings.cfg file information      
from pathlib import Path                        # from built in library pathlib import to join config.py back to setting.cfg

# Load settings.cfg
config = configparser.ConfigParser()            # assign config to the Class ConfigParser() in configparser built in library
config.read("settings.cfg")                     # config read source settings information

# Project paths
DATA_DIR = Path(config["paths"]["data_dir"])                
DATA_INTERNAL = Path(config["paths"]["bank_info"])      
DATA_INTERNAL = Path(config["paths"]["customer_info"])    
LOGGING = Path(config["logging"]["logging"])
        
# Logging
DEBUG = config.getboolean("logging", "debug")              # create univeral constant for DEBUG with path via config.py back to settings.cfg with bool set to true

# Process defaults
DEFAULT_DEMAND_INCREASE = float(config["process"]["default_demand_increase"])   
DEFAULT_CURRENCY = f"${float(.00)}"