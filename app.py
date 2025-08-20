from flask import Flask,render_template, request, redirect, url_for, session
import os, json
from functools import wraps

app=Flask(__name__)
app.secret_key="1234"

ARTICLES_DIR = "articles"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

if not os.path.exists(ARTICLES_DIR):
    os.makedirs(ARTICLES_DIR)

#Load All Articles
def load_articles():
    articles = []
    for filename in sorted(os.listdir(ARTICLES_DIR)):
        if filename.endswith('.json'):
            with open(os.path.join(ARTICLES_DIR, filename), 'r') as f:
                articles.append(json.load(f))
    articles.sort(key=lambda x: x['date'], reverse=True)
    return articles

#Load Single Article by ID
def load_article(article_id):
    file_path = os.path.join(ARTICLES_DIR, f"{article_id}.json")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return None

def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapped

@app.route('/')
def home():
    articles = load_articles()
    return render_template('home.html', articles=articles)

@app.route('/article/<id>')
def article(id):
    article = load_article(id)
    if not article:
        return "Article not found", 404
    return render_template('article.html', article=article)

#admin login
@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if (request.form['username'] == ADMIN_USERNAME and
            request.form['password'] == ADMIN_PASSWORD):
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        return render_template('login.html', error="Invalid credentials")
    return render_template('login.html', error=None)

#admin logout
@app.route('/admin/logout')
def logout():
    session.pop("logged_in", None)
    return redirect(url_for('home'))

#dashboard - list articles with admin options
@app.route('/admin')
@login_required
def dashboard():
    articles = load_articles()
    return render_template('dashboard.html', articles=articles)

#add article
@app.route('/admin/add', methods=['GET', 'POST'])
@login_required
def add_article():
    if request.method == 'POST':
        new_id = str(max([int(a['id']) for a in load_articles()] + [0]) + 1)
        article = {
            "id": new_id,
            "title": request.form['title'],
            "content": request.form['content'],
            "date": request.form['date']
        }
        with open(os.path.join(ARTICLES_DIR, f"{new_id}.json"), 'w') as f:
            json.dump(article, f)
        return redirect(url_for('dashboard'))
    return render_template('add_article.html', article=None)

#edit article
@app.route('/admin/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit_article(id):
    filepath = os.path.join(ARTICLES_DIR, f"{id}.json")
    article = load_article(id)
    if not article:
        return "Article not found", 404
    if request.method == 'POST':
        article['title'] = request.form['title']
        article['date'] = request.form['date']
        article['content'] = request.form['content']
        with open(filepath, 'w') as f:
            json.dump(article, f)
        return redirect(url_for('dashboard'))
    return render_template('edit_article.html', article=article)

#delete article
@app.route('/admin/delete/<id>', methods=['POST'])
@login_required
def delete_article(id):
    filepath = os.path.join(ARTICLES_DIR, f"{id}.json")
    if os.path.exists(filepath):
        os.remove(filepath)
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True)