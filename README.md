# cbssports_scraper

Scraper for scraping the top 30 players for the following basketball positions

PG - SG - SF - PF - C 

from the site http://www.cbssports.com/nba/playerrankings

## Deployment
    git clone git@github.com:thayton/cbssports_scraper.git

    cd cbssports_scraper

    virtualenv venv 
    source venv/bin/activate

    pip install -r requirements.txt

    cd scraper
    python manage.py migrate  

## Usage

Help

```
$ ./scraper.py -h
usage: scraper.py [-h] [-s] [-e]

optional arguments:
  -h, --help    show this help message and exit
  -s, --scrape  do a fresh scrape of the top 30 players for positions
                PG/SG/SF/PF/C
  -e, --export  export results as CSV
```

Launch a scrape

```
(venv)Todds-MBP:cbssports_scraper mhayton$ ./scraper.py -s
Scraping position links
Scraping players for position PG
Scraping players for position SG
Scraping players for position SF
```

Export scrape results from database in CSV format into a file named players.csv

```
$ ./scraper.py -e
(venv)Todds-MBP:cbssports_scraper mhayton$ ls -l players.csv 
-rw-r--r--  1 mhayton  staff  6872 Jan 30 15:19 players.csv
(venv)Todds-MBP:cbssports_scraper mhayton$ wc -l players.csv 
     151 players.csv
```  
