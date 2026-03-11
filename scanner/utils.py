import configparser
import os

required_keys = {
    "performance": ["MAX_THREADS"],
    "input": ["DEFAULT_PORT_RANGE_LOW", "DEFAULT_PORT_RANGE_HIGH"]
}

def load_config(file_path="./config.ini"):
    """Load and validate configuration from a given INI file"""
    if (not os.path.exists(file_path)):
        raise FileNotFoundError(f"Config file '{file_path} not found.")
    
    config = configparser.ConfigParser()
    config.read(file_path)
    
    for section, keys in required_keys.items():
        if (not section in config):
            raise ValueError(f"Config missing section: '{section}'")
        
        for key in keys:
            if (not key in config[section]):
                raise ValueError(f"Config missing key '{key}' in section '{section}'")
        
    return config

