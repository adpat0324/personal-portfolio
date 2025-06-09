from flask import Flask, render_template, url_for

# Simple mapping of page names to placeholder cover images
COVER_IMAGES = {
    'Home': 'https://via.placeholder.com/64?text=Home',
    'About': 'https://via.placeholder.com/64?text=About',
    'Projects': 'https://via.placeholder.com/64?text=Projects',
    'Resume': 'https://via.placeholder.com/64?text=Resume',
    'Contact Me': 'https://via.placeholder.com/64?text=Contact',
    'Library': 'https://via.placeholder.com/64?text=Library',
    'My Playlists': 'https://via.placeholder.com/64?text=Playlists'
}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', page_name='Home',
                           cover_image=COVER_IMAGES['Home'])

@app.route('/about')
def about():
    return render_template('about.html', page_name='About',
                           cover_image=COVER_IMAGES['About'])

@app.route('/projects')
def projects():
    return render_template('projects.html', page_name='Projects',
                           cover_image=COVER_IMAGES['Projects'])

@app.route('/resume')
def resume():
    return render_template('resume.html', page_name='Resume',
                           cover_image=COVER_IMAGES['Resume'])

@app.route('/contact')
def contact():
    return render_template('contact.html', page_name='Contact Me',
                           cover_image=COVER_IMAGES['Contact Me'])

@app.route('/library')
def library():
    return render_template('library.html', page_name='Library',
                           cover_image=COVER_IMAGES['Library'])

@app.route('/playlists')
def playlists():
    return render_template('playlists.html', page_name='My Playlists',
                           cover_image=COVER_IMAGES['My Playlists'])

if __name__ == '__main__':
    app.run(debug=True)
