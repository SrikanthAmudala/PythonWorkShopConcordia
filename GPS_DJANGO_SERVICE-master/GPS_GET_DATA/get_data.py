'''
@author: Sunny
@desc: Gets the data from gps
'''
import datetime

from suds.client import Client


class Data:
    last_update = []

    def get_gps_data(self):
        try:
            client1 = Client("give your client id here")
            requestId = client1.service.BeginGetGps(
                guid="give your guid here",
                # startTime=datetime.datetime(2017, 7, 7, 21 , 0, 1),
                endTime=datetime.datetime.now(),
                startTime=datetime.datetime.now() - datetime.timedelta(seconds=30),
                gatewayId=193
            )
            while (client1.service.GetProgress(
                    guid="give your guid here",
                    requestId=int(requestId)) != 'Ready'):
                pass

            print 'request id: ', requestId
            gps = client1.service.CompleteGetGps(
                guid="give your guid here",
                requestId=int(requestId)
            )

            if len(gps) != 0:
                for i in gps:
                    for j in i[1]:
                        temp = list(j)
                # print 'temp: ', temp
                temp_dict = dict(temp)

                x1 = {}
                x1["geometry"] = {"type": "Point",
                                  "coordinates": [temp_dict.get("Longitude"), temp_dict.get("Latitude"), ],
                                  "Speed": temp_dict.get("Speed"),
                                  "Timestamp": (temp_dict.get("Timestamp")).isoformat(),
                                  "GatewayID": temp_dict.get("GatewayId"), "Heading": temp_dict.get("Heading")}
                x1["type"] = "Feature"
                x1["properties"] = {}
                Data.last_update.append(x1)
                print 'JSON: ',x1
                return x1
            else:
                return Data.last_update[len(Data.last_update) - 1]
                # print 'no gps data found'
        except Exception as e:
            print e.message
