# Google Play Crawler

A crawler that crawls all applications' data from the Google Play and save it to MongoDB.

## Requirements
- Python 3
- MySQL

## Usage

```shell
# Clone this repo
git clone https://github.com/yaoandy107/google_play_crawler.git

# Switch the directory
cd google_play_crawler

# Install all the package required in this project
pip3 install -r requirements.txt

# Run SQL initial script (There is many way to run this script)
mysql -uroot < init.sql

# Run crawler
scrapy crawl google -s JOBDIR=crawls/google_play
```

> If you want to switch the language of Google Play, you could go to modify the function `process_links` in `spiders/google.py`.
