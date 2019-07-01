import requests
from errbot import BotPlugin, botcmd, re_botcmd

CHUCK_URL = 'http://api.icndb.com/jokes/random'


class ChuckNorrisPlugin(BotPlugin):
    def get_joke(self):
        response = requests.get(CHUCK_URL)
        if response.status_code == requests.codes.ok:
            return response.json()['value']['joke']

    def callback_message(self, mess):
        if mess.body.lower().find('chuck norris') != -1:
            self.send(mess.to, self.get_joke())
