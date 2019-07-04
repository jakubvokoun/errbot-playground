from errbot import BotPlugin, botcmd, botmatch
import namegenerator
import re


class RestorePlugin(BotPlugin):
    @botcmd
    def restore(self, msg, _):
        return "Ktery den chcete pouzit? [YYYY-MM-DD]"

    @botmatch(r'^(\d{4}-\d{2}-\d{2})|(yesterday)$', flags=re.IGNORECASE, low_only=True)
    def set_date(self, msg, match):
        msg.ctx['date'] = match.string
        default_name = namegenerator.gen()
        msg.ctx['name'] = default_name
        return "Jak se ma backup jmenovat? Muze se jmenovat '{}'? [Y|y|backup-name]"\
            .format(default_name)

    @botmatch(r'^[a-z0-9-_]+$', flags=re.IGNORECASE, flow_only=True)
    def set_name(self, msg, match):
        if match.string.lower() == 'y':
            backup_name = msg.ctx['name']
        else:
            msg.ctx['name'] = match.string
            backup_name = match.string
        return "Rekapitulace: datum: {d[date]}, nazev: {d[name]}. V poradku? [Y|y]"\
            .format(d=msg.ctx)

    @botmatch(r'^y$', flags=re.IGNORECASE, flow_only=True)
    def final(self, msg, match):
        return "OK"

