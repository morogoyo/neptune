 <?php

 include("connection.php");

$array_to_encode=array();
$encoded;
$new_array;

function updateSiteInfoPage(){
	  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	 
	  global $con ;
	   
	  //$sql_select= "SELECT * FROM data_temp.PAX_LMSConsumer_Append_102016 WHERE PAX_UNIQUE_ID= 10";

	  		//$sql_select="UPDATE data_temp.Rene_test_hash SET * = IF('$date_value'='',"test",'$date_value')";


	  
	  $sql_select="SELECT  (IFNULL(prereq,'lms')) FROM data_temp.Rene_test_hash";
	 // $sql_select .= "SELECT * FROM data_temp.Rene_test_hash";
	  $result_select = $con->query($sql_select);
	  //$result_select = $con->multi_query($sql_select);
			
			if($result_select->num_rows > 0){
				$encoded = fopen("json.php","w");			          
			 
			 while($row = $result_select->fetch_assoc()){	
						
                	$array_to_encode[]= $row;				
			 		
			 		} 

			 
				
				}
					//changeData($array_to_encode);
              fwrite($encoded,'{"data":'.json_encode($array_to_encode).'}'); 

              return $array_to_encode;     
						                   
		
}

//function changeData($array){
					
					// 	$lms="lms";

					// 	//var_dump($array);
                      	
                      	
     //                       //$array = array("Peter"=>"35", "Ben"=>"37", "Joe"=> " ","pedro"=>NULL);
     //                       foreach($array as $x => $rows_name){                      			
                      	
     //              			//if (empty($x)) {// expression is true up to here
     //                       					//var_dump($array[$x]['age']);
     //                       			          // $rows_name==" "||isset($rows_name)||is_null($rows_name)||empty($rows_name)                 		
     //                       				if ($rows_name==" "||$rows_name==""||is_null($rows_name)||empty($rows_name)|| !isset($rows_name)) {
     //                       					//if ($x==""||is_null($x)||empty($x)|| !isset($x)) {
     //                       				echo "</br>".$x;
     //                       				//echo "</br>found empyt array value";
     //                       				$rows_name= 0;

                        	
     //                    				} else{echo "it failed";}           			
						 	
     //      //               				echo "<pre>";
					// 					 //var_dump($array);
					// 					// echo "</pre>";
					// 					// echo "<pre>";
					// 					// print_r($array);
					// 					// echo "</pre>";
					// 	 			// 	echo "</br>this did work</br>";
					// 	}

					// 	 //$new_array = $array;
					// 	//$test=fopen('test.php', "w");
					// 	////fwrite($test,var_dump($array)); 
					// 	// return $new_array;
					// }
						
				



     updateSiteInfoPage();
          
			   	 
             echo "</br> converter.php executed completely ";
             // var_dump($array_to_encode);

//////////////////////////////////  all test that have been done ///////////////////////////////////////////////////////////////////
     //////////////////////////////////////////////////////////////////////////////////////////////////////////////////			
			//testing for different way of making and filtering thru data 
                       // $email = $row['email'];
                       // $first = $row['first'];
                       // $last = $row['last'];
                       // $id = $row['consumer_id'];
                       // $sb = "{";
                       //  $eb = "}";
                      
                       // 	$push =array_push($array_to_encode,$sb.'"first" : "'.'"'.$first.'"','"last" : "'.'"'.$last.'"','"email" : "'.'"'.$email.'"'.$eb);
                       
                       


                   // showing the contenent of first array
			 			
			 			// 	echo '<pre>';
						// print_r($row);
						// echo '</pre>';
// ////////////////////////////////////////////////////////////////////////////////////////////////////////

						// $lms="lms";
      //                 	$count = count($row);
      //                 	$num = 0;
      //                      //$array_to_encode = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"","pedro"=>NULL);
      //                      foreach($row as $x => $rows_name){

      //                 			}$num=0;
      //                 	// for ($i=0; $i < $count ; $i++) { 
      //                 	// 		$num=$i;
      //                 	// }

      //                 			// is_null($rows_name) || $rows_name == null || $rows_name == NULL|| $rows_name == " " ||
                           
      //                      		if (!empty($x)) {// expression is true up to here
                           			                           		
      //                      				$array_to_encode[]= $row;

                        	
      //                   				}else

      //                   				//$row = "lms";
      //                   				$x="lms";
                           				
      //                      				$array_to_encode[]= $row[$x];
                           				
      //                      					echo "test";
                        				
                        				
      //                   			{
						 	
      //                   				echo "<pre>";
						// var_dump($array_to_encode);
						// echo "</pre>";
						// echo "<pre>";
						// print_r($array_to_encode);
						// echo "</pre>";
						//  	echo "</br>this did work</br>";
						// }

// }


 //write to file the encoded json array 
				 // this is the line making the json in to a string fwrite($encoded,'"{"data":'.json_encode($array_to_encode).'}"');
      //                 	$lms="lms";
      //                 	$count = count($array_to_encode);
      //                 	$num = 0;
      //                      //$array_to_encode = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"","pedro"=>NULL);
      //                      foreach($array_to_encode as $x => $rows_name){
      //                       // for($i=0;$i < $count;$i++){
      //                   		//if(!isset($x[$rows_name])){
      //                   		                        	//(!isset($array_to_encode[$x]) || $array_to_encode[$x] == "" || is_null($array_to_encode[$x])){
      //                   	    		echo "rene rules";
                        	
      //                   				// $array_to_encode[$x]=$rows_name;
                        	
      //                   				//$array_to_encode[$x]=$lms;
						// 				$num ++;
						// 				echo $num;


						// // } else{
						 	

						//  	echo "this didnt work";
						//  //}
                        	
						// // echo "<pre>";
						// // var_dump($array_to_encode);
						// // echo "</pre>";
						// // echo "<pre>";
						// // print_r($array_to_encode[0]);
						// // echo "</pre>";
						




?>