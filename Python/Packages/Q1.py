import http.client
'''Used HTTP package 
inside it used the client module
and below are the 3 functions I used within it'''

conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)





