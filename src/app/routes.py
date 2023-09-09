from mvc_flask import Router

home = Router.namespace('')
home.get('/', 'home#index')
