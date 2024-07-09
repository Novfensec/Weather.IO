from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton

from Utility.observer import Observer

class StyledIconButton(MDIconButton):
    def __init__(self, *args,**kwargs):
        super(StyledIconButton, self).__init__(*args,**kwargs)

class CustomLabel(MDLabel):
    def __init__(self, *args,**kwargs):
        super(CustomLabel, self).__init__(*args,**kwargs)
        self.app=MDApp.get_running_app()
        self.bold=False
        self.font_size="21sp"
        self.font_name=self.app.basic_font
        # if self.bold==True:
        #     self.font_name=self.app.basic_font
        # else:
        #     self.font_name=self.app.basic_bold_font

class BaseScreenView(ThemableBehavior, MDScreen, Observer):
    """
    A base class that implements a visual representation of the model data.
    The view class must be inherited from this class.
    """

    controller = ObjectProperty()
    """
    Controller object - :class:`~Controller.controller_screen.ClassScreenControler`.

    :attr:`controller` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    model = ObjectProperty()
    """
    Model object - :class:`~Model.model_screen.ClassScreenModel`.

    :attr:`model` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    manager_screens = ObjectProperty()
    """
    Screen manager object - :class:`~kivymd.uix.screenmanager.MDScreenManager`.

    :attr:`manager_screens` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kw):
        super().__init__(**kw)
        # Often you need to get access to the application object from the view
        # class. You can do this using this attribute.
        self.app = MDApp.get_running_app()
        # Adding a view class as observer.
        self.model.add_observer(self)
