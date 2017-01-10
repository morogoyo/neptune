<?php 
// this connection file is for 192.168.22.4
define( "HOST", "192.168.22.4");
define( "USERNAME", "felix");
define( "DATABASE", "data_temp");
define( "PASSWORD", "*");
global $con;
$con = new mysqli(HOST,USERNAME,PASSWORD,DATABASE);
if (!$con){
	
	echo $con->error;
	}else{
		echo "connected successfuly";
		
		}
?>
