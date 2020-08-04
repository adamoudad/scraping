# Collection of scraping scripts #
Collection of scraping scripts scanning the scrambled web to cram some scoop.

That is a nice tongue-twister, isn't it?

## Craigslist ##
```bash
python craigslist.py
```
Will print a list of newest offers from craigslist Tokyo, in the category appliances.

## Youtube video auto download ##
```bash
python embedded-youtube.py
```
Will scrape the page from URL input, and download all Youtube videos found in links. The videos are placed in a folder `downloads/`.

## Leboncoin.fr ##
*Work in progress*...

Leboncoin is using DataDome to protect from web scraper, therefore [API like this one](https://github.com/tdurieux/leboncoin-api) can't access results anymore.

The script `leboncoin.py` tries to locate `ul` and `li` elements and print results. This method is not completely reliable.
