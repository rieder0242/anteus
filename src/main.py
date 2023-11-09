# Press Shift+F10 to execute it or replace it with your code.

from mySqlConnection import MySqlConnection
from ui import App
import yaml


def load_conf(configFileName):
    print(f'Load config {configFileName}')  # Press Ctrl+F8 to toggle the breakpoint.
    configFile = open(configFileName, "r")
    configFileContent = configFile.read()
    config = yaml.load(configFileContent, Loader=yaml.Loader)
    return config


if __name__ == '__main__':
    """
    mysql-ből táblákat exportál csv-vé
    """
    #
    config = load_conf("conf.yml")
    con = MySqlConnection(config)
    con.connect()
    tables = con.get_tables()
    app = App()
    selectedTables = app.select_tables(tables)

    for table in selectedTables:
        print(table)
        con.save(table)

    con.close()
    exit(0)
