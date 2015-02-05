# views.py 


from flask import Flask, flash, redirect, render_template, request, session, url_for, g
from functools import wraps
import sqlite3
from forms import AddTaskForm

app = Flask(__name__)
app.config.from_object('config')


def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

# Add the data we need to calculate mortgage (this is the home page)
@app.route('/', methods=['GET', 'POST'])
def mort_data_gather():
	if request.method =='GET':
		return render_template('template.html')

	g.db = connect_db()
	income = request.form['income']
	down_payment = request.form['down_payment']
	interest_rate = request.form['interest_rate']

	g.db.execute('insert into mortgages (income, down_payment, interest_rate) values(?,?, ?)', \
		[request.form['income'], request.form['down_payment'], request.form['interest_rate']])
	g.db.commit()
	g.db.close()
	return redirect(url_for('mort_data_display'))

@app.route('/display/')
def mort_data_display():
	g.db = connect_db()
	cur = g.db.execute('select * from mortgages order by mortgage_id desc limit 1')
	mortgage_data = [dict(mortgage_id=row[0], income=row[1], down_payment=row[2], interest_rate=row[3]) for row in cur]
	#monthly_income = (mortgage_data[1]/12)
	g.db.close()
	return render_template(
		'mortgage_data.html',
		mortgage_data = mortgage_data)
