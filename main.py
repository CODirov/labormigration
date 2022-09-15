from flask import render_template

from models import People, db
from config import app

def add_person(name, birth, date_contr):
    people = People(name=name, birthday=birth, date_registr=date_contr)
    db.session.add(people)
    db.session.commit()

# @app.route("/")
# def home():
#     people = People.query.all()
#     return render_template("index.html", people=people)


# @app.route('/myview/<int:page>',methods=['GET'])
# def view(page=1):
#     per_page = 10
#     posts = People.query.order_by(People.time.desc()).paginate(page,per_page,error_out=False)
#     return render_template('index.html',posts=posts)


@app.route('/', methods=['GET'], defaults={"page": 1}) 
@app.route('/<int:page>', methods=['GET'])
def index(page):
    page = page
    per_page = 50
    people = People.query.paginate(page,per_page,error_out=False)
    # print("Result......", users)
    return render_template("index.html", users=people)

if __name__=="__main__":
    app.run(debug=True, port=5000)
