# Cloud-kun Weather Reporter

Cloud-kun Weather Reporter is a simple Python application that provides current weather information for a specified city using the Weatherstack API. It displays temperature, wind speed, wind direction, UV index, time, country, and weather description.

## Features

- Retrieve and display current weather data for a specified city.
- User-friendly graphical user interface (GUI) using Tkinter.
- Fetches weather data from the Weatherstack API.
- Displays temperature in Celsius, wind speed in km/h, UV index, and weather description.
- Shows observation time and country for the weather data.

## Prerequisites

Before running the Weather App, make sure you have the following prerequisites:

- Python 3.x installed on your system.
- Required Python packages: `requests`, `tkinter`, and `Pillow`.
- Weatherstack API access key. Sign up for a free account at [Weatherstack](https://weatherstack.com/) and obtain an API key.

## Getting Started

1. Clone the repository.

2. Install the required Python packages:

   ```
   pip install requests tkinter Pillow
   ```

3. Open the `app.py` file in a text editor.

4. Replace `'YOUR_WEATHERSTACK_API_ACCESS_KEY'` with your actual Weatherstack API access key in the `getWeather()` function.

5. Run the `app.py` file.

6. Enter the desired city in the input field and click the "Submit" button.

7. The current weather information for the specified city will be displayed on the screen, including temperature, wind speed, wind direction, UV index, time, country, and weather description.

Enjoy using the Weather App to stay updated with the latest weather conditions in your desired cities!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Weatherstack API - [Weatherstack](https://weatherstack.com/)

Feel free to customize the README file according to your needs, adding more details about the application and instructions for users.
