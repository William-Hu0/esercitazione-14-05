from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
app = Flask(__name__)
df = pd.read_csv("profilo.csv")

@app.route("/")
def index():
    df = pd.read_csv("profilo.csv")
    dati = df.iloc[0].to_dict()
    return render_template("index.html", dati=dati)



@app.route("/prenotazione", methods=["GET", "POST"])
def prenotazione():
    df = pd.read_csv("profilo.csv")
    if request.method == "POST":
        nuovo_profilo = {
        "Nome": request.form["nome"],
        "Cognome": request.form["cognome"],
        "Sport": request.form["Sport"],
        "Giorno": request.form["Giorno"],
        "Mese": request.form["Mese"],
        "Anno": request.form["Anno"],
        "Ora": request.form["Ora"],
        "Minuti": request.form["Minuti"],
        "Note Opzionali": request.form["Note Opzionali"],
        }
        prenotazione = pd.DataFrame([nuovo_profilo])
        df=pd.concat([df, prenotazione])
        df.to_csv("profilo.csv", index=False)
        return redirect(url_for('index'))

    df = pd.read_csv("profilo.csv")
    dati = df.iloc[0].to_dict()
    return render_template("prenotazione.html", dati=dati)

@app.route("/tabella")
def tabella():
    return render_template("tabella.html", df=df.to_htm(index=False))





if __name__ == '__main__':
    app.run(debug=True)