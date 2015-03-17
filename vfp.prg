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
oHTTP.Send("var1=Hola desde VFP&var2=04140681394")
? oHTTP.Status
? oHTTP.StatusText
