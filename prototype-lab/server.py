from http.server import SimpleHTTPRequestHandler,HTTPServer
class H(SimpleHTTPRequestHandler):
 def do_GET(self):
  if self.path.split('?')[0] in ['/', '/concept-one','/concept-two','/concept-three','/comparison']:
   self.path='/index.html'
  return super().do_GET()
HTTPServer(('127.0.0.1',5173),H).serve_forever()
