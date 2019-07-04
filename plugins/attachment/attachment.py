from errbot import BotPlugin, botcmd
import datetime
import os


class AttachmentPlugin(BotPlugin):
    # http://errbot.io/en/latest/user_guide/plugin_development/streams.html
    def callback_stream(self, stream):
        self.send(stream.identifier, "File request from :" + str(stream.identifier))
        stream.accept()
        self.send(stream.identifier, "Content:" + str(stream.fsource.read()))

    @botcmd
    def send_file(self, msg, _):
        now = datetime.datetime.now()
        tmp_file = '/tmp/errbot-test.txt'
        with open(tmp_file, 'w+') as fp:
            fp.write('Current time is {}'.format(now.isoformat()))
        stream = self.send_stream_request(msg.frm,
                                          open(tmp_file, 'rb'),
                                          name='test.txt',
                                          stream_type='text/plain')
        return "OK"

    @botcmd
    def send_image(self, msg, _):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        stream = self.send_stream_request(msg.frm,
                                          open(os.path.join(dir_path, 'freebsd-logo.png'), 'rb'),
                                          name='freebsd-logo.png',
                                          stream_type='image/png')
        return "OK"
