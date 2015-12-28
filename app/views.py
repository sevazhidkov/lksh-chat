from flask import render_template, request, session, redirect
from . import app
from .forms import LoginForm


@app.route('/', methods=['POST', 'GET'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect('/chat')
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
    return render_template('index.html', form=form)


@app.route('/chat', methods=['POST', 'GET'])
def chat():
    name = session.get('name', '')
    if name == '':
        return redirect('/')
    return render_template('chat.html', name=name)
