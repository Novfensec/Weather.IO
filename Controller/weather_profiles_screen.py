import importlib

import View.WeatherProfilesScreen.weather_profiles_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.WeatherProfilesScreen.weather_profiles_screen)




class WeatherProfilesScreenController:
    """
    The `WeatherProfilesScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.weather_profiles_screen.WeatherProfilesScreenModel
        self.view = View.WeatherProfilesScreen.weather_profiles_screen.WeatherProfilesScreenView(controller=self, model=self.model)

    def get_view(self) -> View.WeatherProfilesScreen.weather_profiles_screen:
        return self.view
