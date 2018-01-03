from base_settings import BaseSettings

class Setting(BaseSettings):

    def __init__(self, settings_dir, settings_file_name = '.env'):
        super(Setting, self).__init__(settings_dir, settings_file_name)

        self.telegram_token = self.loadSetting('TELEGRAM_TOKEN')
        self.botan_token = self.loadSetting('BOTAN_TOKEN')
        self.database_url = self.loadSetting('DATABASE_URL')




