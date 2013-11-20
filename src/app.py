#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from datetime import date, datetime
from pagination import Pagination

# config
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
BASE_URL = 'http://macgera.name'
FREEZER_BASE_URL = 'http://macgera.name'
FREEZER_DESTINATION = '../macgera.github.io'
FREEZER_DESTINATION_IGNORE = ['.git*', 'CNAME']
FREEZER_RELATIVE_URLS = False
PER_PAGE = 5
FEED_MAX_LINKS = 5

# app
app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

# get posts
def get_posts(year=None):
    blog = (p for p in pages if 'blog' in p.meta.values())
    posts = sorted(blog, reverse=True, key=lambda p: p.meta['date'])
    return posts

def get_tags():
    z = (i.meta['tags'] for i in get_posts())
    f = []
    for i in z:
        for a in i:
            f.append(a)
    tags = sorted(set(f))
    return tags

def get_years(pages):
    years = list(set([page.meta.get('date').year for page in pages]))
    years.reverse()
    return years

def get_taget(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    tagged = sorted(tagged, reverse=True, key=lambda p: p.meta['date'])
    return tagged

@app.route('/', defaults={'page': 1})
@app.route('/page/<int:page>/')
def index(page):
    pages = get_posts()[(page-1)*PER_PAGE:PER_PAGE*page]
    pagination = Pagination(page, PER_PAGE, len(get_posts()))
    return render_template('index.html', pages = pages, pagination = pagination, section = 'index', tags = get_tags())

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page = page, tags = get_tags())

@app.route('/tag/<string:tag>/')
def tag(tag):
    return render_template('tag.html', pages = get_taget(tag), tag = tag, tags = get_tags())

@app.route('/feed/')
def feed(): 
    pages = get_posts()[:FEED_MAX_LINKS]
    now = datetime.now()
    return render_template('base.rss', pages = pages, build_date = now)

@app.route('/archive/')
def archive():
    years = get_years(get_posts())
    pages = get_posts()
    return render_template('archive.html', pages=pages, years = years)

def make_external(url):
    return urljoin(request.url_root, url)

# url for freeze
@freezer.register_generator
def pages_frozen():
    for page in pages:
        yield '/%s/' % page.path

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)