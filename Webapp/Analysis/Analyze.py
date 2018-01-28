#DIR = "../sessions/100/";

import urllib, base64
import json
from Analysis import ImageEmotion, Transcribe
import numpy as np

import os


def processFrame(DIR, fileName):
	if(fileName.find(".png")==-1):
		print("Can not process frame "+fileName)
		return;
	# Scores are for (anger, contempt, disgust, fear, happiness, neutral, sadness, surprise)
	scores = ImageEmotion.emotionAPI(DIR + fileName);
	if(scores is None or  len(scores)>0):
		with open(DIR + "results_image.csv", "a") as myfile:
			myfile.write(str(scores[0]));
			for score in scores:
				myfile.write("," + str(score));
			myfile.write('\n')
			myfile.close()

def resetDirectory(DIR):
	os.remove(DIR + "results.csv")

def speechToText(DIR, fileName):
	if(fileName.find(".wav")==-1):
		print("Can not process file "+fileName)
		return;
	[text, score] = Transcribe.getText(DIR + fileName)
	with open(DIR + "results_speech.csv", "a") as myfile:
		myfile.write(str(score)+"\n");
	return text


#processFrame(DIR, "36.png")
#speechToText(DIR, "audio_1.wav")

# resetDirectory(DIR)
# for i in range(len(arr)):
# 	allScores = [];
# 	if(arr[i].find('png')!=-1):
# 		# Scores are for (anger, contempt, disgust, fear, happiness, neutral, sadness, surprise)
# 		processFrame(DIR, arr[i])