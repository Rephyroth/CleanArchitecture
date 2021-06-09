
<?php
$conn = pg_connect("host=sheep port=5432 dbname=libreria user=admin password=123");
if(!$conn)
{
	echo "An error occurred.\n";
	exit;
}
 
$sql="SELECT id_book,title,isbn,author,publisher,genre,num_pages,year FROM book";
 
$result = pg_query($conn, $sql);
if(!$result)
{
	echo "An error occurred.\n";
	exit;
}

?>

<!DOCTYPE html >
<html >

<title>All books</title>

<h3>Search for a book by its ID</h3>

<table>

  <tr>
    <th>id Book</th>
    <th>title</th>
    <th>isbn</th>
    <th>author</th>
    <th>publisher</th>
    <th>genre</th>
    <th>Number of pages</th>
    <th>year</th>
</tr>

<?php

while ($row = pg_fetch_array($result))
	{
		echo "<tr>";
			echo "<td>".$row["id_book"]."</td>";
      echo "<td>".$row["title"]."</td>";
      echo "<td>".$row["isbn"]."</td>";
      echo "<td>".$row["author"]."</td>";
      echo "<td>".$row["publisher"]."</td>";
      echo "<td>".$row["genre"]."</td>";
      echo "<td>".$row["num_pages"]."</td>";
      echo "<td>".$row["year"]."</td>";
		echo "<tr>";
	}

?>

</table>

</html >
