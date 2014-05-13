# Import smtplib for the actual sending function
import smtplib

# Here are the email package modules we'll need
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import sys

class correo:
    def __init__(self):
        '''ru'''

    def leerArchivo(self):
        listaEmail = []
        f = '/home/administrador/desarrollo/python/pyLoroWeb/correos'
        fi = open(f)
        leido = fi.read()
        lista = leido.split(',')
        for fila in lista:
            listaEmail.append(fila.strip())
        return listaEmail
    
    def enviar_email(self, remitente, destinatario, asunto,  mensaje, adjunto, clave, server, puerto):
        '''
        El metodo enviar email recibe 3 parametros:
        Destinatario:uncorreo@gmail.com
        Mensaje:'Esto es una prueba de envio'
        Remitente:Si no se envia ningun remitente el toma por defecto pycondor@gma
        Asunto:si no se coloca ninguno el toma por defecto el pasado en el parametr
        MEMultipart()'''

        #COMMASPACE = ', '
        
        # Create the container (outer) email message.
        msg = MIMEMultipart()
        msg['Subject'] = asunto
        # me == the sender's email address
        # family = the list of all recipients' email addresses
        msg['From'] = remitente
        msg['To'] = destinatario  # COMMASPACE.join(destinatario)
        msg.preamble = mensaje

        #Creamos el cuerpo del mensaje
        msg.attach(MIMEText(mensaje))

        # Autenticamos
        mailServer = smtplib.SMTP(server, puerto)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(remitente, clave)
    
        # Enviamos
        print(destinatario)
        try:
            mailServer.sendmail(remitente, destinatario, msg.as_string())
        except:
            print(destinatario, sys.exc_info()[1])

        # Cerramos conexion
        mailServer.close()
    
if __name__ == '__main__':
    app = correo()
    l = app.leerArchivo()
    
    correoH = ['hotmail', 'congresoshospitalcoromoto@outlook.com', 'docencia2014', 'smtp.live.com', '587']
    correoG = ['gmail', 'congresoshospitalcoromoto@gmail.com', 'pdvserviciosdesalud', 'smtp.gmail.com', '587']
    
    mensaje = 'Invitacion al II Congreso y III Jornadas Cientificas Integrales del Hospital Coromoto.\
            Si no puede ver la imagen haga click aqui: http://foxcarlos.no-ip.biz:8085/congreso'
    adjunto = '/home/administrador/desarrollo/python/pyLoroWeb/congreso.jpg'
    asunto = 'Invitacvion al II Congreso y III Jornadas Cientificas del Hospital Coromoto'

    for destino in l:
        #anavr8486@gmail.com
        #remitente, destino, asunto,  mensaje, adjunto, clave, server, puerto

        app.enviar_email(destino, 'Invitacion al II Congreso y III Jornadas Cientificas Integrales del Hospital Coromoto.  Si no puede ver la imagen haga click aqui: http://foxcarlos.no-ip.biz:8085/congreso', '/home/administrador/desarrollo/python/pyLoroWeb/congreso.jpg', 'congresoshospitalcoromoto@outlook.com', 'Invitacvion al II Congreso y III Jornadas Cientificas del Hospital Coromoto')
