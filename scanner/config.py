from scanner.utils import load_config

config = load_config()

MAX_THREADS = int(config["performance"]["MAX_THREADS"])

DEFAULT_PORT_RANGE_LOW = int(config["input"]["DEFAULT_PORT_RANGE_LOW"])
DEFAULT_PORT_RANGE_HIGH = int(config["input"]["DEFAULT_PORT_RANGE_HIGH"])
MAX_PORT_RANGE_HIGH = int(config["input"]["MAX_PORT_RANGE_HIGH"])
DEFAULT_OUTPUT_FILENAME = config["input"]["DEFAULT_OUTPUT_FILENAME"]