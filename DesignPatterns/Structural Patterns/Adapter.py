# Adaptee  {existing interface}
class FrenchSpeaker:
    def speak_french(self, message):
        print(f"{message} in French")

# Target Interface
class EnglishSpeaker:
    def speak_english(self, message):
        pass

# Adapter
class Translator(EnglishSpeaker):
    def __init__(self, french_speaker):
        self.french_speaker = french_speaker

    def speak_english(self, message):
        french_message = self._translate_to_french(message)
        self.french_speaker.speak_french(french_message)

    def _translate_to_french(self, message):
        return message.replace("Hello", "Bonjour").replace("Thank you", "Merci")


# Client
class EnglishClient:
    def __init__(self, speaker):
        self.speaker = speaker

    def express(self, message):
        self.speaker.speak_english(message)


# Usage
french_speaker = FrenchSpeaker()
translator = Translator(french_speaker)
english_client = EnglishClient(translator)

# The English client speaks English but the French speaker receives the message in French
english_client.express("Hello! Thank you for the meeting")


# Bonjour! Merci for the meeting in French