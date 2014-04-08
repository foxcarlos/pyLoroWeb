<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="description" content="">
<meta name="viewport" content="width=device-width">
<link rel="stylesheet" href="/static/css/bootstrap.min.css">
<link rel="stylesheet" href="/static/css/style.css">
<link href='http://fonts.googleapis.com/css?family=Cabin+Condensed:400,500,600,700' rel='stylesheet' type='text/css'>

<style>

</style>
<title>Inicio de Sesion</title>
</head>

<body>
<div class="container">
    <div class="row">
		<div class="col-md-4 col-md-offset-4">
    		<div class="panel panel-personal">
			  	<div class="panel-heading">
			    	<h3 class="panel-title">Inicio de Sesión<span class="Three-Dee pull-right" >PyLoroWeb</span></h3>
			 	</div>
			  	<div class="panel-body">
			    	<form accept-charset="UTF-8"  role="form" action="/" method="post">
                    <fieldset>
			    	  	<div class="input-group form-group">
                        <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
			    		    <input class="form-control" placeholder="Usuario" name="usu_form" maxlength="16" type="text">
			    		</div>
                        
			    		<div class="input-group form-group">
                        <span class="input-group-addon"><i class="glyphicon glyphicon-lock"></i></span>
			    			<input class="form-control" placeholder="Clave" name="pass_form" maxlength="16" type="password" value="">
			    		</div>
                        <div class="row">
			    		<div class="col-xs-offset-0 col-xs-12">
			    	    	<a href="olvido.html" class="pull-right">
			    	    		¿Has olvidado tu contraseña?
			    	    	</a>
                         </div>
			    	    </div>
			    		<div class="row boton">
                        
                        <div class="col-xs-12 ">
                        <input class="btn btn-personal" type="submit" value="Entrar"> &nbsp;o <a href="/registro" class="align-vertical">Regístrarte</a>
                        </div>
                        
                        </div>
			    	</fieldset>
			      	</form>
			    </div>
			</div>
		</div>
	</div>
</div>
</body>
</html>
