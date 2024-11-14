from flask import Flask, render_template, request

api = Flask(__name__)
Utenti=[["mario","rossi","0"],["gianni","bianchi","0"]]

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/visualizza', methods=['GET'])
def visualizza():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
   
    for utente in Utenti:
            if utente[0] == nome and utente[1]==cognome:
                return render_template('ok.html', nome=nome, cognome=cognome)
            
    return render_template('no.html', nome=nome, cognome=cognome)


@api.route('/visualizza1', methods=['GET'])
def index123():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    return render_template('visualizza.html', nome=nome, cognome=cognome)

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8085)

