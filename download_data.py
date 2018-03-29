import requests
import os
import calendar
from datetime import datetime
from tqdm import tqdm

DATA_URL = "http://www.houstontx.gov/health/Pollen-Mold/{}_Archives/{}_{}_{}.xls"
DATA_DIR = "data"

def download(month, year, data_type):
    url = DATA_URL.format(data_type.title(), month, year, data_type)
    filename = "{}_{}_{}.xls".format(month, year, data_type)
    resp = requests.get(url, stream=True)
    if not resp.status_code == 200:
        print("Error downloading {} data for {} of {}".format(data_type, month, year))
        print
        return
    with open(os.path.join(DATA_DIR, filename), 'wb') as f:
        for chunk in resp.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

months = [calendar.month_name[i].lower() for i in range(1, 13)]
years = [y for y in range(2013, datetime.now().year)]
data_types = ["pollen", "mold"]
all_data = [(m, y, t) 
             for m in months 
             for y in years 
             for t in data_types] 

if __name__ == "__main__":
    for month, year, data_type in tqdm(all_data):
        download(month, year, data_type)
