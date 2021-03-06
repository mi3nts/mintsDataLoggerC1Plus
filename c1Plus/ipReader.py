from datetime import timezone
import time
import os
import datetime
import netifaces as ni
from collections import OrderedDict
import netifaces as ni
from mintsC1Plus import mintsSensorReader as mSR
from mintsC1Plus import mintsDefinitions as mD


dataFolder = mD.dataFolder


def main():

    sensorName = "IP"
    dateTimeNow = datetime.datetime.now()

    ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

    sensorDictionary =  OrderedDict([
            ("dateTime"     , str(dateTimeNow)),
            ("ip"  ,str(ip))
            ])

    mSR.sensorFinisherIP(dateTimeNow,sensorName,sensorDictionary)

if __name__ == "__main__":
   main()
