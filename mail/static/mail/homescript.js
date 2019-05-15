
jQuery(document).ready(function() {
  for (let i = 1; i < $('.mail').length+1; i++) {
    jQuery('#reveal_' + i).hide();
    jQuery('.rv_button_' + i).click(function(e){
      $("[id^='reveal_']").each(function(i,v){
        $(this).hide();
      });
      e.preventDefault();
      jQuery('#reveal_' + i).show();
      });
  }
});

function createLinks(div, text) {
    var target = document.getElementById(div).getElementsByClassName("msg")[0];
    var exp = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig;
    var reps = text.replace(exp,"<a href='$1'>$1</a>");
    document.getElementById(div).getElementsByClassName("msg")[0].innerHTML = reps;
    document.title = "PayloadMail"
}

function loadFile(ctype, name, enc, data){
  var linkSource = "data:" + ctype + ";" + enc + "," + data;
  var downloadLink = document.createElement("a");
  downloadLink.href = linkSource;
  downloadLink.download = name;
  downloadLink.click();
}