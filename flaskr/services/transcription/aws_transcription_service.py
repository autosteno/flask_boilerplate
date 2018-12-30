from .contract import TranscriptionContract
from ...models.transcript import Transcript


class AwsTranscriptionService(TranscriptionContract):

    def transcribe(self, audio_file) -> Transcript:
        # ========= PREPARE MOCK RESULT ===========
        mock_transcript = Transcript()
        from ...models.transcript import Sentence, Speaker
        import datetime
        sentence = Sentence()
        sentence2 = Sentence()
        speaker = Speaker()
        speaker.id = '1221'
        speaker.name = 'Mock user'
        speaker.number = '995310xyz1'

        sentence.text = 'Hey !! Howdy... This is me.... Yeah me..'
        sentence.moment = datetime.datetime.utcnow()
        sentence.speaker = speaker

        sentence2.text = 'Wohoho'
        sentence2.moment = datetime.datetime.utcnow()
        sentence2.speaker = speaker

        mock_transcript.sentences.append(sentence)
        mock_transcript.sentences.append(sentence2)
        # ========= END OF PREPARATION BLOCK ===========
        return mock_transcript
