import psycopg2

class Db():

    def __init__(self, setting):
        self.setting = setting

    def getDia(self, code):

        connect = psycopg2.connect(self.setting.database_url)
        cursor = connect.cursor()

        sqlCode = '%{}%'.format(code.upper())

        cursor.execute("select mkb_code, mkb_name from mkb_bot.mkb_10 mkb where mkb.mkb_code like '{}'".format(sqlCode))

        dia_list = cursor.fetchmany(10)

        res = ''
        for dia in dia_list:
            res += '{} {}\n'.format(dia[0], dia[1])

        connect.close()

        if res == '':
            res = 'Записи для кода "{}" не найдены.'.format(code)

        return res

