from flask import Flask, render_template

#створення екземпляру Flask
app = Flask(__name__)

#створення декоратора шляху
@app.route('/')
def index():
    first_name = 'John'
    favorite_pizza = ['Pepperoni', 'Cheese', 'Mushrooms', 41]
    return render_template('index.html',
                           first_name=first_name,
                           favorite_pizza=favorite_pizza)

#http://127.0.0.1:5000/user/John
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

#custom error pages
#invalid url
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

#internal server error
@app.errorhandler(500)
def page_not_found(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)