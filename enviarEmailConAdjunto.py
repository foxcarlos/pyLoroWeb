import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

class correo:
    def __init__(self):
        '''ru'''

    def leerArchivo(self):
        listaEmail = []
        f = '/home/administradorcgarcia/desarrollo/python/pyLoroWeb/correos'
        fi = open(f)
        leido = fi.read()
        lista = leido.split(',')
        for fila in lista:
            #print(fila.strip())
            listaEmail.append(fila.strip())
        return listaEmail
    
    def enviar_email(self, destinatario, mensaje, imgAdjunta, remitente='pycondor@gmail.com', asunto='** Sistema de Monitoreo y Control Condor **'):
        '''
        El metodo enviar email recibe 3 parametros:
        Destinatario:uncorreo@gmail.com
        Mensaje:'Esto es una prueba de envio'
        Remitente:Si no se envia ningun remitente el toma por defecto pycondor@gma
        Asunto:si no se coloca ninguno el toma por defecto el pasado en el parametr
        MEMultipart()'''
        
        # Creamos el mensaje
        msg = MIMEText(mensaje)
        msg = MIMEMultipart('alternative')  # MIMEText(mensaje)
        
        # Conexin con el server
        msg['Subject'] = asunto
        msg['From'] = remitente
        msg['To'] = destinatario
    
        '''# Adjuntamos Imagen
        file = open(imgAdjunta, "rb")
        attach_image = MIMEImage(file.read())
        attach_image.add_header('Content-Disposition', 'attachment; filename = imgAdjunta')
        msg.attach(attach_image)'''

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
        mailServer.login("pycondor@gmail.com", "shc21152115")
    
        # Enviamos
        mailServer.sendmail(remitente, destinatario, \
        msg.as_string())
        # Cerramos conexion
        mailServer.close()
    
if __name__ == '__main__':
    app = correo()
    l = app.leerArchivo()
    ll = ','.join(l)
    app.enviar_email(ll, 'Prueba', '/home/administradorcgarcia/desarrollo/python/pyLoroWeb/congreso.jpg', 'pycondor@gmail.com', 'Enviando desde python')
    
