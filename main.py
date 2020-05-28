import json
import datetime

jsonFile = open('./defaultTemperatureValue.json', )
defaultTemperatureValue = json.load(jsonFile)


def main():
    set_temperature_value_driver(get_temperature_value())


def get_temperature_value():
    # monday is 0 and sunday is 7
    toDay = datetime.datetime.today()
    return defaultTemperatureValue[str(toDay.isocalendar()[2])][str(toDay.hour)]

def set_temperature_value_driver(temperature_controller_value):
    # TODO here should implement something to communicate with IOT Devices
    print(temperature_controller_value)


if __name__ == '__main__':
    main()

jsonFile.close()
