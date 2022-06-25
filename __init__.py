from mycroft import MycroftSkill, intent_file_handler


class Countdown(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('countdown.intent')
    def handle_countdown(self, message):
        self.speak_dialog('countdown')


def create_skill():
    return Countdown()

