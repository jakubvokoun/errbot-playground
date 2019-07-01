from errbot import BotPlugin, botcmd


class Ping(BotPlugin):
    """
    This plugin implements ping command

    """

    @botcmd  # flags a command
    def ping(self, msg, args):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        """
        return '`pong`'

