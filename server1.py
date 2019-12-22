from flask import Flask, jsonify, request, abort
from bookDAO import bookDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello, World!"

#curl "http://127.0.0.1:5000/books"
@app.route('/books')
def getAll():
    #print("in getall")
    results = bookDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/books/2"
@app.route('/books/<int:id>')
def findById(id):
    foundBooks = bookDAO.findByID(id)

    return jsonify(foundBooks)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])

def create():
    if not request.json:
        abort(400)
    # other checking 
    books = {
        "Title": request.json['Title'],
        "Author": request.json['Author'],
        "Price": request.json['Price'],
    }
    values =(books['Title'],books['Author'],books['Price'])
    newId = bookDAO.create(values)
    books['id'] = newId
    return jsonify(books)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBooks = bookDAO.findByID(id)
    if not foundBooks:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)

    if 'Title' in reqJson:
        foundBooks['Title'] = reqJson['Title']
    if 'Author' in reqJson:
        foundBooks['Author'] = reqJson['Author']
    if 'Price' in reqJson:
        foundBooks['Price'] = reqJson['Price']
    values = (foundBooks['Title'],foundBooks['Author'],foundBooks['Price'],foundBooks['id'])
    bookDAO.update(values)
    return jsonify(foundBooks)
        

    

@app.route('/books/<int:id>' , methods=['DELETE'])
def delete(id):
    bookDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)