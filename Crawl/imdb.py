# -*- coding:utf-8 -*-
import requests
from  pyquery import PyQuery as pq
import pandas as pd

def get_releasedate(movieid):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    url = 'https://www.imdb.com/title/{id}/?ref_=tt_urv'.format(id=movieid)
    detailpage = requests.get(url, headers=headers)
    doc = pq(detailpage.text)
    release_date = doc('#titleDetails.article div.txt-block h4').items()
    for r in release_date:
        if 'Release Date:' in str(r):
            date = str(r).strip('<h4 class="inline">Release Date:</h4>').strip('(USA)')
    return date


def judgedate(dateone,datetwo):
    pass


def get_firstpagereviews(movieid):
    reviewlist =[]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    url = 'https://www.imdb.com/title/{id}/reviews?ref_=tt_urv'.format(id=movieid)
    detailpage = requests.get(url, headers=headers)
    doc = pq(detailpage.text)
    reviews = doc('.lister-item-content').items()
    for r in reviews:
        reviewsdate = r('.display-name-date span.review-date').text()
        releasedate  = get_releasedate(movieid)
        reviewstext = r('.content').text()
        if judgedate(reviewsdate,releasedate):
            reviewlist.append(reviewstext)
    return reviewlist

path = r'C:\Users\Administrator\Desktop\movie.csv'
moviedata = pd.read_csv(path)
mid = moviedata.ix[:,1].values[0:3]
for m in mid:
    try:
        reviews = get_firstpagereviews(m)
        print(reviews)
        df = pd.DataFrame([reviews])
        df.to_csv('imdb_data.csv', mode='a', header=False)
    except:
        pass

