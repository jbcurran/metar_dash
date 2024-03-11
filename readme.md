## Intro:
In the summer of '23, I created a proof of concept for VFA that provided a simple webpage that displayed current METAR data for any airport.   This page would also alert the user if the METAR prohibited students from a solo flight, based on wind, visibility, or clouds.  
you can view this page here: https://metarmonitor.fly.dev  
  
I thought it would be interesting to see if I could iterate on that idea with a Tableau dashboard as the user interface. 
The objective is to provide the user with a simple dashboard to quickly understand the METAR data for a given observation.
I added historical data, and provided the user with the ability to select observation times in the past.
The data is retrieved from https://aviationweather.gov/data/api/

>- **get_metar.py** retrieves the data and stores in a SQLite db (metar_observations.db)
>- **check_data.py** queries the db to check if there are 24 observations per day
>- **output.csv** is used to get the data into Tableau Public

Dashboard link:  
https://public.tableau.com/views/METARMap/Dashboard2?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link

Examples of Weather Limiting Solo Flights:
February 28 at 19:00 - Wind at 26 kts
March 4 at 6:00 - Clouds at 300 ft

### software used:  
- postman - initial api discovery  
- pycharm - python ide  
- dbvisualizer - adhoc sql queries  
- tableau public - dashboard creation and hosting  
- github - code/data repository  
  

### TODO - further possible iterations
- Convert datetimes to local, API returns zulu
- Provide better wind indicator viz with compass rose
- Provide information on multiple cloud reports
- Provide natural language weather observations
- Run python script on cron to collect data everyday
- Expand dataset to additional airports
- Provide additional dashboards for analyzing metar patterns
