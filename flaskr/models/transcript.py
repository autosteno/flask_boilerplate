from typing import List
from flask import current_app as app
from functools import reduce


class Speaker(object):
    """
    A speaker for steno is a person in meeting.
    """
    def __init__(self):
        # identifier for speaker.
        self.id: str = None
        # name of speaker.
        self.name: str = None
        # phone number of speaker.
        self.number: str = None

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'number': self.number
        }

    def __str__(self):
        return self.name or self.id


class Sentence(object):
    """
    A sentence spoken by speaker.
    """
    def __init__(self):
        # sentence that has been spoken.
        self.text: str = None
        # time when sentence has been spoken
        self.moment = None
        # speaker of sentence.
        self.speaker: Speaker = None

    def to_dict(self):
        return {
            'text': self.text,
            'moment': self.moment,
            'speaker': self.speaker.to_dict()
        }

    def __str__(self):
        return '[{}] {}: {}'.format(self.moment, self.speaker, self.text)


class Transcript(object):
    """
    A transcript model which is textual form of audio file.
    """

    def __init__(self):
        self.audio_file = None
        # collection of sentences extracted from audio file.
        self.sentences: List[Sentence] = []

    def to_dict(self):
        app.logger.info(str(self))
        return {'sentences': [sentence.to_dict() for sentence in self.sentences]}

    def __str__(self):
        return reduce(lambda x, y: '\n{}\n{}'.format(x, y),
                      [str(s) for s in self.sentences])
