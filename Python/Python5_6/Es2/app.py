from flask import Flask, render_template, request

api = Flask(__name__)
Utenti=[["mario","rossi","0"],["gianni","bianchi","0"]]

@api.route('/', methods=['GET'])
def index():
    return render_template('home.html')

@api.route('/accedi', methods=['GET'])
def index123():
    return render_template('accedi.html')

@api.route('/registrati', methods=['GET'])
def index1234():
    return render_template('registrazioneform.html')

@api.route('/consulta_old', methods=['GET'])
def consultaold():
    return render_template('consultaold.html')


@api.route('/consulta_new', methods=['GET'])
def consultanew():
    return render_template('consultanew.html')

@api.route('/gestisci_login', methods=['GET'])
def acc1():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    for utente in Utenti:
            if utente[0] == nome and utente[1]==cognome:
                return render_template('lista_servizi.html', nome=nome, cognome=cognome)
            else:
                Utenti.append([nome,cognome])
                return render_template('personale.html')

@api.route('/gestisci_reg', methods=['GET'])
def acc():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    for utente in Utenti:
            if utente[0] == nome and utente[1]==cognome:
                return render_template('personale.html', nome=nome, cognome=cognome)
            else:
                Utenti.append([nome,cognome])
                return render_template('accedi.html')

    
"""
 nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    Utenti.append([nome,cognome])
 """
    
if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8085)

