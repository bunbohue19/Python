# Import logging module
import logging

# Build and config the logger
logging.basicConfig(filename = "main.log", 
                    format = "%(asctime)s %(message)s", 
                    filemode = "w")

# set an object for the logger
new_logger = logging.getLogger()

# set threshold to debug
new_logger.setLevel(logging.DEBUG)

# Test Messages for that log
print(new_logger.debug("This is a Harmless debug message"))
print(new_logger.info("Information message"))
print(new_logger.warning("A warning message"))
print(new_logger.error("This is an error message"))
print(new_logger.critical("No Internet, Internet is down now"))

