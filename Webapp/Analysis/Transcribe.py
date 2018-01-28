import argparse
import io
import os
import http.client, urllib
import json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/aimihat/Desktop/ICHack 2018/Webapp/Analysis/ichack-6ab4dc2acced.json"
textSentimentKey = '3d885902d9734c0c9a6dd80f87469ca8'

from pydub import AudioSegment


def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        language_code='en-UK')

    response = client.recognize(config, audio)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    text = ""
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        part = (result.alternatives[0].transcript)
        print('Transcript: '+part)
        text = text+ part
    return text

def transcribe_streaming(stream_file):
    """Streams transcription of the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    with io.open(stream_file, 'rb') as audio_file:
        content = audio_file.read()

    # In practice, stream should be a generator yielding chunks of audio data.
    stream = [content]
    requests = (types.StreamingRecognizeRequest(audio_content=chunk)
                for chunk in stream)

    config = types.RecognitionConfig(
        language_code='en-IE')
    streaming_config = types.StreamingRecognitionConfig(config=config)

    # streaming_recognize returns a generator.
    responses = client.streaming_recognize(streaming_config, requests)

    for response in responses:
        # Once the transcription has settled, the first result will contain the
        # is_final result. The other results will be for subsequent portions of
        # the audio.
        for result in response.results:
            print('Finished: {}'.format(result.is_final))
            print('Stability: {}'.format(result.stability))
            alternatives = result.alternatives
            # The alternatives are ordered from most likely to least.
            for alternative in alternatives:
                print('Confidence: {}'.format(alternative.confidence))
                print('Transcript: {}'.format(alternative.transcript))

def GetSentiment (documents):
        "Gets the sentiments for a set of documents and returns the information."
        # API for text sentiment analysis
        uri = 'westcentralus.api.cognitive.microsoft.com'
        path = '/text/analytics/v2.0/sentiment'

        headers = {'Ocp-Apim-Subscription-Key': textSentimentKey}
        conn = http.client.HTTPSConnection (uri)
        body = json.dumps (documents)
        conn.request ("POST", path, body, headers)
        response = conn.getresponse ()
        return response.read ()

def getText(filePath):
    sound = AudioSegment.from_wav(filePath)
    sound = sound.set_channels(1)
    sound.export(filePath, format="wav")
    transcript = transcribe_file(filePath)
    print(transcript)


    documents = { 'documents': [
        #{ 'id': '1', 'language': 'en', 'text': transcript },
        { 'id': '1', 'language': 'en', 'text': transcript }
    ]}

    result = GetSentiment (documents)
    score = json.loads(result)["documents"][0]["score"]
    print (score)
    return [transcript, score]
