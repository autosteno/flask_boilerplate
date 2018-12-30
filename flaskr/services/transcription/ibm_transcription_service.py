from .contract import TranscriptionContract
from ...models.transcript import Transcript


class IbmTranscriptionService(TranscriptionContract):

    def transcribe(self, audio_file) -> Transcript:
        return Transcript()
