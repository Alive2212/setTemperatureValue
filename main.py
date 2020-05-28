import json
import datetime

jsonFile = open('./defaultTemperatureValue.json', )
defaultTemperatureValue = json.load(jsonFile)


def main():
    print(getTemperatureValue())

def getTemperatureValue():
    # monday is 0 and sunday is 7
    toDay = datetime.datetime.today()
    return defaultTemperatureValue[str(toDay.isocalendar()[2])][str(toDay.hour)]

if __name__ == '__main__':
    main()

jsonFile.close()
