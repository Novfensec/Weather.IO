# Weather.IO

Weather.IO is a sleek and modern weather application built using Kivy and KivyMD. This open-source project provides real-time weather updates by leveraging the OpenWeatherMap API. Whether you're a developer looking to learn more about Kivy or a user who needs an intuitive weather app, Weather.IO is designed to be both educational and functional.

## Features

- **Real-Time Weather Updates**: Get current weather information for any city, including temperature, humidity, wind speed, and more.
- **Modern User Interface**: A clean and responsive UI built with KivyMD for a consistent look across devices.
- **Advanced Weather Icons**: Display weather conditions with dynamic icons using the OpenWeatherMap API.
- **Cross-Platform Support**: Runs smoothly on Windows, macOS, Linux, Android, and iOS.
- **Open Source**: Licensed under the MIT License, making it free to use, modify, and distribute.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Novfensec/Weather.IO.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Weather.IO
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Usage

Simply run the application and enter the name of a city to get the latest weather updates. The app will display the current temperature, weather conditions, and a relevant icon.

## Tutorials

View the tutorial series on youtube:
[Kivy and KivyMD Weather App - Youtube Playlist](https://youtube.com/playlist?list=PL_ybtaIzwgfI8NYTPM8Id09Rjn-YtStRa&si=7vmQP2z4EhKeM0y1)

## Configuration

To use the OpenWeatherMap API, you'll need to add your API key:

1. Create a free account on [OpenWeatherMap](https://openweathermap.org/).
2. Obtain your API key.
3. Replace the placeholder in the `View/HomeScreen/Components/weather_api_data.py` file with your API key:
   ```python
   api_key = "your_openweathermap_api_key"
   ```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. Please make sure to follow the code style and include tests for any new features or bug fixes.

## License

Weather.IO is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions, suggestions, or feedback, feel free to reach out through GitHub Issues or contact me directly at [novfensec@protonmail.com].