from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import PizzaForm
# from ..request import get_movies,get_movie,search_movie

from ..models import Pizza,User
from flask_login import login_required, current_user
from .forms import UpdateProfile
from .. import db,photos
import markdown2 
@main.route("/")
@main.route("/home")
def index():

   '''
   View root page function that returns the index page and its data
   '''
   title = 'Welcome to Pizza app'

   page = request.args.get('page', 1, type=int)
  

   return render_template('index.html')

@main.route("/user_order")
def user_order():

   '''
   View root page function that returns the index page and its data
   '''
   
   pizza=Pizza.query.all()

    
  

   return render_template('users_orders.html',pizza=pizza)


@main.route('/pizza/nea')
def nea():
    pizza=Pizza.query.filter_by(name='Neapolitan')

    return render_template('nea.html', pizza=pizza)


@main.route('/pizza/chi')
def chi():
    pizza=Pizza.query.filter_by(name='Chicago')

    return render_template("chi.html", pizza=pizza)
@main.route('/pizza/new')
def new():
    pizza=Pizza.query.filter_by(name='New-york')

    return render_template('new.html', pizza=pizza)

@main.route('/pizza/new')
def greek():
    pizza=Pizza.query.filter_by(name='Greek')

    return render_template('greek.html', pizza=pizza)
    
@main.route("/post/new", methods= ['GET', 'POST'])
@login_required
def new_order():

    form = PizzaForm()
    if form.validate_on_submit():
        pizza = Pizza(name=form.name.data, toppings = form.topping.data, crust = form.crust.data)
        db.session.add(pizza)
        db.session.commit()
        
        return redirect(url_for('main.user_order'))
    return render_template('order.html', new_order_form = form, legend = 'New Post')

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

