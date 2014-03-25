__author__ = 'cgarcia'

import zmq
import time
import os
import ConfigParser
import bottle
import sys
import pymongo
from bson.objectid import ObjectId
from os.path import join, dirname
from bottle import route, static_file, template
import re

class enviarZMQ():
    def __init__(self):
        ruta_arch_conf = os.path.dirname(sys.argv[0])
        fi = '/home/administrador/desarrollo/python/pyloro/pyloro.cfg'
        archivo_configuracion = os.path.join(ruta_arch_conf, fi)
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

app = enviarZMQ()

def buscarContactosListas(objetoUsuarioIdPasado):
    '''Este metodo busca dentro de la base de datos mongo
    todos los conmtactos y listas que pertenecen a un usuario
    del Sistema pasado como parametro'''

    server = pymongo.MongoClient('localhost', 27017)
    baseDatos = server.pyloroweb
    coleccionListas = baseDatos.listas
    coleccionContactos = baseDatos.contactos
    
    objetoUsuarioId = objetoUsuarioIdPasado 
    
    #Aqui se buscan los contactos y las listas que pertecen al usuario que inico sesion para mostrarlos en los combobox
    #Tanto los contactos como las listas se deben mostrar solo los del usuario que inicio sesion
    nombresMostrar = [f['nombre'] for f in coleccionContactos.find({"usuario_id":objetoUsuarioId}).sort('nombre')]
    listasMostrar = [f['nombre_lista'] for f in coleccionListas.find({"usuario_id":objetoUsuarioId}).sort('nombre_lista')]
    return nombresMostrar, listasMostrar

def buscarUsuarioId(usuario):
    '''parametros 1 string: usuario
    Este metodo busca el objetoId en mongodb del usuario que inicio
    sesion en el Sistema pyLoroWeb'''

    usuarioBuscar = usuario
    cliente = pymongo.MongoClient('localhost', 27017)
    baseDatos = cliente.pyloroweb
    coleccionUsuarios = baseDatos.usuarios                    
    buscarId = [f['_id'] for f in coleccionUsuarios.find({'usuario':usuarioBuscar})]
    objetoId = buscarId[0] if buscarId else ''
    return objetoId

def validaLogin(usuario, clave):
    ''' parametros recibidos 2:
    (string usuario, string clave)
    Metodo para validar el inicio de sesion
    contra la base de datos'''

    lcUsuario = usuario
    lcClave = clave
    accesoPermitido = False

    cliente = pymongo.MongoClient('localhost', 27017)
    baseDatos = cliente.pyloroweb
    coleccionUsuarios = baseDatos.usuarios
    
    buscar = coleccionUsuarios.find({'usuario':lcUsuario.lower(), 'clave':lcClave}).count()
    if buscar:
        accesoPermitido = True
    return accesoPermitido

@bottle.route('/static/<filename:path>') 
def static(filename): 
    return bottle.static_file(filename, root='static/')

@bottle.post('/seleccionar')
def seleccionarContactos():
    '''Metodo POST capturar las variables  que vienen del FORM elegir-contactos 
    y procesarlas para luego mostrarla en los controles text de la vista 
    seleccionados en el ComboBox HTML'''

    server = pymongo.MongoClient('localhost', 27017)
    baseDatos = server.pyloroweb    
    coleccionContactos = baseDatos.contactos

    #Busca el objetoId del usuario en la base de datos mongodb
    objetoUsuarioId = buscarUsuarioId(usuario)

    #Capturar todas las variables que vienen del <FORM elegir-comtactos/>
    listaDevuelta = bottle.request.forms.getall('elegir-contactos')
    listaDevuelta2 = bottle.request.forms.getall('elegir-listas')

    #Busca en la Base de datos el nombre y el telefono los contactos seleccionados en el ComboBox
    contactosElegidos = ['{0}<{1}>'.format(f['nombre'], f['telefonos'])\
            for f in coleccionContactos.find({'nombre':{'$in':listaDevuelta}, "usuario_id":objetoUsuarioId})]
    listasElegidas = listaDevuelta2

    #Aqui se buscan los contactos y las listas que pertecen al usuario que inico sesion para mostrarlos en los combobox
    nombresMostrar, listasMostrar = buscarContactosListas(objetoUsuarioId)
    
    textContactos = ','.join(contactosElegidos)
    textListas = ','.join(listasElegidas)

    return bottle.template('pyloro_sms_multiple.html', text1=textContactos, text2=textListas, comboBoxContactos=nombresMostrar, comboBoxListas=listasMostrar)

@bottle.route('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/')
def login():
    ''' Metodo para el inicio de Sesion en pyLoroWeb'''

    global usuario
    global clave
    usuario = ''
    clave = ''
    buscar = False

    usuario = bottle.request.forms.get('usu_form')
    clave = bottle.request.forms.get('pass_form')

    buscar = validaLogin(usuario, clave)
    if buscar:
        objetoUsuarioId = buscarUsuarioId(usuario)
        nombresMostrar, listasMostrar = buscarContactosListas(objetoUsuarioId)
        return bottle.template('pyloro_sms_multiple.html', comboBoxContactos=nombresMostrar, comboBoxListas=listasMostrar)
    else:
        cabecera = 'Lo Siento...!'
        msg = 'El usuario o la clave es invalida'
        return bottle.template('mensaje_login', {'cabecera':cabecera, 'mensaje':msg})

@bottle.route('/smsenviar')
def smsEnviar():
    try:
        objetoUsuarioId = buscarUsuarioId(usuario)
        nombresMostrar, listasMostrar = buscarContactosListas(objetoUsuarioId)
        return bottle.template('pyloro_sms_multiple.html', comboBoxContactos=nombresMostrar, comboBoxListas=listasMostrar)
    except:
        cabecera = 'Lo Siento ...!'
        msg = 'Ud. no ha iniciado sesion en el servidor'
        return bottle.template('mensaje_login', {'cabecera':cabecera, 'mensaje':msg})

@bottle.post('/smsenviar')
def smsEnviar():
    ''' Metodo que captura lo ingresado en el form de envio de SMS
    y lo envia al servidor ZMQ con la Clase enviar '''

    contactos = bottle.request.forms.get('contactos')
    listas = bottle.request.forms.get('listas')
    numeros = bottle.request.forms.get('numeros')
    mensaje = bottle.request.forms.get('mensaje')
    
    listasNumeros = componerContactosListas(contactos, listas) + numeros.split(',')

    try:
        if not validaLogin(usuario, clave):
            cabecera = 'Lo Siento ...!'
            msg = 'Ud. no ha iniciado sesion en el servidor'
            return bottle.template('mensaje_login', {'cabecera':cabecera, 'mensaje':msg})
    except:
        cabecera = 'Lo Siento ...!'
        msg = 'Ud. no ha iniciado sesion en el servidor'
        return bottle.template('mensaje_login', {'cabecera':cabecera, 'mensaje':msg})
  
    for numero in listasNumeros:
        if validaSms(numero, mensaje.strip()):
            devuelve = app.enviar(numero, mensaje)
            if devuelve:
                cabecera = 'Felicidades ...'
                msg = 'Mensaje enviado con exito al numero {0}'.format(numero)
            else:
                cabecera = 'Lo Siento ...!'
                msg = 'No se pudo enviar el SMS al numero:{0}'.format(numero)
    return bottle.template('mensaje_exito', {'cabecera':cabecera, 'mensaje':msg})

def componerContactosListas(contactos, listas):
    '''Obtener solo los numeros de telefonos de las selecciones
    hechas en l combobox del html'''
    
    server = pymongo.MongoClient('localhost', 27017)
    baseDatos = server.pyloroweb    
    coleccionContactos = baseDatos.contactos
    coleccionListas = baseDatos.listas

    recvContactos = contactos
    recvListas = listas.split(',')

    #se toma solo el numero de recvContactos ya que este devuelve una lista con nombre y numeros 'Carlos<04263002966>'
    patron = r'[0-9]{11}'
    devolverContactos = re.findall(patron, recvContactos)
    

    #Busca en mongodb el objetoId del usuario que inicio sesion
    objetoUsuarioId = buscarUsuarioId(usuario)

    ''' Busca en la base de datos "listas" los objetosId() de las listas que fueron selecioandas en el combobox
    del html'''
    devolverListasID = [f['_id'] for f in coleccionListas.find({'nombre_lista':{'$in':recvListas}, "usuario_id":objetoUsuarioId})]
    
    '''Buscos en la tabla "contactos" los objetosId() de las listas devueltas anteriormente y tomo solo los 
    contactos que pertencen a esas listas'''
    devolverListas = [f['telefonos'] for f in coleccionContactos.find({'listas_id':{'$in':devolverListasID}, "usuario_id":objetoUsuarioId})]
    
    numeros = devolverContactos + devolverListas
    return numeros 

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
bottle.run(host='0.0.0.0', port=8085)
