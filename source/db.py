import psycopg2

class Db():

    def __init__(self, setting):
        self.setting = setting

    def get_dia_by_code(self, code):
        connect = psycopg2.connect(self.setting.database_url)
        cursor = connect.cursor()

        sqlCode = '%{}%'.format(code.replace("'", "").upper())

        cursor.execute("select mkb_code, mkb_name from mkb_bot.mkb_10 mkb where mkb.mkb_code like '{}'".format(sqlCode))

        dia_list = cursor.fetchmany(10)

        res = ''
        for dia in dia_list:
            res += '{} {}\n'.format(dia[0], dia[1])

        connect.close()

        if res == '':
            res = 'Записи для кода "{}" не найдены.'.format(code)

        return res


    def get_dia_by_name(self, name):
        connect = psycopg2.connect(self.setting.database_url)
        cursor = connect.cursor()

        sqlCode = '%{}%'.format(name.replace("'", "").lower())

        cursor.execute("select mkb_code, mkb_name from mkb_bot.mkb_10 mkb where lower(mkb.mkb_name) like '{}'".format(sqlCode))

        dia_list = cursor.fetchmany(10)

        res = ''
        for dia in dia_list:
            res += '{} {}\n'.format(dia[0], dia[1])

        connect.close()

        if res == '':
            res = 'Записи для строки "{}" не найдены.'.format(name)

        return res

    @staticmethod
    def is_code(find_str):
        for c in find_str.lower():
            if not (c.isalpha() or c == ' '):
                return True
        return False

    def getDia(self, find_str):
        if self.is_code(find_str):
            return self.get_dia_by_code(find_str)
        else:
            return self.get_dia_by_name(find_str)




if __name__ == '__main__':
    print(Db.is_code('ава'))