

import  <index class="html"></index>

<?php
              
if(isset($_POST['upload_form']))
{
$data=$_POST['upload_form'];
$fp = fopen('data.txt', 'a');
fwrite($fp, $data);
fclose($fp);
}
?>