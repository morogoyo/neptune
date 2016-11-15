 <?php

 include("connection.php");

function updateSiteInfoPage(){
	  
	  global $con ;
	  $sql_select= "SELECT * FROM data_temp.PAX_LMSConsumer_Append_102016";
	  $result_select = $con->query($sql_select);
			
			if($result_select->num_rows > 0){
			   $encoded = fopen("json.php","w");
			         $array_to_encode=array();  
			 
			 while($row = $result_select->fetch_assoc()){		    
				
			//testing for different way of making and filtering thru data 
                       //$email = $row['EMAIL'];
                       // $first = $row['first'];
                       // $last = $row['last'];
                       // $id = $row['consumer_id'];
                       // $sb = "{";
                       //  $eb = "}";
                     
                       // 	$push =array_push($array_to_encode,$sb.'"first" : "'.'"'.$first.'"','"last" : "'.'"'.$last.'"','"email" : "'.'"'.$email.'"'.$eb);


						 $array_to_encode []= $row;
				
			 } 
				 //write to file the envoded json array 
				 // this is the line making the json in to a string fwrite($encoded,'"{"data":'.json_encode($array_to_encode).'}"');
			       fwrite($encoded,'{"data":'.json_encode($array_to_encode).'}');
				 //confirm creation
		  }
	  
	  
	  }
             echo "</br> converter.php executed completely  ";

     updateSiteInfoPage();

?>