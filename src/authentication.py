class Authentication:
    def __init__(self, discord = '',weather = ''):
        self.discord = discord
        self.weather = weather
    def DiscordToken(self):
        self.discord = 'MjQwNjQxNDIzNTAwNzcxMzI4.C8vUtg.i3Jp8L4De4rHhe0hNt7loyuSQLY'
        return self.discord

    def WeatherToken(self):
        self.weather = 'fed7544efb617d625f4f6f3b340b4701'
        return self.weather
