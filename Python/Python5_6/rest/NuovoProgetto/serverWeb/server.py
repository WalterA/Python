from flask import Flask, render_template, request
import os

api = Flask(__name__)


@api.route('/', methods=['GET'])
def index():
    return render_template('sendfile.html')#per cambiare l'interno della box ,answer="ciao")

   

@api.route('/mansendfile', methods=['POST'])
def RiceviDati():
    sDomande = request.form.get("question")
    image= request.form.get("image")
    if image:
        image.save("./pippo.jpg")
    
    return render_template('sendfile.html',answer="Nessuna risposta"+ sDomande )#per cambiare l'interno della box ,answer="ciao")

   

api.run(host="0.0.0.0", port=8085)