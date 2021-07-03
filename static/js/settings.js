function change_margin(){
    var height_header = document.getElementById('id1').scrollHeight;
    document.getElementById('id2').style.marginTop = String(height_header + 20) + 'px';
}

window.onresize = change_margin;
function online_list(id_online, id_line){
    var server_online = document.getElementById(id_online).innerText;
    var curent_online = server_online.split('/')[0];
    var maximal_online = server_online.split('/')[1];
    var online_procent = Number(curent_online) / Number(maximal_online) * 100;
    var block = document.getElementById(id_line);
    block.style.background = `linear-gradient(to right, #33ffff ${online_procent}%, transparent ${online_procent}%)`;
}

window.onload = online_list('online1', 'line1')