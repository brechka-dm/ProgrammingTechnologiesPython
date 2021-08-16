from abc import ABC, abstractmethod


class iObserver(ABC):
    @abstractmethod
    def update(self): pass


class iSubject(ABC):
    @abstractmethod
    def registerObserver(self, observer): pass
    @abstractmethod
    def removeObserver(self, observer): pass
    @abstractmethod
    def notifyObservers(self, observer): pass


class iDisplayElement(ABC):
    @abstractmethod
    def display(self): pass


class WeatherData(iSubject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for o in self.observers:
            o.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()


class CurrentConditionsDisplay(iObserver, iDisplayElement):
    def __init__(self, weatherData):
        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print(
                "Current conditions:"
                + str(self.temperature)
                + "C degrees and "
                + str(self.humidity)
                + "% humidity"
            )

    def unregister(self):
         self.weatherData.removeObserver(self)


if __name__ == "__main__":
    weatherData = WeatherData()
    currentDisplay = CurrentConditionsDisplay(weatherData)
    weatherData.setMeasurements(25, 65, 30.4)
    weatherData.setMeasurements(27, 70, 29.2)
    weatherData.setMeasurements(23, 90, 29.2)
