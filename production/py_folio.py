import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from funct import page_filter, return_page, return_tag, tag_filter

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', pages=pages), 404


@app.route('/')
def index():
    portfolio = page_filter(pages, 'portfolio')
    main_page = return_page(pages, 'home')
    return render_template('index.html', portfolio=portfolio, page=main_page)


@app.route('blog/tag/<string:tag>/')
def tag(tag):
    blog_posts = page_filter(pages, 'blog')
    tagged = tag_filter(blog_posts, tag)
    return render_template('tag.html', posts=tagged, tag=tag)


@app.route('/blog/')
def bloghome():
    blog_posts = page_filter(pages, 'blog')
    main_page = return_page(pages, 'home')
    tags = return_tag(blog_posts, 'tags')
    return render_template('blog.html', posts=blog_posts, page=main_page, tags=tags)


@app.route('/blog/post/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='0-0-0-0')
