from flask import Flask, render_template, url_for

# Mapping of page names to local cover image filenames. The actual image
# URL is resolved using ``url_for`` in each route so new images can be
# dropped into ``static/images`` without changing the template logic.
COVER_IMAGES = {
    'Home': 'cover_placeholder.svg',
    'About': 'cover_placeholder.svg',
    'Projects': 'cover_placeholder.svg',
    'Resume': 'cover_placeholder.svg',
    'Contact Me': 'cover_placeholder.svg',
    'Library': 'cover_placeholder.svg',
    'My Playlists': 'cover_placeholder.svg'
}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'index.html',
        page_name='Home',
        cover_image=url_for('static', filename=f"images/{COVER_IMAGES['Home']}")
    )

@app.route('/about')
def about():
    return render_template(
        'about.html',
        page_name='About',
        cover_image=url_for('static', filename=f"images/{COVER_IMAGES['About']}")
    )

@app.route('/projects')
def projects():
    return render_template(
        'projects.html',
        page_name='Projects',
        cover_image=url_for('static', filename=f"images/{COVER_IMAGES['Projects']}")
    )

@app.route('/resume')
def resume():
    return render_template(
        'resume.html',
        page_name='Resume',
        cover_image=url_for('static', filename=f"images/{COVER_IMAGES['Resume']}")
    )

@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        page_name='Contact Me',
        cover_image=url_for('static', filename=f"images/{COVER_IMAGES['Contact Me']}")
    )

@app.route('/library')
def library():
    return render_template(
        'library.html',
        page_name='Library',
        cover_image=url_for('static', filename=f"images/{COVER_IMAGES['Library']}")
    )

@app.route('/playlists')
def playlists():
    return render_template(
        'playlists.html',
        page_name='My Playlists',
        cover_image=url_for('static', filename=f"images/{COVER_IMAGES['My Playlists']}")
    )

if __name__ == '__main__':
    app.run(debug=True)
