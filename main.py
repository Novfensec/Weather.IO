from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
Window.size=354,589

class HomeScreen(MDScreen):
    pass

class WeatherIO(MDApp):
    def build(self):
        self.kv='''
MDScreen:
    id:screen
    
    HomeScreen:
        id:home_screen                
'''
        self.theme_cls.primary_palette='Gray'
        self.theme_cls.primary_hue='300'
        self.screen=Builder.load_string(self.kv)
        return self.screen
    
    def refresh_callback(self):
        
        def refresh_callback(interval):
            self.screen.ids.home_screen.ids.refresh_layout.refresh_done()
            
        Clock.schedule_once(refresh_callback, 1)
            
        
            

if __name__=="__main__":
    WeatherIO().run()