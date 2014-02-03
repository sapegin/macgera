#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from flask import Flask, render_template, url_for, request
from flask_flatpages import FlatPages
from datetime import date, datetime
from pagination import Pagination
from flask_frozen import Freezer

# config
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POSTS_DIR = 'blog'
PAGES_DIR = 'page'
GEEKS_DIR = 'geek'
PER_PAGE = 5
FEED_MAX_LINKS = 5

BASE_URL = 'http://macgera.name'
FREEZER_BASE_URL = 'http://macgera.name'

FREEZER_DESTINATION = '../production'
FREEZER_RELATIVE_URLS = False

# app
app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

# templatetags
def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

app.jinja_env.globals['url_for_other_page'] = url_for_other_page

# functions
def sorted_posts(posts_list):
    return sorted(posts_list, reverse=True, key=lambda p: p.meta['date'])

def get_tags():
    z = (i.meta['tags'] for i in get_posts())
    f = []
    for i in z:
        for a in i:
            f.append(a)
    tags = sorted(set(f))
    return tags

def get_taget(posts_list, tag):
    tagged = [p for p in posts_list if tag in p.meta.get('tags', [])]
    tagged = sorted_posts(tagged)
    return tagged

# get posts
def get_posts():
    blog = [p for p in pages if p.path.startswith(POSTS_DIR)]
    posts = sorted_posts(blog)
    return posts

def get_geeks():
    geeks = [p for p in pages if p.path.startswith(GEEKS_DIR)]
    posts = sorted_posts(geeks)
    return posts

def get_years(pages):
    years = list(set([page.meta.get('date').year for page in pages]))
    years.reverse()
    return years

# views
@app.route('/', defaults={'page': 1})
@app.route('/page/<int:page>/')
def index(page):
    pages = get_posts()[(page-1)*PER_PAGE:PER_PAGE*page]
    pagination = Pagination(page, PER_PAGE, len(get_posts()))
    return render_template('index.html', pages = pages, pagination = pagination, section = 'index')

@app.route('/tag/<string:tag>/')
def tag(tag):
    posts = get_posts()
    return render_template('tag.html', pages = get_taget(posts, tag), tag = tag)

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


# dev
@app.route('/geek/', defaults={'page': 1})
@app.route('/geek/page/<int:page>/')
def geek_index(page):
    pages = get_geeks()[(page-1)*PER_PAGE:PER_PAGE*page]
    pagination = Pagination(page, PER_PAGE, len(get_geeks()))
    return render_template('geek_index.html', pages = pages, pagination = pagination, section = 'index')

@app.route('/geek/tag/<string:tag>/')
def geek_tag(tag):
    posts = get_geeks()
    return render_template('geek_tag.html', pages = get_taget(posts, tag), tag = tag)

@app.route('/geek/archive/')
def geek_archive():
    years = get_years(get_geeks())
    pages = get_geeks()
    return render_template('geek_archive.html', pages=pages, years = years)

@app.route('/geek/feed/')
def geek_feed(): 
    pages = get_geeks()[:FEED_MAX_LINKS]
    now = datetime.now()
    return render_template('base.rss', pages = pages, build_date = now)

# single page
@app.route('/<path:path>/')
def page(path):
    section = path.split('/')[0]
    page = pages.get_or_404(path)
    if section == 'blog':
        template = 'post.html'
    if section == 'geek':
        template = 'geek_post.html'
    if section == 'page':
        template = 'page.html'
    return render_template(template, page = page)

# sys pages
@app.route('/403.html')
def error403():
    return render_template('403.html')


@app.route('/404.html')
def error404():
    return render_template('404.html')


@app.route('/500.html')
def error500():
    return render_template('500.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# freezer

def make_external(url):
    return urljoin(request.url_root, url)

@freezer.register_generator
def pages_frozen():
    for page in pages:
        yield '/%s/' % page.path


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)