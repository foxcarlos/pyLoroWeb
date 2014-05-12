# Import smtplib for the actual sending function
import smtplib

# Here are the email package modules we'll need
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

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
            #print(fila.strip())
            listaEmail.append(fila.strip())
        return listaEmail
    
    def enviar_email(self, destinatario, mensaje, imgAdjunta, remitente='congresoshospitalcoromoto@gmail.com', asunto='Congresos Hospital Coromoto'):
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

        archivo_imagen = open(imgAdjunta, 'rb')
        msgImage = MIMEImage(archivo_imagen.read())
        archivo_imagen.close()

        #Hemos de adjuntar la imagen en el content-id.
        #En el archivo html se debe hacer referencia al content-id
        #como fuente en el source de la imagen, por ejemplo:
        #<img src="cid:/nombre/de_la_ruta_entera/imagen.jpg">
        msgImage.add_header('Content-ID', '<' + imgAdjunta + '>')
        msg.attach(msgImage)

        # Autenticamos
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login("congresoshospitalcoromoto@gmail.com", "pdvserviciosdesalud")
    
        # Enviamos
        print(destinatario)
        mailServer.sendmail(remitente, destinatario, msg.as_string())
        # Cerramos conexion
        mailServer.close()
    
if __name__ == '__main__':
    app = correo()
    l = app.leerArchivo()
    #ll = ','.join(l)
    for destino in l:
        app.enviar_email(destino, 'Invitacion al II Congreso y III Jornadas Cientificas Integrales del Hospital Coromoto.  Si no puede ver la imagen haga click aqui: http://foxcarlos.no-ip.biz:8085/congreso.html', '/home/administrador/desarrollo/python/pyLoroWeb/congreso.jpg', 'pycondor@gmail.com', 'Invitacvion al II Congreso y III Jornadas Cientificas del Hospital Coromoto')
