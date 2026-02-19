import traceback
from pycti import OpenCTIConnectorHelper
from config import MainConfig
from connector import Connector

if __name__ == "__main__":
    try:
        config = MainConfig()
        config_instance = config.load
        # Convert the config into a dictionary, automatically excluding any parameters set to `None`.
        config_dict = config_instance.model_dump(exclude_none=True)
        helper = OpenCTIConnectorHelper(config=config_dict)
        connector = Connector(config_instance, helper)
        connector.run()
    except Exception:
        traceback.print_exc()
        exit(1)
