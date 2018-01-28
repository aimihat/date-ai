import requests, json
text="what's your name"
r='http://www.cleverbot.com/getreply'
d = {'key':'CC6wwsZu_c50FJ9mMPyRjXHbl7Q','input':text}
r = requests.get(r,d).text
json.loads(r)['output']