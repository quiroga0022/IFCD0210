from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
@app.route('/')

def hello_world():
    return "Hola Mundo"

@app.route('/hola')
def hola():
    cadena = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Hola Usuario</h1>
        <h2>Bienvenido a mi sitio Flask</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vero rerum aliquam neque exercitationem necessitatibus
        non possimus quia suscipit sequi voluptate esse libero doloribus eligendi ut minima, deserunt reprehenderit
        nostrum consectetur.</p>
        
    </body>
    </html>
    """
    return cadena

@app.route('/prueba')
def prueba():
    return render_template('prueba.html')

@app.route('/jinja1')
def jinja1():
    lista = ['uno', 'dos', 'tres', 'cuatro']
    # return render_template('jinja1.html',nombre='Paco',apellidos='Gomez García',numeros=lista)
    return render_template('principal.html')


if __name__ == '__main__':
    app.run(debug=True)