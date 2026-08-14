<?php

$host = "localhost";
$user = "root";
$password = "";
$dbname = "mydb";

/* Connect to MySQL */
$conn = mysqli_connect($host, $user, $password);

if (!$conn) {
    die("Could not connect: " . mysqli_connect_error());
}

echo "Connected successfully<br>";

/* Create Database */
$sql = "CREATE DATABASE IF NOT EXISTS mydb";

if (mysqli_query($conn, $sql)) {
    echo "Database created successfully<br>";
} else {
    echo "Error creating database: " . mysqli_error($conn) . "<br>";
}

/* Select Database */
mysqli_select_db($conn, $dbname);

/* Create Employee Table */
$sql = "CREATE TABLE IF NOT EXISTS emp (
    id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    empsalary INT NOT NULL,
    PRIMARY KEY (id)
)";

if (mysqli_query($conn, $sql)) {
    echo "Table created successfully<br>";
} else {
    echo "Error creating table: " . mysqli_error($conn) . "<br>";
}

/* Insert Record */
$sql = "INSERT IGNORE INTO emp (id, name, empsalary)
        VALUES (312, 'RANA', 200000)";

if (mysqli_query($conn, $sql)) {
    echo "Record inserted successfully<br>";
} else {
    echo "Error inserting record: " . mysqli_error($conn) . "<br>";
}

/* Display Records - SELECT */
echo "<br><b>Records after INSERT:</b><br>";

$sql = "SELECT * FROM emp";
$result = mysqli_query($conn, $sql);

while ($row = mysqli_fetch_assoc($result)) {
    echo "ID: " . $row["id"] .
         " | Name: " . $row["name"] .
         " | Salary: " . $row["empsalary"] . "<br>";
}

/* UPDATE */
$sql = "UPDATE emp SET empsalary = 9000000 WHERE id = 312";

if (mysqli_query($conn, $sql)) {
    echo "<br>Record updated successfully<br>";
} else {
    echo "Error updating record: " . mysqli_error($conn) . "<br>";
}

/* Display after UPDATE */
echo "<br><b>Records after UPDATE:</b><br>";

$sql = "SELECT * FROM emp";
$result = mysqli_query($conn, $sql);

while ($row = mysqli_fetch_assoc($result)) {
    echo "ID: " . $row["id"] .
         " | Name: " . $row["name"] .
         " | Salary: " . $row["empsalary"] . "<br>";
}

/* DELETE */
$sql = "DELETE FROM emp WHERE id = 312";

if (mysqli_query($conn, $sql)) {
    echo "<br>Record deleted successfully<br>";
} else {
    echo "Error deleting record: " . mysqli_error($conn) . "<br>";
}

/* Display after DELETE */
echo "<br><b>Records after DELETE:</b><br>";

$sql = "SELECT * FROM emp";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) == 0) {
    echo "No records found";
} else {
    while ($row = mysqli_fetch_assoc($result)) {
        echo "ID: " . $row["id"] .
             " | Name: " . $row["name"] .
             " | Salary: " . $row["empsalary"] . "<br>";
    }
}

/* Close Connection */
mysqli_close($conn);

?>