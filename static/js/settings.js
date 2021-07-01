function change_margin(){
    var height_header = document.getElementById('id1').scrollHeight;
    document.getElementById('id2').style.marginTop = String(height_header + 20) + 'px';
}

window.onresize = change_margin;
window.onload   = change_margin;