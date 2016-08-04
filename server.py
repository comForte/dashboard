#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
          self.send_response(200)
          self.send_header('Content-Type', 'application/json')
          self.end_headers()
          self.wfile.write(get_data())
          return
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

import random
import os
import subprocess
fn = "npns01.ztc1log.txt"

from datetime import datetime
import calendar

def utc_now():
  return calendar.timegm(datetime.utcnow().utctimetuple())

def json_for(field, id, value):
  json = '{{"data": {{"{}":{}, "id":"{}", '
  json += '"updatedAt":{} }}}}'
  return json.format(field, value, id, utc_now())

def get_data():
  count = random.randint(0, lines/3)
  pos = random.randint(0, lines - count)
  cmd = "tail -{} {} | head -{} | grep successful | wc -l"
  c = subprocess.check_output(cmd.format(pos, fn, count), shell=True).split()[0]
  r =  "[" + json_for("value", "ssh-sessions", int(c) + random.randint(5, 10))
  r += "," + json_for("current", "puts", random.randint(1, 5)) +  "]"
  return r
  
with open(fn) as f: lines = sum(1 for _ in f)

Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)

server.serve_forever()
