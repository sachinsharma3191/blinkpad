import configparser


def read_config():
    config = configparser.ConfigParser()
    config.read("app.ini")
    return config
