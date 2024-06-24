from View.base_screen import BaseScreenView
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivymd.uix.button import MDFillRoundFlatIconButton

class BaseNavigationDrawer(MDNavigationDrawer):
    current=StringProperty()

class BaseNavigationLayout(MDBoxLayout):
    pass

class WeatherCard(MDCard,CommonElevationBehavior):
    text=StringProperty()

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

    def set_spacing(self, interval):
        self.ids.box.spacing = "12dp"

    def set_radius(self, *args):
        if self.rounded_button:
            self._radius = self.radius = self.height / 4
        
class HomeScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def navigation_layout_popup(self):
        print("pressed")
