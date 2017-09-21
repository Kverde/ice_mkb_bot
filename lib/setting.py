import configparser
import os


class Setting():

    def __init__(self, app_path, app_id):
        self.app_path = app_path
        self.data_path = os.path.join(app_path, 'data')

        self.telegram_token = self.loadSetting(app_id, 'TELEGRAM_TOKEN')
        self.botan_token = self.loadSetting(app_id, 'BOTAN_TOKEN')
        self.database_url = self.loadSetting(app_id, 'DATABASE_URL')

    def loadSetting(self, app_id, setting_name):
        token = os.getenv(setting_name)
        if not token is None:
            return token

        setting_file_name = os.path.join(self.app_path, '.env')

        if not os.path.exists(setting_file_name):
            raise Exception('Setting file {} not found'.format(setting_file_name))

        config = configparser.ConfigParser()
        config.read(setting_file_name)

        res = config['main'][setting_name]

        return res.strip()


