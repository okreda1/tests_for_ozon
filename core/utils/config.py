import configparser
import os
config = dict()

config_parser = configparser.ConfigParser()


def set_value(section, field, default=None):
    if section in config_parser and field in config_parser[section]:
        config[section].update({field: config_parser[section][field]})
    env_var = os.environ.get(field.upper(), None)
    if env_var:
        # for docker env file, params are string
        if env_var.upper() == "TRUE":
            env_var = True
        elif env_var.upper() == "FALSE":
            env_var = False
        config[section].update({field: env_var})
    else:
        config[section].update({field: default})


config.update({'dev': {}})
os.environ["JSONPLACEHOLDER_HOST"] = 'https://jsonplaceholder.typicode.com'
set_value('dev', 'JSONPLACEHOLDER_HOST', os.environ.get('JSONPLACEHOLDER_HOST'))
