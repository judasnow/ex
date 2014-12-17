from tornado.httpclient import HTTPClient, HTTPError

http_client = HTTPClient()

headers = {'User-Agent': 'Safari/537.36'}

try:
    response = http_client.fetch("http://www.douban.com/group/haixiuzu/", headers=headers)
    print response.body

except HTTPError as e:
    print "Error:", e

http_client.close()


