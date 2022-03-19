from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function


@app.route('/')
def index():
    writen_books = [
        ("Daily Business Quotes", "daily-quotes.jpeg", "lorem ipsum dolor"),
        ("The corporate World", "world.jpeg", "lorem ipsum dolor"),
        ("The Baby Genius", "baby.jpeg", "lorem ipsum dolor"),
        ("Power of Association", "association.jpeg", "lorem ipsum dolor"),
    ]
    return render_template('index.html', books=writen_books)


@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')


@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')


if __name__ == '__main__':
    app.run(debug=True)
