from View.base_screen import BaseScreenView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineIconListItem
from kivy.clock import Clock
from kivymd.uix.button import MDFillRoundFlatIconButton
from .components.weather_api_data import get_weather
from kivymd.uix.menu import MDDropdownMenu

class DisplayContentData(MDBoxLayout):
    pass

class ExtendedButton(MDFillRoundFlatIconButton, CommonElevationBehavior):
    '''
    Implements a button of type
    `Extended FAB <https://m3.material.io/components/extended-fab/overview>`_.

    .. rubric::
        Extended FABs help people take primary actions.
        They're wider than FABs to accommodate a text label and larger target
        area.

    This type of buttons is not yet implemented in the standard widget set
    of the KivyMD library, so we will implement it ourselves in this class.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.padding = "16dp"
        Clock.schedule_once(self.set_spacing)
        menu_items = [
                {
                    "viewclass": "Item",
                    "icon":'weather-cloudy',
                    "text": "Sydney",
                    "on_release":lambda : self.get_data(city="Sydney"),
                 },
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4.5,
            max_height=750,
        )
        
    def set_spacing(self, interval):
        self.ids.box.spacing = "12dp"

    def set_radius(self, *args):
        if self.rounded_button:
            self._radius = self.radius = self.height / 4
        
    def dropdownmenucallback(self,instance_action):
        self.menu.caller = instance_action
        self.menu.open()
    
    def get_data(self,city="Delhi"):
        data=get_weather(city)
        print(data["location"])
        self.menu.dismiss()
    
class Item(OneLineIconListItem):
    divider = None
    icon = StringProperty()

class HomeScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """