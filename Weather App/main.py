from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.card import MDCard
from kivymd.uix.screenmanager import MDScreenManager
from kivy.factory import Factory

Window.size= (300, 735)
Window.top=51
Window.left=1070

class BaseScreen(MDScreen):
    def __init__(self,**kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        
class BaseScreenManager(MDScreenManager):
    def __init__(self,**kwargs):
        super(BaseScreenManager, self).__init__(**kwargs)
        
class HomeScreen(MDScreen):
    def __init__(self,**kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        
class WeatherProfilesScreen(MDScreen):
    def __init__(self,**kwargs):
        super(WeatherProfilesScreen, self).__init__(**kwargs)
        
class UI(Factory.ScreenManager):
    def __init__(self, *args):
        super(UI, self).__init__(*args)

class Weather(MDApp):
    
    def __init__(self,**kwargs):
        super(Weather, self).__init__(**kwargs)
        
    def build(self):
        return UI()

baseapp=Weather()

if __name__=="__main__":
    baseapp.run()