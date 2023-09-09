from flask import render_template



class HomeController():
    def index(self):
        response = render_template('pages/home/index.html.j2'), 200
        return response
