import smtplib
from email.mime.text import MIMEText

class correo:
    def __init__(self):
        import smtplib
        from email.mime.text import MIMEText        
        
    def leerArchivo(self):
        f = '/home/cgarcia/correos'
        fi = open(f)
        leido = fi.read()
        lista = leido.split(',')
        for fila in lista:
            print(fila.strip())    
    
    def enviar_email(self, destinatario, mensaje, imgAdjunta, remitente='pycondor@gmail.com', asunto='** Sistema de Monitoreo y Control Condor **'):
        '''
        El metodo enviar email recibe 3 parametros:
        Destinatario:uncorreo@gmail.com
        Mensaje:'Esto es una prueba de envio'
        Remitente:Si no se envia ningun remitente el toma por defecto pycondor@gma
        Asunto:si no se coloca ninguno el toma por defecto el pasado en el parametr
        '''
        
        # Creamos el mensaje
        msg = MIMEText(mensaje)
        
        # Conexin con el server
        msg['Subject'] = asunto
        msg['From'] = remitente
        msg['To'] = destinatario
    
        '''# Adjuntamos Imagen
        file = open(imgAdjunta, "rb")
        attach_image = MIMEImage(file.read())
        attach_image.add_header('Content-Disposition', 'attachment; filename = imgAdjunta')
        msg.attach(attach_image)'''
        
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
    #enviar_email('foxcarlos@gmail.com', 'Prueba', '/home/cgarcia/CONGRESO HOSPITAL COROMOTO AGOSTO 2014.JPG', 'pycondor@gmail.com', 'Enviando desde python')
    app = correo()
    app.enviar_email('foxcarlos@gmail.com', 'Prueba', '', 'pycondor@gmail.com', 'Enviando desde python')
    