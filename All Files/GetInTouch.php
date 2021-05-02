<?php
    if (isset($_POST['submit'])){
        $phone=$_POST['phone'];
        $mail=$_POST['mail'];
        $name=$_POST['name'];
        $message=$_POST['message'];

        $mailto="achet";
        $headers= "From: My Website";
        $txt="You have received an E-mail from ".$name.".\n\n".$message;
        mail($mailto,$phone,$txt,$headers);
        header("Location: index.php?mailsent");
    }


    

?>