#! /usr/bin/env python
import SimpleHTTPServer
import SocketServer
import pdb
import time
import re
import collections
import os
import subprocess
import datetime
import json

reporting_time_seconds = 4*7*24*60*60

def dict_for(id, field, value):
  return {
    'data': {
      'id': id,
      field: value,
      'updatedAt': time.time(),
    }
  }

def get_data():
  since_time = time.strftime("%d%b%y", time.localtime(time.time() - 
      reporting_time_seconds))
  subprocess.check_output(("""gtacl -c "\$system.system.showlog """
      """ \$system.zssh.sshlog2 * \\"{} 00:01:00\\"" > /tmp/log """).
      format(since_time), shell=True)
  user_count = int(subprocess.check_output("grep successful /tmp/log | wc -l", 
      shell=True).split()[0])
  log_blob = subprocess.check_output("grep 'password verification successful "  
      "for user' /tmp/log", shell=True)
  # ^password verification successful for user 'username'$
  users = map(lambda v: re.search("'([^']+)'", v).group(1), 
      log_blob.splitlines()) 
  top_users = collections.Counter(users).most_common(5)
  return json.dumps([
    dict_for("ssh-sessions", "value", user_count), 
    dict_for("top-users", "items", 
    [{"label": u[0], "value": u[1]} for u in top_users])
  ])

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def do_GET(self):
    if self.path == '/data':
      self.send_response(200)
      self.send_header('Content-Type', 'application/json')
      self.end_headers()
      self.wfile.write(get_data())
      return
    return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)
server.serve_forever()
