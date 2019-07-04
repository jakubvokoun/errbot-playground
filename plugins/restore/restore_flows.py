from errbot import botflow, FlowRoot, BotFlow


class RestoreFlows(BotFlow):
    @botflow
    def restore(self, flow: FlowRoot):
        restore = flow.connect('restore', auto_trigger=True)
        set_date = restore.connect('set_date')
        set_name = set_date.connect('set_name')
        final = set_name.connect('final')

