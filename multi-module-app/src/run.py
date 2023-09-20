from flask import Flask
from app import create_app


app: Flask = create_app()
app.run(debug=True)
