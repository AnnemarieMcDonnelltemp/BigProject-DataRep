from flask import Flask, jsonify, request, abort
from bookDAO import bookDAO
from flask import Flask, render_template
import mysql.connector as mariadb


app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/book')
def getAll():
    #print("in getall")
    results = bookDAO.getAll()
    return jsonify(results)

@app.route('/book<int:id>')
def findById(id):
    foundBook = bookDAO.findByID(id)

    return jsonify(foundBook)


@app.route('/book', methods=['POST'])


def create():
    if not request.json:
        abort(400)
    
    book = {
        "title": request.json['title'],
        "author": request.json['author'],
        "price": request.json['price'],
    }
    values =(book['title'],book['author'],book['price'])
    newId = bookDAO.create(values)
    book['id'] = newId
    return jsonify(book)


@app.route('/book/<int:id>', methods=['PUT'])
def update(id):
    foundBook = bookDAO.findByID(id)
    if not foundBook:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)

    if 'Title' in reqJson:
        foundBook['title'] = reqJson['title']
    if 'Author' in reqJson:
        foundBook['author'] = reqJson['author']
    if 'Price' in reqJson:
        foundBook['price'] = reqJson['price']
    values = (foundBook['title'],foundBook['author'],foundBook['price'],foundBook['id'])
    bookDAO.update(values)
    return jsonify(foundBook)
        

    

# @app.route('/books/<int:id>' , methods=['DELETE'])
def delete(id):
    bookDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run()