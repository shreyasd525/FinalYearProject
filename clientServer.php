<?php
header("Access-Control-Allow-Origin: *");

$site="https://www.google.com";
#$site=$_POST['url'];

$html = file_get_contents($site);
#echo $html;
$bytes=file_put_contents('newmarkupnew5google.txt', $html);
#echo("current dir CS.PHP");

$userName="shreyas";
$userPassword="user123";

$input = $userName.'|'.$userPassword.'\n';
$output = shell_exec($input);

$a=exec('python3 test.py '.$site.' 2>&1 ');


echo $a;
?>
