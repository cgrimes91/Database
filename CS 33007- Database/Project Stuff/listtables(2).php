<?php
//Step1
 $servername = "localhost:3306";
$username = "root";
$password = "root";
$dbname = "university";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
         
 if(! $conn ){
               die('Could not connect: ' . mysqli_error($conn));
  }
?>

<html>
 <head>
 </head>
 <body>
 <h1>List of tables in my database:</h1>

<?php
//Step2
$query = "show tables;";
mysqli_query($conn, $query) or die('Error querying database.');

//Step3
$result = mysqli_query($conn, $query);

while ($row = mysqli_fetch_array($result)) {
 echo $row[0].'<br />';
}
//Step 4
mysqli_close($conn);
?>

</body>
</html>