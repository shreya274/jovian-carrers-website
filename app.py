
from flask import Flask, render_template, jsonify



app = Flask(__name__)

JOBS = [
  
    {
    'id':1,
    'title':'Data analyst',
    'location':'Bengaluru,India',
    'salary':'Rs. 10,00,000',
  },

  {
    'id':2,
    'title':'Data scientist',
    'location':'Delhi,India',
    'salary':'Rs. 15,00,000',
  },

{
    'id':3,
    'title':'Frontend Enngineer',
    'location':'remote',
    
  },

{
    'id':4,
    'title':'Backend Enngineer',
    'location':'San Francisco,USA',
    'salary':'$150,000',
  }
]

@app.route("/")
def hello_world():

    return render_template('home.html',jobs=JOBS, company_name ='Jovain')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__=="__main__" :
 app.run(host='0.0.0.0', debug=True)