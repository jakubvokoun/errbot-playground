from errbot import BotPlugin, arg_botcmd
from errbot.backends.slack import COLORS


class FancyPlugin(BotPlugin):
    @arg_botcmd('color', type=str)
    @arg_botcmd('--title', type=str, default="Title test")
    @arg_botcmd('--body', type=str, default="Body test")
    def color_msg(self, msg, color, title=None, body=None):
        if not color in COLORS:
            self.send_card(title="Unkonwn color",
                           body="Allowed colors are: {}".format(', '.join(COLORS)),
                           color='red',
                           in_reply_to=msg)
        else:
            self.send_card(title=title, body=body, color=color,
                           in_reply_to=msg)
