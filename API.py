import os
import uuid
import speech_recognition as sr
from os import path
from pydub import AudioSegment
import werkzeug
import logging
import utils
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
#import environment as env
import analyzer


# Instance of application
class SoundCount(Resource):

    """
    An instance of the SoundCount app
    POST: receive a WAV file to process.
    file: the file field.
    """

    def post(self):
        logging.info("POST Request received.")

        # assume bad result, create temp file.
        payload = {'status': 'failure',
                   'count': 0,
                   'meta': {}}

        # Parse the request into a dict() which contains the raw wav data.
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()

        # Save the data as a temporary file
        filename = str(uuid.uuid4())

        try:
            audio_file = args['file']
            audio_file.save(filename)
        except AttributeError:
                if audio_file is None:
                    logging.error("Audio data not received")
                    return payload
        #opens the file and it recognize the text and saves it to payload
        try:
            r = sr.Recognizer()
            with sr.AudioFile(filename) as source:
                    audio = r.record(source)  # read the entire audio file
                    payload['meta']['text'] = r.recognize_google(audio)
        except:
            return payload

        """the main problem happens here
        it calculate everthing right from the .wav file but it cant
        get the data that it needs to know if it is a male
        or a female speaking"""
        ana= analyzer.voice_analyzer(filename)
        print(ana)

        #it counts the words
        if 'error' not in payload:
            payload['status'] = 'success'
            payload['count'] += len(payload['meta']['text'].split())
        os.remove(filename)
        return payload


# Create the app and resource (root)
app = Flask(__name__)
api = Api(app)

api.add_resource(SoundCount, '/')


if __name__ == '__main__':
    app.run(debug=False)
