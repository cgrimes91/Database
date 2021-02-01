<html>

   <head>
      <title>Add New Record in MySQL Database</title>
   </head>

   <body>
      <?php
	  
		require("tableshow.php");
		require("dbconnect.php");
	  
         if(isset($_POST['add'])) {
            
            if(! get_magic_quotes_gpc() ) {
               $i_name = addslashes ($_POST['i_name']);
               $i_dept = addslashes ($_POST['i_dept']);
            } else {
               $i_name = $_POST['i_name'];
               $i_dept = $_POST['i_dept'];
            }

            $i_ID = $_POST['i_ID'];
            $i_salary = $_POST['i_salary'];
			
			echo " <br> Instructor table before insertion <br>";
			show_instructor($conn);
   
            $sql = "INSERT INTO instructor ".
               "(ID,name, dept_name, salary) "."VALUES ".
               "('$i_ID','$i_name','$i_dept', '$i_salary')";
            
			//mysqli_select_db($conn,'university');
            $retval = mysqli_query($conn, $sql);
         
            if(! $retval ) {
               die('Could not enter data: ' . mysqli_error($conn));
            }
         
            echo "Entered data successfully\n";
			
			echo " <br> Instructor table after insertion <br>";
			show_instructor($conn);
			
            mysqli_close($conn);
         } 
		 else if(isset($_POST['show'])){
			 
			 show_instructor($conn);
		 }	 
		 
		 else {
      ?>
     <p>Enter Instructor information for insertion <br> </p>
      <form method = "post" action = "<?php $_PHP_SELF ?>">
         <table width = "600" border = "0" cellspacing = "1" cellpadding = "2">
            <tr>
               <td width = "250">ID</td>
               <td>
                  <input name = "i_ID" type = "text" id = "i_ID">
               </td>
            </tr>
         
            <tr>
               <td width = "250">Name</td>
               <td>
                  <input name = "i_name" type = "text" id = "i_name">
               </td>
            </tr>
         
            <tr>
               <td width = "250">Department</td>
               <td>
                  <input name = "i_dept" type = "text" id = "i_dept">
               </td>
            </tr>
      
            <tr>
               <td width = "250"> Salary</td>
               <td> <input name="i_salary" type= "text" id = "i_salary"> </td>
            </tr>
            <tr>
               <td width = "250"></td>
               <td> </td>
            </tr>
         
            <tr>
               <td width = "250"> </td>
               <td>
                  <input name = "add" type = "submit" id = "add"  value = "insert">
               </td>
            </tr>
			<tr>
			<br>
			 
			 
				<td> Click the buttion to see instructor table: <input name = "show" type = "submit" id = "show"  value = "show_instructors"></td>
				
			</tr>
         </table>
   
	  
   <?php
      }
   ?>
   </body>
</html>