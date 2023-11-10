# Press Shift+F10 to execute it or replace it with your code.

import yaml
from mysql.connector import errors

from src.mySqlConnection import MySqlConnection
from ui import App, err_msg


def load_conf(config_file_name) -> map:
    print(f'Load config {config_file_name}')  # Press Ctrl+F8 to toggle the breakpoint.
    with open(config_file_name, "r") as configFile:
        return yaml.load(configFile.read(), Loader=yaml.Loader)


def err_handing(msg, ret, ex):
    print(msg)
    print(ex)
    err_msg(msg)
    exit(ret)


if __name__ == '__main__':
    """
    mysql-ből táblákat exportál csv-vé
    """
    try:
        config: map = load_conf("conf.yml")
    except FileNotFoundError as err:
        err_handing("Can not open config file.", 1, err)

    con: MySqlConnection = MySqlConnection(config)
    try:
        con.connect()
    except errors.Error as err:
        err_handing("Can not open database.", 2, err)

    try:
        tables: list[str] = con.get_tables()
    except errors.Error as err:
        err_handing("Can not list tables.", 3, err)
        con.close()

    try:
        app = App()
        selectedTables = app.select_tables(tables)
        if selectedTables is not None:
            for table in selectedTables:
                print(table)
                con.save(table)

    except errors.Error as err:
        err_handing("Can not export tables.", 4, err)
    finally:
        con.close()
    exit(0)
