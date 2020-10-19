from flask import render_template, url_for, redirect
from flask import request, session, jsonify
from .secondDB import kind, trajectory
from .forms import userForm, loginForm
from .schemas import Users, Checks
from sqlalchemy import exc
from random import randint
from app import app, db


@app.route('/')
def index():
    return render_template('inicio.html', name='desconocido')


@app.route('/inicio')
def inicioApp():
    return render_template('inicioApp.html',
                            name=session['username'],
                            title='Inicio')


@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for('index'))


@app.route('/login/', methods=['GET', 'POST'])
def Show_login_Form():

    form = loginForm(request.form)
    if request.method == 'POST':
        name = form.nombre.data
        passw = form.contraseña.data

        usuario = Users.query.filter_by(username=name).first()

        if usuario and usuario.password == passw:
            session['username'] = name

            return redirect(url_for('inicioApp'))

    return render_template('login.html', title="Inicio de sesión", form=form, name='Desconocido')


@app.route('/signup/', methods=['GET', 'POST'])
def Show_Signup_Form():

    form = userForm()

    if request.method == 'POST':
        new_data = Users(username=form.nombre.data,
                         password=form.contraseña.data,
                         address=form.direccion.data,
                         identification=form.ID.data,
                         postalCode=form.codigoPostal.data)

        db.session.add(new_data)
        session['username'] = form.nombre.data

        try:
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()

        return redirect(url_for('inicioApp'))

    return render_template('signup.html', title='Registrarse', form=form, name='Desconocido')


@app.route('/paquete')
def paquete():
    return render_template('paquete.html', title="Paquetes", paq=kind, name=session['username'])


@app.route('/trayectoria/ <type>', methods=['GET', 'POST'])
def paqueteRespuesta(type):

    session['type'] = type
    session['num'] = randint(0, 100000)

    return render_template('trayectoria.html',
                            title="Trayectoria",
                            trayectoria=trajectory,
                            paq=type,
                            price=kind[type],
                            name=session['username'])


@app.route('/factura/<des>', methods=['GET', 'POST'])
def factura(des):
    n = session['username']
    usuario = Users.query.filter_by(username=n).first()
    total = kind[session['type']] + trajectory[des]


    if request.method == 'POST':
        new_check = Checks(name=n,
                            numofcheck=str(session['num']),
                            destination=des,
                            identification=usuario.identification,
                            paquete=session['type'],
                            price=total)

        db.session.add(new_check)
        try:
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()

        return render_template('final.html', name=session['username'], title="Factura")

    factura = {
        'Nombre': usuario.username,
        'Numero de factura': session['num'],
        'Identificacion': usuario.identification,
        'direccion': usuario.address,
        'Codigo Postal': usuario.postalCode,
        'paquete': session['type'],
        'Destino': des,
        'Precio total': total
    }


    return render_template('factura.html', factura=factura,
                            title="Factura", name=session['username'])


@app.route('/Buscar', methods=['GET', 'POST'])
def buscar():

    if request.method == 'POST':
        n = str(request.form['fac'])

        f = Checks.query.filter_by(numofcheck=n).first()
        return render_template('mostrar.html', factura=f)

    return render_template('buscar.html',
                            name=session['username'],
                            title='buscar')
