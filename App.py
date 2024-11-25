from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

#  наша корневая страиницу лендинга 
@app.route('/')
@app.route('/home')
def home():
    # Загрузка и отображение главной страницы (landing page)
    return render_template('landing.html') 

#  
@app.route('/about')
def about():
     return render_template('about.html') 

if __name__ == '__main__':
    app.run(debug=True) #в проде изменить на False 
