import httplib
conn = httplib.HTTPConnection("http://34.66.7.201:8080/job/microservice-environments-set/parambuild?token=123456&NAME=test-micro&ENV=test-env&NS=testnamespace")
conn.request("HEAD","/index.html")
res = conn.getresponse()
print res.status, res.reason
