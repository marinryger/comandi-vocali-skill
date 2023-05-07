from mycroft import MycroftSkill, intent_file_handler


class ComandiVocali(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('vocali.comandi.intent')
    def handle_vocali_comandi(self, message):
        self.speak_dialog('vocali.comandi')


def create_skill():
    return ComandiVocali()

