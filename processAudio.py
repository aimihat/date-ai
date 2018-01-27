import subprocess
import httplib, urllib, base64
import json

# command = "ffmpeg -i Dump/m1.mov -ab 160k -ac 2 -ar 44100 -vn audio.wav"
#
# subprocess.call(command, shell=True)
#
headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'audio/wav; codec=audio/pcm; samplerate=16000',
    'Ocp-Apim-Subscription-Key': '8becfa4edfe1488fbdfa3718872b1226',
    'Transfer-Encoding' :'chunked'
}

params = urllib.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
body = "{ 'file': audio.wav' }"
with open(filename, 'rb') as fd:
    contents = fd.read()

try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
    #   URL below with "westcentralus".
    conn = httplib.HTTPSConnection('speech.platform.bing.com/speech/recognition/interactive/cognitiveservices/v1?language=en-us&format=detailed')
    conn.request("POST", "/sts/v1.0" , body, headers)
    response = conn.getresponse()
    data = response.read()
    print data
    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    conn.close()
except Exception as e:
    print e
