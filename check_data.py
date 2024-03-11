import sqlite3

con = sqlite3.connect('metar_observations.db')
cur = con.cursor()
# cur.execute("DROP TABLE 'metar'")
# con.commit()
cur.execute("""
SELECT strftime('%Y-%m-%d', observation_time), count(*)
FROM metar 
group by strftime('%Y-%m-%d', observation_time)
            """)
res = cur.fetchall()
print(res)