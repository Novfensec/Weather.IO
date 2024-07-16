# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.home_screen import HomeScreenModel
from Controller.home_screen import HomeScreenController
from Model.weather_profiles_screen import WeatherProfilesScreenModel
from Controller.weather_profiles_screen import WeatherProfilesScreenController
from Model.settings_screen import SettingsScreenModel
from Controller.settings_screen import SettingsScreenController

screens = {
    'home screen': {
        'model': HomeScreenModel,
        'controller': HomeScreenController,
    },
    'weather profiles screen': {
        'model': WeatherProfilesScreenModel,
        'controller': WeatherProfilesScreenController,
    },
    'settings screen': {
        'model': SettingsScreenModel,
        'controller': SettingsScreenController,
    },
}