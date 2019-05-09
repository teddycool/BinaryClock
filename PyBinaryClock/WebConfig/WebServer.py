__author__ = 'teddycool'

import os
import urllib2
import time

import SimpleHTTPServer
import SocketServer

class WebServer(object):

    def __init__(self):
        print "Init WebServer"
        self._port = 8000
        self._handler=SimpleHTTPServer.SimpleHTTPRequestHandler
        self._handler.extensions_map.update({
            '.webapp': 'application/x-web-app-manifest+json',
        });

    def StartServer(self):
        print "Starting webserver, listening to port " + str(self._port)
        self._httpd= SocketServer.TCPServer(("", self._port), self._handler)

if __name__ == '__main__':

    print "Testcode for WebServer"
    web = WebServer()
    web.StartServer()
    while True:
        time.sleep(0.1)