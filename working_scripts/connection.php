<?php 
// this connection file is for 192.168.22.4
define( "HOST", "*");
define( "USERNAME", "*");
define( "DATABASE", "*");
define( "PASSWORD", "*");
global $con;
$con = new mysqli(HOST,USERNAME,PASSWORD,DATABASE);
if (!$con){
	
	echo $con->error;
	}else{
		echo "connected successfuly";
		
		}
?>
