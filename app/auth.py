from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import functools
from models import Order

bp = Blueprint('auth', __name__, url_prefix='/auth')


def init_login_manager(app):
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Для доступа к данной странице необходимо пройти процедуру аутентификации.'
    login_manager.login_message_category = 'warning'
    login_manager.user_loader(load_user)
    login_manager.init_app(app)


def load_user(SMS_code):
    user = Order.query.get(SMS_code)
    return user

# @bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         number = request.form.get('login')
#         sms_code = request.form.get('password')
#         if number and sms_code:
#             user = Table2.query.filter_by(SMS_code=sms_code, number=number).first()
#             if user:
#                 login_user(user)
#                 flash('Вы успешно аутентифицированы.', 'success')
#                 next = request.args.get('next')
#                 return redirect(next or url_for('index'))
#         flash('Введены неверные логин и/или пароль.', 'danger')
#     return render_template('auth/login.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        number = request.form.get('login')
        sms_code = request.form.get('password')
        if number and sms_code:
            user = Order.query.filter_by(sms_code=sms_code, num_of_phone=number).first()
            if user:
                login_user(user)
                flash('Вы успешно аутентифицированы.', 'success')
                next = request.args.get('next')
                return redirect(next or url_for('index'))
        flash('Введены неверные логин и/или пароль.', 'danger')
    return render_template('auth/login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))