## Intro:
In the summer of '23, I created a proof of concept for VFA that provided a simple webpage that displayed current METAR data for any airport.   This page would also alert the user if the METAR prohibited students from a solo flight, based on wind, visibility, or clouds.  
you can view this page here: https://metarmonitor.fly.dev  
  
I thought it would be interesting to see if I could iterate on that idea with a Tableau dashboard as the user interface. I added historical data, and provided the user with the ability to select observation times in the past.

Dashboard link:  
https://public.tableau.com/app/profile/ben.curran/viz/METARMap/Dashboard2v


### software used:  
- postman - initial api discovery  
- pycharm - python ide  
- dbvisualizer - adhoc sql queries  
- tableau public - dashboard creation and hosting  
- github - code/data repository  
  

### TODO - Things I would do if I kept working on this
- Convert datetimes to local, API returns zulu
- Provide better wind indicator viz with compass rose
- Run python script on cron to collect data everyday
- Expand dataset to additional airports
- Provide additional dashboards for analyzing metar patterns
