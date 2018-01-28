########### Python 2.7 #############
import http.client, urllib, base64
import json
import numpy as np

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '3ce0e2d17845482c9587c8b4c76ce777',
}

params = urllib.parse.urlencode({
})

def emotionAPI(filePath):
    try:
        # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
        #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
        #   URL below with "westcentralus".
        file = open(filePath, 'rb')
        print("Processing file "+filePath)
        chunk = file.read()
        file.close()

        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, chunk, headers)
        response = conn.getresponse()
        data = response.read()
        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(data)
        # print ("Response:")
        # print(len(parsed))
        if(len(parsed)>0):
            conn.close()
            return np.array([parsed[0]["scores"]["anger"], parsed[0]["scores"]["contempt"], parsed[0]["scores"]["disgust"], parsed[0]["scores"]["fear"],
                            parsed[0]["scores"]["happiness"], parsed[0]["scores"]["neutral"], parsed[0]["scores"]["sadness"], parsed[0]["scores"]["surprise"]])
        else :
            conn.close()
            return np.array([])
    except Exception as e:
        print e
        return np.array([])
