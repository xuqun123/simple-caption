from video_player import VideoPlayerApp

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class SimpleCaptionApp(App):

    def build(self):
        root = Builder.load_file('layout.kv')
        Window.add_widget(root)

if __name__ == '__main__':
    SimpleCaptionApp().run()
