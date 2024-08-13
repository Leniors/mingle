#~/usr/bin/python3
""" test signup """
from . import app_views
from flask import render_template, redirect, url_for
from .forms import SignUpForm

@app_views.route('/testsignup', methods=['GET', 'POST'])
def testsignup():
    form = SignUpForm()
    if form.validate_on_submit():
        return redirect(url_for('mingle'))
    return render_template('testsignup.html', form=form)
