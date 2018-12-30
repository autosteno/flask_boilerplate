from abc import ABC, abstractmethod
from flaskr.models.transcript import Transcript
from ..core.service_contract import ServiceContract


class TranscriptionContract(ServiceContract):

    @abstractmethod
    def transcribe(self, audio_file) -> Transcript:
        pass
