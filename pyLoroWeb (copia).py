__author__ = 'cgarcia'

import zmq
import time
import os
import ConfigParser
import bottle
import sys
import pymongo
from os.path import join, dirname
from bottle import route, static_file, template

class test():
    def __init__(self):
        ruta_arch_conf = os.path.dirname(sys.argv[0])
        archivo_configuracion = os.path.join(ruta_arch_conf, '/home/administrador/desarrollo/python/pyloro/pyloro.cfg')
        self.fc = ConfigParser.ConfigParser()
        self.fc.read(archivo_configuracion)
        self.zmqConectar()

    def zmqConectar(self):
        ''' Busca en el archivo de configuracion pyloro.cfg todos los 
        demonios servidores ZMQ y los conecta'''
        
        self.socket = ''
        context = zmq.Context()
        self.socket = context.socket(zmq.REQ)
        seccionDemonio = 'DEMONIOS'
        
        if self.fc.has_section(seccionDemonio):
            for demonios in self.fc.items(seccionDemonio):
                seccion, archivo = demonios
                seccionFinal = seccion.upper()
                if self.fc.has_section(seccionFinal):
                    listaPar = []
                    for var, par in self.fc.items(seccionFinal):
                        listaPar.append(par)
                    print(listaPar)               
                    ip_telefono, \
                    puerto_telefono, \
                    puerto_adb_forward, \
                    ip_demonio_zmq, \
                    puerto_demonio_zmq, \
                    serial_telefono = listaPar
                    servSock = 'tcp://{0}:{1}'.format(ip_demonio_zmq, puerto_demonio_zmq)
                    try:
                        self.socket.connect(servSock)
                        print('Conexion Satisfactoria con el servidor {0}'.format(servSock))
                    except:
                        print('Ocurrio un Error al momento de conectar al Socket Server {0}'.format(servSock))

    def enviar(self, telefono, mensaje):
        msg = '{0}^{1}'.format(telefono, mensaje)
        devuelve = True

        try:
            self.socket.send(msg)
        except zmq.ZMQError:
            e = sys.exc_info()[1]
            print(e)

        #Se recibe el mensaje de vuelta
        msg_in = self.socket.recv()            
        noEnviado, nombreServidor = msg_in.split(',')
        if int(noEnviado):
            devuelve = True
        else:
            devuelve = False
        return devuelve

app = test()

appPath = '/home/foxcarlos/desarrollo/python/pyLoroWeb/views/static/img'

# Rutas de archivos estAticos
  
# javascript
@bottle.get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root=join(appPath, 'static/js'))
  
# estilos css
@bottle.get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root=join(appPath, 'static/css'))
  
'''
# imagenes
@bottle.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root=join(appPath, 'static/img'))
'''

# imagenes
@bottle.route('/images/<filename:re:.*\.png>')
def send_image(filename):
    return bottle.static_file(filename, root='/home/foxcarlos/desarrollo/python/pyLoroWeb/static/img')
    
# fuentes
@bottle.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root=join(appPath, 'static/fonts'))
    
@bottle.route('/')
def index():
    return bottle.template('index')

@bottle.post('/login')
def login():
    usuario = bottle.request.forms.get('usu_form')
    clave = bottle.request.forms.get('pass_form')

    cliente = pymongo.MongoClient('localhost', 27017)
    baseDatos = cliente.pyloroweb
    coleccionUsuarios = baseDatos.usuarios
    
    buscar = coleccionUsuarios.find({'usuario':usuario, 'clave':clave}).count()
    if buscar:
        return bottle.template('pyloro_sms')
    else:
        cabecera = 'Mensaje'
        msg = 'Usuario o Clave invalida'
        return bottle.template('mensaje_login', {'cabecera':cabecera, 'mensaje':msg})

@bottle.route('/sms')
def sms():
    return bottle.template('pyloro_sms')

@bottle.post('/smsenviar')
def smsEnviar():
    numero = bottle.request.forms.get('numero')
    mensaje = bottle.request.forms.get('comentarios')
    
    if validaSms(numero, mensaje.strip()):
        devuelve = app.enviar(numero, mensaje)
        
        if devuelve:
            cabecera = 'Felicidades ...'
            msg = 'Mensaje enviado con exito al numero {0}'.format(numero)
            return bottle.template('mensaje_exito', {'cabecera':cabecera, 'mensaje':msg})
        else:
            cabecera = 'Houston tenemos un problema...'
            msg = 'No se pudo enviar el SMS al numero:{0}'.format(numero)
    else:
        cabecera = 'Houston tenemos un problema...'
        msg = 'Numero telefonico invalido o Mensaje Vacio'
        return bottle.template('mensaje_envio', {'cabecera':cabecera, 'mensaje':msg})

def validaSms(num, msg):
    devuelve = True
    if not num:
        devuelve = False
    elif not msg:
        devuelve = False
    elif len(num) !=11:
        devuelve = False
    elif num[:4] not in ['0426', '0416', '0414', '0424', '0412']:
        devuelve = False
    return devuelve

bottle.debug(True)
bottle.run(host='localhost', port=8085)
