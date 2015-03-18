****************************************************************************************************
* Script en VFP que permite enviar un SMS via web usando Web Service de pyLoro SMS
* Creado Por: Carlos Alberto Garcia Diaz
* Fecha: 17/03/2015
****************************************************************************************************

oHTTP = CREATEOBJECT("WinHttp.WinHttpRequest.5.1")

*Solo en caso de estar detras de un proxy
oHTTP.SetProxy(2, "10.121.6.12:8080", "")

oHTTP.Open("POST", "http://foxcarlos.no-ip.biz/mensaje", .F.)
oHTTP.SetRequestHeader("User-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)")
oHTTP.SetRequestHeader("Content-type", "application/x-www-form-urlencoded")

numeroTelf = '04263002966'
mensaje = 'Hola desde VFP'
repetir = 5

*oHTTP.Send("var1=Hola desde VFP&var2=04140681394")
TEXT TO parametroEnviar TEXTMERGE NOSHOW 
	var1=<<mensaje>>&var2=<<numeroTelf>>
ENDTEXT 

FOR veces = 1 TO repetir
	oHTTP.Send(parametroEnviar)
	?veces
	? oHTTP.Status
	? oHTTP.StatusText
	? oHTTP.ResponseText
ENDFOR