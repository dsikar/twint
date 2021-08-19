# Scraping google news titles

Basic title scraping, to add content see scratch.py dictionary keys.

## Requirements

```
$ pip install pygooglenews
```

## Scraping

```
$ python get_esg_news.py > esg_news.txt
```
this will open file esg_topics.txt and scrape google news for every topic, returning all titles, outputting to esg_news.txt (9k lines approx. as per committed code).

