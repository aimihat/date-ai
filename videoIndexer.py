########### Python 2.7 #############
import httplib, urllib, base64
import json

headers = {
    # Request headers
    'Content-Type': 'multipart/form-data',
    'Ocp-Apim-Subscription-Key': '8594b86ba540422ab37146cebfae65b5',
}

params = urllib.urlencode({
    'language': 'English',
    # Request parameters
})

try:
    filename = 'Dump/m3.mov'
    f = open(filename, "rb")
    chunk = f.read()
    f.close()

    conn = httplib.HTTPSConnection('videobreakdown.azure-api.net')
    conn.request("POST", "/Breakdowns/Api/Partner/Breakdowns?name=v.mp4&privacy=Private&%s" % params, chunk, headers)
    #conn.request("GET", "/Breakdowns/Api/Partner/Breakdowns/{id}?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    #print("[Errno {0}] {1}".format(e.errno, e.strerror))
    print(e)
