import mysql.connector
import csv


class MySqlConnection:
    def __init__(self, conf):
        self.conf = conf

    def connect(self):
        print("try connect")
        self.cnx = mysql.connector.connect(user=self.conf["user"],
                                           password=self.conf["password"],
                                           host=self.conf["host"],
                                           database=self.conf["database"],
                                           )
        print("connect success")

    def get_tables(self):
        print('get tables')
        cursor = self.cnx.cursor()
        cursor.execute("SELECT TABLE_NAME FROM information_schema.tables where TABLE_SCHEMA = %s;",
                       [self.conf["database"]])
        result = cursor.fetchall()
        ret = [];
        for x in result:
            print('table "' + x[0] + '"')
            ret.append(x[0])
        print('get tables finished')
        return ret

    def save(self, name):
        with open(name + '.csv', mode='w', newline='') as employee_file:
            csv_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            cursor = self.cnx.cursor()
            cursor.execute("SELECT * FROM "+name+";")
            csv_writer.writerow([i[0] for i in cursor.description])
            for row in cursor:
                csv_writer.writerow(row)

    def close(self):
        self.cnx.close()
