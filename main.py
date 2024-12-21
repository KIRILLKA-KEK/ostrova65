from flask import Flask, render_template
from now import condition, temperatura, wind, wni, davlenie, vlazhn, zaxod, vosxod
from afternoon import acondition, atemperatura, awind, awni, adavlenie, avlazhn, azaxod, avosxod
import static
import templates

name = 'main'
app = Flask(name, static_folder='static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/ostrova')
def main():
    return render_template('index.html', condition=condition, temperatura=temperatura,
                           wind=wind, icon=wni, davlenie=davlenie, vlazhn=vlazhn, zaxod=zaxod, vosxod=vosxod,
                           acondition=acondition, atemperatura=atemperatura,
                           awind=awind, aicon=awni, adavlenie=adavlenie, avlazhn=avlazhn, azaxod=azaxod, avosxod=avosxod
                           )


@app.route('/contacts')
def contacts():
    return render_template("contacts.html")


@app.route('/writeus')
def writeus():
    return render_template("form.html")


@app.route('/workmode')
def workmode():
    return render_template("workmode.html")


if name == 'main':
    app.run(debug=True)
