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
import json

def utc_now():
  return calendar.timegm(datetime.utcnow().utctimetuple())

def dict_for(id, field, value):
  return {
    'data': {
      'id': id,
      field: value,
      'updatedAt': utc_now(),
    }
  }

def get_data():
  count = random.randint(0, lines/3)
  pos = random.randint(0, lines - count)
  cmd = "tail -{} {} | head -{} | grep successful | wc -l"
  c = subprocess.check_output(cmd.format(pos, fn, count), shell=True).split()[0]
  return json.dumps([
      dict_for("ssh-sessions", "value", int(c) + random.randint(5, 10)),
      dict_for("puts", "current", random.randint(1, 5)),
      dict_for("remote-ip-addresses", "points", 
      [{"x": _, "y": random.randint(0, 50)} for _ in range (10)])])
  
with open(fn) as f: lines = sum(1 for _ in f)

Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)

server.serve_forever()
