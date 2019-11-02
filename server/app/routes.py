from app import app, db
from flask import jsonify, request, current_app
from app.models import User, Article
from functools import wraps
import jwt
from datetime import datetime, timedelta
from base64 import b64encode

# returns { 'token': UTF-8 encoding of token }
def generate_token(username):
    token = jwt.encode({
        'sub': username,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    return { 'token': token.decode('UTF-8') }

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid = {
            'status': 'ERROR',
            'data': 'Invalid token'
        }
        expired = {
            'status': 'ERROR',
            'data': 'Expired token'
        }

        if len(auth_headers) != 2:
            return jsonify(invalid), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = User.query.filter_by(username=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid), 401

    return _verify

@app.route('/add-article', methods=['POST'])
@token_required
def add_article(current_user):
    try:
        data = request.form
        files = request.files
        article = Article()
        article.title = data['title']
        article.category = data['category']
        article.author = data['author']
        article.author_desc = data['author_desc']
        article.date = datetime.strptime(str(data['date']),'%Y-%m-%d')
        article.image = files['image'].read()
        article.caption = data['caption']
        article.text = data['text']
        if 'chart1' in files:
            article.chart1 = files['chart1'].read()
        article.chart1_caption = data.get('chart1','')
        if 'chart2' in files:
            article.chart2 = files['chart2'].read()
        article.chart2_caption = data.get('chart2','')
        db.session.add(article)
        db.session.commit()
        return jsonify({
            'status': 'SUCCESS',
            'data': {},
        })
    except Exception as e:
        print(e)
        return jsonify({
            'status': 'ERROR',
            'data': str(e),
        })

@app.route('/get-articles', methods=['GET'])
def get_articles():
    entries = Article.query.all()
    articles = []
    for entry in entries:
        article = {
            'id': entry.id,
            'title': entry.title,
            'category': entry.category,
            'author': entry.author,
            'author_desc': entry.author_desc,
            'date': entry.date,
            'image': b64encode(entry.image).decode(),
            'caption': entry.caption,
            'text': entry.text,
            'chart1': b64encode(entry.chart1).decode() if entry.chart1 else '',
            'chart1_caption': entry.chart1_caption,
            'chart2': b64encode(entry.chart2).decode() if entry.chart2 else '',
            'chart2_caption': entry.chart2_caption,
        }
        articles.append(article)
    return jsonify({
        'status': 'SUCCESS',
        'data': articles,
    })

@app.route('/get-article', methods=['GET'])
def get_article():
    entry = Article.query.filter_by(id=request.args.get('id')).first()
    if not entry:
        return jsonify({
            'status': 'ERROR',
            'data': None,
        })
    article = {
        'id': entry.id,
        'title': entry.title,
        'category': entry.category,
        'author': entry.author,
        'author_desc': entry.author_desc,
        'date': entry.date,
        'image': b64encode(entry.image).decode(),
        'caption': entry.caption,
        'text': entry.text,
        'chart1': b64encode(entry.chart1).decode() if entry.chart1 else '',
        'chart1_caption': entry.chart1_caption,
        'chart2': b64encode(entry.chart2).decode() if entry.chart2 else '',
        'chart2_caption': entry.chart2_caption,
    }
    return jsonify({
        'status': 'SUCCESS',
        'data': article,
    })

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({
            'status': 'ERROR',
            'data': 'No such user exists',
        })
    if not user.check_password(password):
        return jsonify({
            'status': 'ERROR',
            'data': 'Incorrect password',
        })
    return jsonify({
        'status': 'SUCCESS',
        'data': {
            'token': generate_token(username),
        }
    })

@app.route('/logout', methods=['GET','POST'])
@token_required
def logout():
    return ""

@app.route('/create-user', methods=['POST'])
def create_user():
    username = 'mark'
    password = 'testpass'
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({
            'status': 'ERROR',
            'data': 'User with username ' + username + ' already exists',
        })
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'status': 'SUCCESS',
        'data': {
            'username': user.username,
            'token': generate_token(user.username),
        },
    })
