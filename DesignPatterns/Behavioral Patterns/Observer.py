# Abstract Oberver class with function - updates
class Observer:
    def update(self, temperature, humidity, pressure):
        pass

# Abstract Subject class with register and remove observer and notify observer functions
class Subject:
    def register_observer(self, observer):
        pass

    def notify_observer(self, observer):
        pass

    def remove_observer(self, observer):
        pass


class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._humidity = 0
        self._temperature = 0
        self._pressure = 0

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()


class CurrentConditionsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Current conditions: {temperature}F degrees and {humidity}% humidity")


# Test the implementation
weather_station = WeatherStation()
current_display = CurrentConditionsDisplay()
weather_station.register_observer(current_display)

weather_station.set_measurements(30, 65, 1013)


# Current conditions: 30F degrees and 65% humidity