# import ftplib
#
# ftp = ftplib.FTP('tgftp.nws.noaa.gov')
# response = ftp.login()
# print(response)
# ftp.cwd('data')
# response = ftp.nlst()
# print(response)
# x = ftp.retrbinary('RETR observations/metar/decoded/KORD.TXT', open('KORD.TXT', 'wb').write)
# print(x)
# print('______________')

# from pprint import pprint as pp
# import requests
# response = requests.get("http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt")
# data = [field.split() for field in response.text.split('\r\n')[7:]]
# for row in data:
#     if row[4] == '---':
#         row[4] = None
#     else:
#         row[4] = int(row[4])
#     if row[6] == '---':
#         row[6] = None
#     else:
#         row[6] = float(row[6].strip('#'))
#     row[0], row[1] = int(row[0]), int(row[1])
#     row[2], row[3], row[5] = float(row[2]), float(row[3]), float(row[5])
# result = [['year','average max','average min','average rain']]
# year = 1948
# average_max = 0
# average_min = 0
# average_rain = 0
# count_month = 0
# for row in data:
#     if year != row[0]:
#         result.append([year,average_max/count_month,average_min/count_month,average_rain/count_month])
#         year = row[0]
#         average_max = 0
#         average_min = 0
#         average_rain = 0
#         count_month = 0
#     average_max += row[2]
#     average_min += row[3]
#     average_rain += row[5]
#     count_month += 1
# pp(result)

import requests
from pprint import pprint as pp
import json
response = requests.get("https://data.cityofchicago.org/resource/6zsd-86xi.json?$where=date between '2015-01-10T12:00:00' and '2015-01-10T13:00:00'")
# chicago=json.loads(response.text)
chicago=response.json()
pp(chicago)
outfile = open("chicago_data_01.json", "w")
json.dump(chicago, outfile)
outfile.close()
