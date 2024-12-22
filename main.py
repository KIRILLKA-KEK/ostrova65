from flask import Flask, render_template
from now import condition, temperatura, wind, wni, davlenie, vlazhn, zaxod, vosxod
from afternoon import acondition, atemperatura, awind, awni, adavlenie, avlazhn, azaxod, avosxod
import static
import templates
from events import notification
from status import status_lw
from status_up import status_up

name = 'main'
app = Flask(name, static_folder='static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/')
def main():
    return render_template('index.html', condition=condition, temperatura=temperatura,
                           wind=wind, icon=wni, davlenie=davlenie, vlazhn=vlazhn, zaxod=zaxod, vosxod=vosxod,
                           acondition=acondition, atemperatura=atemperatura,
                           awind=awind, aicon=awni, adavlenie=adavlenie, avlazhn=avlazhn, azaxod=azaxod,
                           avosxod=avosxod, notification=notification, status_lw=status_lw, status_up=status_up)

@app.route('/ostrova')
def ostrova():
    return render_template('index.html', condition=condition, temperatura=temperatura,
                           wind=wind, icon=wni, davlenie=davlenie, vlazhn=vlazhn, zaxod=zaxod, vosxod=vosxod,
                           acondition=acondition, atemperatura=atemperatura,
                           awind=awind, aicon=awni, adavlenie=adavlenie, avlazhn=avlazhn, azaxod=azaxod,
                           avosxod=avosxod, notification=notification, status_lw=status_lw, status_up=status_up)


@app.route('/contacts')
def contacts():
    return render_template("contacts.html", notification=notification)


@app.route('/writeus')
def writeus():
    return render_template("form.html", notification=notification)


@app.route('/workmode')
def workmode():
    return render_template("workmode.html", notification=notification)

@app.route('/tariffs')
def tariffs():
    return render_template("tariffs.html", notification=notification)

@app.route('/rent')
def rent():
    return render_template("rent.html", notification=notification)



if name == 'main':
    app.run(debug=True)
