#!/usr/bin/env python

import sys
import os
import urlparse
import subprocess
from SimpleHTTPServer import SimpleHTTPRequestHandler
from SocketServer import TCPServer

CONVERT = "c:/imagemagick/convert"

def undistort(image_data, params, newfilename):
  args = '%s - -matte -virtual-pixel transparent -distort Perspective "%s" %s' % (CONVERT, params, newfilename)
  p = subprocess.Popen(args, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
  p.communicate(input=image_data)

def main():
  if len(sys.argv) < 3:
    print "undistort_gui by Grom PE"
    print "- run web browser with correction interface,"
    print "- then use imagemagick to create fixed image"
    print "Usage: undistort_gui.py <image_filename> <output_filename>"
    exit()
  filename = sys.argv[1]
  newfilename = sys.argv[2]
  data = ""
  try:
    f = open(filename, "rb")
    data = f.read()
    f.close()
  except Exception, e:
    print "Can't read file: %s" % filename
    exit()
  the_image = data
  global stopped_server
  stopped_server = False
  f = open("index.html", "rb")
  main_page_html = f.read()
  f.close()

  def stop_server():
    global stopped_server
    stopped_server = True

  class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
      try:
        parsed = urlparse.urlparse(self.path)
        query = urlparse.parse_qs(parsed.query)
        path = parsed.path
        if path == '/':
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          self.wfile.write(main_page_html)

        elif path == '/image':
          self.send_response(200)
          self.send_header('Content-type', 'image/png')
          self.end_headers()
          self.wfile.write(the_image)

        elif path == '/doit':
          params = query["p"][0]
          undistort(the_image, params, newfilename)
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          self.wfile.write("Done!")
          stop_server()

        else:
          self.send_response(404)
          self.end_headers()
          self.wfile.write("404 Not Found")
      except Exception, e:
        self.send_response(500)
        self.end_headers()
        self.wfile.write("500 Internal Server Error")
        raise


  httpd = TCPServer(('127.0.0.1', 8000), Handler)
  os.startfile("http://127.0.0.1:8000/")
  while not stopped_server:
    httpd.handle_request()

if __name__ == "__main__":
  main()
