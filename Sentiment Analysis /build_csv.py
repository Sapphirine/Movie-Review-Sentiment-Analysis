%matplotlib inline

import json

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 30)

# set some nicer defaults for matplotlib
from matplotlib import rcParams

#these colors come from colorbrewer2.org. Each is an RGB triplet
dark2_colors = [(0.10588235294117647, 0.6196078431372549, 0.4666666666666667),
                (0.8509803921568627, 0.37254901960784315, 0.00784313725490196),
                (0.4588235294117647, 0.4392156862745098, 0.7019607843137254),
                (0.9058823529411765, 0.1607843137254902, 0.5411764705882353),
                (0.4, 0.6509803921568628, 0.11764705882352941),
                (0.9019607843137255, 0.6705882352941176, 0.00784313725490196),
                (0.6509803921568628, 0.4627450980392157, 0.11372549019607843),
                (0.4, 0.4, 0.4)]

rcParams['figure.figsize'] = (10, 6)
rcParams['figure.dpi'] = 150
rcParams['axes.color_cycle'] = dark2_colors
rcParams['lines.linewidth'] = 2
rcParams['axes.grid'] = False
rcParams['axes.facecolor'] = 'white'
rcParams['font.size'] = 14
rcParams['patch.edgecolor'] = 'none'


def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
    """
    Minimize chartjunk by stripping out unnecesary plot borders and axis ticks
    
    The top/right/left/bottom keywords toggle whether the corresponding plot border is drawn
    """
    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)
    
    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')
    
    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()

api_key = 'YOUR KEY HERE'
movie_id = '770672122'  # toy story 3
url = 'http://api.rottentomatoes.com/api/public/v1.0/movies/%s/reviews.json' % movie_id

#these are "get parameters"
options = {'review_type': 'top_critic', 'page_limit': 20, 'page': 1, 'apikey': api_key}
data = requests.get(url, params=options).text
data = json.loads(data)  # load a json string into a collection of lists and dicts


from io import StringIO  
movie_txt = requests.get('https://raw.github.com/cs109/cs109_data/master/movies.dat').text
movie_file = StringIO(movie_txt) # treat a string like a file
movies = pd.read_csv(movie_file, delimiter='\t')


def base_url():
    return 'http://api.rottentomatoes.com/api/public/v1.0/'

def rt_id_by_imdb(imdb):
    """
    Queries the RT movie_alias API. Returns the RT id associated with an IMDB ID,
    or raises a KeyError if no match was found
    """
    url = base_url() + 'movie_alias.json'
    
    imdb = "%7.7i" % imdb
    params = dict(id=imdb, type='imdb', apikey=api_key)
    
    r = requests.get(url, params=params).text
    r = json.loads(r)
    
    return r['id']


def _imdb_review(imdb):
    """
    Query the RT reviews API, to return the first page of reviews 
    for a movie specified by its IMDB ID
    
    Returns a list of dicts
    """    
    rtid = rt_id_by_imdb(imdb)
    url = base_url() + 'movies/{0}/reviews.json'.format(rtid)

    params = dict(review_type='top_critic',
                  page_limit=20,
                  page=1,
                  country='us',
                  apikey=api_key)
    data = json.loads(requests.get(url, params=params).text)
    data = data['reviews']
    data = [dict(fresh=r['freshness'], 
                 quote=r['quote'], 
                 critic=r['critic'], 
                 publication=r['publication'], 
                 review_date=r['date'],
                 imdb=imdb, rtid=rtid
                 ) for r in data]
    return data

def fetch_reviews(movies, row):
    m = movies.irow(row)
    try:
        result = pd.DataFrame(_imdb_review(m['imdbID']))
        result['title'] = m['title']
    except KeyError:
        return None
    return result

def build_table(movies, rows):
    dfs = [fetch_reviews(movies, r) for r in range(rows)]
    dfs = [d for d in dfs if d is not None]
    return pd.concat(dfs, ignore_index=True)


critics = build_table(movies, 3000)
critics.to_csv('critics.csv', index=False)
critics = pd.read_csv('critics.csv')


#let's drop rows with missing quotes
critics = critics[~critics.quote.isnull()]


n_reviews = len(critics)
n_movies = critics.rtid.unique().size
n_critics = critics.critic.unique().size


print "Number of reviews: %i" % n_reviews
print "Number of critics: %i" % n_critics
print "Number of movies:  %i" % n_movies
