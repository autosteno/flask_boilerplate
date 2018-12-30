import enum


class SupportedServices(enum.Enum):
    TranscriptionService = 'transcription'


class SupportedVendors(enum.Enum):
    Amazon = 'aws'
    Ibm = 'ibm'
