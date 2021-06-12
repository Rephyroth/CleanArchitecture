from flask import Flask,request, render_template, jsonify, abort
import requests

app = Flask(__name__,template_folder="templates")

@app.route('/All_Books')
def index_All_Books():
    return  render_template ('All_Books.html')

@app.route('/Search')
def search_book():
    return  render_template ('Search.html')

@app.route('/')
def index():
    return  render_template ('menu.html')

@app.route('/One_Book')
def index_One_Book():
    return  render_template ('One_Book.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
