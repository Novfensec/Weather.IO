# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.home_screen import HomeScreenModel
from Controller.home_screen import HomeScreenController
from Model.weather_profiles_screen import WeatherProfilesScreenModel
from Controller.weather_profiles_screen import WeatherProfilesScreenController

screens = {
    "home screen": {
        "model": HomeScreenModel,
        "controller": HomeScreenController,
    },

    "weather profiles screen": {
        "model": WeatherProfilesScreenModel,
        "controller": WeatherProfilesScreenController,
    },
}