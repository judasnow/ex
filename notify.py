from foo.handlers.base import BaseHandler 
import tornado.web 
import tornado.httpclient 
import urllib 
import xml.dom.minidom 
from cStringIO import StringIO 

import mimetypes 

"adapted from: http://code.activestate.com/recipes/146306/" 
def encode_multipart_formdata(fields, files): 
    """ 
    fields is a sequence of (name, value) elements for regular form 
fields. 
    files is a sequence of (name, filename, value) elements for data 
to be uploaded as files 
    Return (content_type, body) ready for httplib.HTTP instance 
    """ 
    BOUNDARY = '-------tHISiStheMulTIFoRMbOUNDaRY' 
    CRLF = '\r\n' 
    L = [] 
    for (key, value) in fields: 
        L.append('--' + BOUNDARY) 
        L.append('Content-Disposition: form-data; name="%s"' % key) 
        L.append('') 
        L.append(value) 
    for (key, filename, value) in files: 
        L.append('--' + BOUNDARY) 
        L.append('Content-Disposition: form-data; name="%s"; 
filename="%s"' % (key, filename)) 
        L.append('Content-Type: %s' % get_content_type(filename)) 
        L.append('') 
        L.append(value) 
    L.append('--' + BOUNDARY + '--') 
    L.append('') 
    b = StringIO() 
    for l in L: 
        b.write(l) 
        b.write(CRLF) 
    body = b.getvalue() 
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY 
    return content_type, body 

def get_content_type(filename): 
    return mimetypes.guess_type(filename)[0] or 'application/octet- 
stream' 

class TwitPicHandler(BaseHandler): 

    post_url = "http://twitpic.com/api/uploadAndPost" 
    upload_url = "http://twitpic.com/api/upload" 

    @tornado.web.authenticated 
    def get(self): 
        self.context['title'] = "Upload image" 
        self.render('twitpic.html', **self.context) 

    @tornado.web.authenticated 
    @tornado.web.asynchronous 
    def post(self): 
        if self.get_argument('tweet', False): 
            url = self.post_url 
        else: 
            url = self.upload_url 
        p = [] 
        p.append(('username',self.u['username'])) 
        p.append(('password',self.u['password'])) 
        if self.get_argument('tweet',False): 
            p.append(('message',self.get_argument('message'))) 
        f = self.request.files['media'][0] 
        f =  ('media',f['filename'].encode('utf-8'),f['body']) 
        content_type, body = encode_multipart_formdata([(k,v.encode 
('utf-8')) for k,v in p], [f]) 
        http = tornado.httpclient.AsyncHTTPClient() 
        headers = {'Content-Type':content_type} 
        req = tornado.httpclient.HTTPRequest(url=url, 
                                             method="POST", 
                                             body=body, 
                                             headers=headers) 
        http.fetch(req,callback=self.async_callback(self.on_response)) 

    def on_response(self, response): 
        if response.body: 
            if 'stat="ok"' in response.body: 
                self.set_secure_cookie('err_message',"Pic posted ok") 
            else: 
                self.set_secure_cookie('err_message',"Error posting 
pic %s" % response.body) 
        else: 
            self.set_secure_cookie('err_message',"Error posting pic %s 
- check to see if it has been posted, sometimes we get weird 
errors. :)" % response.body) 
        self.redirect('/home') 
