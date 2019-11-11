import kivy
import sys
import os

kivy.require('1.2.0')

from sys import argv
from os.path import dirname, join
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer

class VideoPlayerApp(App):

    def build(self):
        if len(argv) > 1:
            filename = argv[1]
        else:
          print('Usage: python %s VIDEO_FILE_PATH' % os.path.basename(sys.argv[0]))
          sys.exit(1)
        return VideoPlayer(source=filename, state='stop')


if __name__ == '__main__':
    VideoPlayerApp().run()
