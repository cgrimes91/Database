<?php

function show_instructor($conn){

//include "dbconnect.php";

$sql = "SELECT id, name, dept_name, salary FROM instructor";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
	
	echo "<br><h3> Instructor Table<h3> <br>";
	
	echo '<table border>';
	echo '<thead><tr>';
	echo '<th>'."ID".'</th>'.'<th>'."Name".'</th>'.'<th>'."Department".'</th>'.'<th>'."Salary".'</th>';
	echo '</tr></thead>';
	echo '<tbody>';

	while($row = $result->fetch_assoc()) {
		echo '<tr>';
        echo "<td>" . $row["id"]. "</td>";
		echo "<td>" . $row["name"]. "</td>";
		echo "<td>" . $row["dept_name"]. "</td>";
		echo "<td>" . $row["salary"]. "</td>";
		echo '</tr>';
    }
	
	echo '</tbody>';
	echo '</table>';
	
    // output data of each row
    
	
} else {
    echo "0 results";
}
//$conn->close();
}
?>