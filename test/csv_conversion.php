
<?php
// $json_file = fopen('json.php','r+');
// $read_json_file = fread($json_file,filesize('json.php'));

// //echo $read_json_file;//for testin purposes

// //if (empty($argv[1])) die("The json file name or URL is missed\n");
// $jsonFilename = $read_json_file;
// var_dump($jsonFilename);

// $json = file_get_contents($jsonFilename);
// $array = json_decode($json, true);
// $f = fopen('../file_test/result.csv', 'w+');
// $w =fwrite($f, "test writing");
// var_dump($json);
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//if (empty($argv[0])) die("The json file name or URL is missed\n");

$json_file = fopen('json.php','r');
$read_json_file = fread($json_file,filesize('json.php'));
var_dump("testing".$read_json_file);
$jsonFilename = $read_json_file;

$json = file_get_contents($read_json_file);
$array = json_decode($json, true);
var_dump($array);
$f = fopen('php://output', 'w');
$firstLineKeys = false;
foreach ($array as $x => $line)
{
    if (empty($firstLineKeys))
    {
        $firstLineKeys = array_keys($line);
        fputcsv($f, $firstLineKeys);
        $firstLineKeys = array_flip($firstLineKeys);
    }
    // Using array_merge is important to maintain the order of keys acording to the first element
    fputcsv($f, array_merge($firstLineKeys, $line));
}
?>

