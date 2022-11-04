import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
from texttospeech2 import *
from intent_calculate import *
load_dotenv()
def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    SUBSCRIPTION_KEY = os.getenv('SPEECH_KEY')
    REGION = os.getenv('SPEECH_REGION')
    speech_config = speechsdk.SpeechConfig(subscription=SUBSCRIPTION_KEY, region=REGION)
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        # check the confidence value of the recognized sppech
        if (calculate_intent(speech_recognition_result.text) > 0.6):
            if(("." in speech_recognition_result.text)):
                pass_speech = speech_recognition_result.text.replace(".","")
            if(("?" in speech_recognition_result.text)):
                pass_speech = speech_recognition_result.text.replace("?","")
            number_list = pass_speech.split(" ")
            plus_position = number_list.index("+")
            answer = int((number_list)[plus_position-1])+int((number_list)[plus_position+1])
            # say the answer
            text_to_speech(str(answer))
        else :
            print("That's not a calculation")
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

recognize_from_microphone()
