<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
	<title>PyLoro SMS</title>
	<meta http-equiv="content-type" content="text/html;charset=utf-8" />
	<meta name="generator" content="Geany 1.22" />
</head>

<body>
	<h1> <p align="Center"> PyLoro SMS </p> </h1>
	<p align="Center"> Envio Gratis de SMS en Venezuela </p>	
	
	<FORM action="/smsenviar" method="POST">
	<table bgcolor="#F57171" border="0" cellpadding="1" cellspacing="1" align="center">
		
		<tr>
			<td align="center" bgcolor=#E03C3C colspan="2">
				Envio de SMS
			</td>
		</tr>

		<tr>
			<td align="left">
				Numero de Celular:
			</td>
			<td align="left">
				<input type="text" name="numero" value="" maxlength = 11 size="41"><br>
			</td>
		</tr>
		
		<tr>
			<td align="left">
				Mensaje a Enviar:
			</td>
			<td align="left">
				<textarea name="comentarios" rows="5" cols="40" value=""> </textarea>
			</td>
		</tr>
		<tr>
			<td align="center" colspan="2">
				<INPUT type="submit" value="Enviar">
				<INPUT type="reset">				
			</td>
		</tr>
		
	</table>
</body>

</html>
