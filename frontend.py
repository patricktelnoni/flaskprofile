from flask import Blueprint, request, render_template, url_for, session, redirect
from flask_bootstrap import Bootstrap
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from .nav import nav
from .forms import *
from .model.artikel import *
from .model.user import *



frontend = Blueprint('frontend', __name__)



def top_nav():
    return Navbar(
    View('Flask-Bootstrap', '.index'),
    View('Home', '.index'),
    View('Logout', '.logout')  if session.get('logged_in') else View('Login', '.form_login'), 
    View('Artikel', '.artikel'),    
    Subgroup(
        'Docs',
        Link('Flask-Bootstrap', 'http://pythonhosted.org/Flask-Bootstrap'),
        Link('Flask-AppConfig', 'https://github.com/mbr/flask-appconfig'),
        Link('Flask-Debug', 'https://github.com/mbr/flask-debug'),
        Separator(),
        Text('Bootstrap'),
        Link('Getting started', 'http://getbootstrap.com/getting-started/'),
        Link('CSS', 'http://getbootstrap.com/css/'),
        Link('Components', 'http://getbootstrap.com/components/'),
        Link('Javascript', 'http://getbootstrap.com/javascript/'),
        Link('Customize', 'http://getbootstrap.com/customize/'), ),
    # Text('Using Flask-Bootstrap {}'.format(FLASK_BOOTSTRAP_VERSION)), 
    )

nav.register_element('frontend_top', top_nav)

@frontend.route('/example_form/', methods=('GET', 'POST'))
def example_form(): 
    form = SignupForm(request.form)
    if request.method == "POST":
        admin            = User(
                                username   = request.form.get('email'),
                                nama       = request.form.get('name'),
                                password   = request.form.get('password')                                
                             )         
         # In case user table doesn't exists already. Else remove it.    
        db.session.add(admin)
        db.session.commit()
    return render_template('signup.html', form=form)

@frontend.route('/login_form/', methods=('GET', 'POST'))
def form_login(): 
    form = LoginFom(request.form)
    if request.method == "POST":
        
        nama       = request.form.get('name')
        password   = request.form.get('password')
        user       = User.query.filter_by(nama=nama, password=password).first()
        if bool(user):
            session['nama']        = user.nama
            session['username']    = user.username
            session['logged_in']   = True
            return redirect('/')
        else:
            return redirect('login_form')
    return render_template('login.html', form=form)

@frontend.route('/')
def index():
    if not session.get('logged_in'):
        return redirect('login_form')
    else: 
        return render_template('index.html')
        # return "Sok dah ente lewat"
    # return render_template('index.html')

@frontend.route('/logout')
def logout():
    session.clear()
    return redirect('login_form')

@frontend.route('/artikel')
def artikel():
    db.create_all()
    artikel_list    = Artikel.query.all()
    return render_template('artikel.html', data=artikel_list)

@frontend.route('/rundb')
def rundb():
    admin = User()
    db.create_all() # In case user table doesn't exists already. Else remove it.    
    db.session.add(admin)
    db.session.commit() 
    return 'sucessfully create table in database'
