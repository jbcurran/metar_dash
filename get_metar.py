import requests
import datetime
import sqlite3
from xml.etree import ElementTree
import csv

station = 'KBTV'

SKY_COVER = {
        "SKC": "clear",
        "CLR": "clear",
        "NSC": "clear",
        "NCD": "clear",
        "FEW": "a few ",
        "SCT": "scattered ",
        "BKN": "broken ",
        "OVC": "overcast",
        "///": "",
        "VV": "indefinite ceiling",
    }

#Create table for retrieved METAR data
con = sqlite3.connect('metar_observations.db')
cur = con.cursor()
# cur.execute("DROP TABLE 'metar'")
# con.commit()
cur.execute("""
    CREATE TABLE IF NOT EXISTS metar(
        observation_time string UNIQUE, 
        station_id string, 
        raw_text string,
        latitude decimal,
        longitude decimal,
        temp_c decimal,
        dewpoint_c decimal,
        wind_dir_degrees decimal,
        wind_speed_kt decimal,
        wind_gust_kt decimal,
        visibility_statute_mi string,
        altim_in_hg decimal,
        flight_category string,
        sky_cover string,
        cloud_base_ft_agl string)
""")
con.commit()

#Create list of Columns
cur.execute('select * from metar')
columns = list(map(lambda x: x[0], cur.description))

#Perform Datetime calc to build array of desired datetimes in format for API
def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

days = 2
today = datetime.datetime.today().replace(second=0, microsecond=0, minute=0, hour=0)
print(today - datetime.timedelta(days=days))
dts = [dt.strftime('%Y%m%d_%H%M') for dt in
       datetime_range(today - datetime.timedelta(days=days), datetime.datetime.today(), datetime.timedelta(minutes=60))]
#Manually specifcy dates if api limits responses
dts = [dt.strftime('%Y%m%d_%H%M') for dt in
       datetime_range(datetime.datetime(2024, 3, 9, 0, 0), datetime.datetime(2024,3, 11, 0, 0), datetime.timedelta(minutes=60))]

#For each desired datetime, retrive METAR data
for dt in dts:
    print(dt)
    url = "https://aviationweather.gov/api/data/metar/"
    params = {'ids': station, 'date': dt, 'format':'xml'}
    response = requests.get(url, params=params)
    #print(response.text)
    data = {}
    for metar in ElementTree.fromstring(response.content).iter('METAR'):
        for column in columns:
            if column == 'sky_cover':
                try:
                    data[column] = SKY_COVER[metar.find('sky_condition').attrib['sky_cover']]
                except:
                    data[column] = ""
            elif column == 'cloud_base_ft_agl':
                try:
                    data[column] = metar.find('sky_condition').attrib['cloud_base_ft_agl']
                except:
                    data[column] = ""
            else:
                if metar.find(column) is None:
                    data[column] = ""
                else:
                    data[column] = metar.find(column).text

    #Insert METAR data into sqlite db
    cur.execute("INSERT or IGNORE into metar VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
        list(data.values())
    ))
    con.commit()

#Tableau Public doesn't provide sqlite connector, bummer
cur.execute('SELECT * FROM metar')
with open('output.csv','w') as out_csv_file:
  csv_out = csv.writer(out_csv_file)
  # write header
  csv_out.writerow([d[0] for d in cur.description])
  # write data
  for result in cur:
    #print(result)
    csv_out.writerow(result)

con.close()
