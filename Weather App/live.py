from kaki.app import App
from kivy.factory import Factory
import os

class Live(App):
    def __init__(self, *args):
        super(Live, self).__init__(*args)
    
    CLASSES={
        "UI":"main"
    }

    KV_FILES={
        os.path.join(os.getcwd(),"app.kv")
    }
    
    AUTORELOADER_PATHS=[
        (".",{"recursive":True}),
    ]
    
    def build_app(self,first=False):
        return Factory.UI()
    
if __name__ == '__main__':
    Live().run()
    