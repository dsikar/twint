# Scrape handle mentions for given years
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time

years = []
for i in range (2020, 2022):
  years.append(i)

handles = ['AstraZeneca', 'bhp', 'Shell', 'UnileverUKI', 'RioTinto', 'DiageoGB', 'HSBC', 'GSK', 'BATplc', 'nationalgriduk', 'bp_plc']

for handle in handles :
  for year in years :
    given_date = '1/1/' + str(year)
    date_format = '%d/%m/%Y'
    startdate = datetime.strptime(given_date, date_format)
    for i in range(1,13) :
      enddate = startdate + relativedelta(months=1)
      query = "twint -s \"@{}\" --since \"{}\" --until \"{}\" --verified >> {}_{}.txt".format(handle, startdate, enddate, handle, year)
      print("Running:", query)
      # print(query)
      os.system(query)
      startdate = enddate
      time.sleep(5) # give twitter a rest
