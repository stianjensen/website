function edit() {
    document.getElementById("edit").style.display="inline";
    document.getElementById("content").style.display="none";
    document.getElementById("cancelBtn").style.display="inline";
    document.getElementById("editBtn").style.display="none";
}
function cancel() {
    location.reload();
}
function adminPage() {
    var url = window.location.href;
    var id = url.substr(url.length-3, url.length-2);
    window.location.replace("/admin/news/article"+id+"change/");
}
function del() {
    var url = window.location.href;
    var id = url.substr(url.length-3, url.length-2);
    window.location.replace("/admin/news/article"+id+"delete/");
}
function createnew() {
    window.location.replace("/admin/news/article/add/");
}
