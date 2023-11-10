# Press Shift+F10 to execute it or replace it with your code.

import yaml
from mysql.connector import errors

from mySqlConnection import MySqlConnection
from ui import App


def load_conf(configFileName):
    print(f'Load config {configFileName}')  # Press Ctrl+F8 to toggle the breakpoint.
    configFile = open(configFileName, "r")
    configFileContent = configFile.read()
    config = yaml.load(configFileContent, Loader=yaml.Loader)
    return config


def errHanding(msg, ret, ex):
    print(msg)
    print(ex)
    app = App()
    err(msg)
    exit(ret)


if __name__ == '__main__':
    """
    mysql-ből táblákat exportál csv-vé
    """
    try:
        config = load_conf("conf.yml")
    except FileNotFoundError as err:
        errHanding("Can not open config file.", 1, err)

    try:
        con = MySqlConnection(config)
        con.connect()
    except errors.Error as err:
        errHanding("Can not open database.", 2, err)

    try:
        tables: list[str] = con.get_tables()
    except errors.Error as err:
        errHanding("Can not list tables.", 3, err)
        con.close()

    try:
        app = App()
        selectedTables = app.select_tables(tables)
        if selectedTables is not None:
            for table in selectedTables:
                print(table)
                con.save(table)

    except errors.Error as err:
        errHanding("Can not export tables.", 4, err)
    finally:
        con.close()
    exit(0)
