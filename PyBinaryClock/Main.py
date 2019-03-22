__author__ = 'teddycool'

from MainLoop import MainLoop
import sys
import time
import os


class Main(object):

    def __init__(self):
        print "Init Main object..."
        self._mainloop =  MainLoop()


    def run(self):
        self._mainloop.initialize()
        running=True
        frames = 0
        print "BinaryClock Main starts running..."
        while running:
            try:
                self._mainloop.update()
            except(KeyboardInterrupt):
                running = False
                del(self._mainloop)
                print "User aborted..."
            except (Exception):
                running = False
                del (self._mainloop)
                e = sys.exc_info()
                t = time
                n = time.ctime()[11:13] + time.ctime()[14:16]
                s = str(n).rjust(4)
                f = file(time.asctime()+".log", 'w')
                for l in e:
                    f.write(str(l))
                #os.system('sudo halt')


if __name__ == "__main__":
    print 'Started from: Main.py,  if __name__ == "__main__" '
    gl=Main()
    gl.run()


#Put this in  /etc/rc.local for autostart at boot:
#cd /home/pi/PyBinaryClock
#sudo python Main.py &