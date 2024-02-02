import configparser


class Config:
    def __init__(self, config_file):
        """
        Initializes a Config object.

        Args:
            config_file (str): The path to the configuration file.

        Returns:
            None
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get(self, section, key):
        """
        Retrieves the value associated with the given key in the specified section.

        Args:
            section (str): The section name in the configuration file.
            key (str): The key whose value needs to be retrieved.

        Returns:
            str: The value associated with the key in the specified section.
        """
        return self.config.get(section, key)
