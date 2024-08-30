from View.base_screen import BaseScreenView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty

class WeatherCard(MDBoxLayout):
    text=StringProperty()
    data=ObjectProperty()
    
class WeatherCardGrid(MDGridLayout):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

class WeatherProfilesScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
