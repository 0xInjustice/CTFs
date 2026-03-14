<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $data = isset($_POST["output"]) ? $_POST["output"] : "No data received";

    // Simpan ke file log
    file_put_contents("log.txt", base64_decode($data) . "\n", FILE_APPEND | LOCK_EX);

    echo "Data received!";
} else {
    echo "Invalid request method.";
}
?>
