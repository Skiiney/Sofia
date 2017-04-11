class Authentication:
    def __init__(self, discord = '',weather = '',cat=''):
        self.discord = discord
        self.weather = weather
        self.cat = cat
    def DiscordToken(self):
        self.discord = 'MjQwNjQxNDIzNTAwNzcxMzI4.C8vUtg.i3Jp8L4De4rHhe0hNt7loyuSQLY'
        return self.discord
    def WeatherToken(self):
        self.weather = 'fed7544efb617d625f4f6f3b340b4701'
        return self.weather
    def catToken(self):
        self.cat = 'MTc1NDI5'
        return self.cat
