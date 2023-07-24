# @app.route('/buscar', methods=['GET', 'POST'])
# def buscar():
#     if request.method == 'POST':
#         id_solicitud = request.form['id_solicitud']

#         # Buscar los datos por ID de solicitud
#         solicitud = datos_solicitudes.get(id_solicitud)

#         if solicitud:
#             return render_template('mostrar_solicitud.html', solicitud=solicitud)
#         else:
#             return "No se encontraron datos para esa solicitud."

#     return render_template('buscar.html')


# @app.route('/agregar_estado', methods=['GET', 'POST'])
# def agregar_estado():
#     if request.method == 'POST':
#         id_solicitud = request.form['id_solicitud']
#         nuevo_estado = request.form['nuevo_estado']
#         observaciones = request.form['observaciones']

#         # Actualizar los datos de la solicitud con la información del nuevo estado y observaciones
#         solicitud = datos_solicitudes.get(id_solicitud)
#         if solicitud:
#             solicitud['nuevo_estado'] = nuevo_estado
#             solicitud['observaciones'] = observaciones

#         return redirect(url_for('buscar'))

#     id_solicitud = request.args.get('id_solicitud')
#     return render_template('agregar_estado.html', id_solicitud=id_solicitud)


# @app.route('/todos_los_datos', methods=['GET'])
# def todos_los_datos():
#     return render_template('todos_los_datos.html', datos=datos_solicitudes)

# pass
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Diccionario para almacenar los datos
datos_solicitudes = {}


@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # Obtener los datos del formulario
        id_solicitud = request.form['id_solicitud']
        fecha_actual = request.form['fecha_actual']
        reclutador = request.form['reclutador']
        generador = request.form['generador']
        lider_gh = request.form['lider_gh']
        lider_vacante = request.form['lider_vacante']
        empresa = request.form['empresa']
        zona = request.form['zona']
        planta = request.form['planta']
        num_vacantes = request.form['num_vacantes']

        # Guardar los datos en el diccionario
        datos_solicitudes[id_solicitud] = {
            'fecha_actual': fecha_actual,
            'reclutador': reclutador,
            'generador': generador,
            'lider_gh': lider_gh,
            'lider_vacante': lider_vacante,
            'empresa': empresa,
            'zona': zona,
            'planta': planta,
            'num_vacantes': num_vacantes
        }

    return render_template('formulario.html')


@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        id_solicitud = request.form['id_solicitud']

        # Buscar los datos por ID de solicitud
        solicitud = datos_solicitudes.get(id_solicitud)

        if solicitud:
            return render_template('mostrar_solicitud.html', solicitud=solicitud, id_solicitud=id_solicitud)
        else:
            return "No se encontraron datos para esa solicitud."

    return render_template('buscar.html')


@app.route('/agregar_estado', methods=['GET', 'POST'])
def agregar_estado():
    if request.method == 'POST':
        id_solicitud = request.form['id_solicitud']
        nuevo_estado = request.form['nuevo_estado']
        observaciones = request.form['observaciones']

        # Actualizar los datos de la solicitud con la información del nuevo estado y observaciones
        solicitud = datos_solicitudes.get(id_solicitud)
        if solicitud:
            solicitud['nuevo_estado'] = nuevo_estado
            solicitud['observaciones'] = observaciones

        return redirect(url_for('buscar'))

    id_solicitud = request.args.get('id_solicitud')
    return render_template('agregar_estado.html', id_solicitud=id_solicitud)


@app.route('/todos_los_datos', methods=['GET'])
def todos_los_datos():
    # Obtener todos los datos del diccionario
    solicitudes = datos_solicitudes

    return render_template('todos_los_datos.html', solicitudes=solicitudes)


if __name__ == '__main__':
    app.run(debug=True)
