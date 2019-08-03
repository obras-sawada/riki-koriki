const default_image = './static/img/main.png'
const id_upload_btn = 'uploadBtn'
const id_select_btn = 'selectFile'
const id_upload_text = 'uploadText'
const id_file = 'file'
const id_image = 'image'
const id_default='id_default'
const id_selected='id_selected'
const id_textdef="id_textdef"

var textdef=null;


window.onload = function () {
    textdefText=$("#"+id_textdef).val()
    textdef=JSON.parse(textdefText)
    console.log(textdef)
}

$(function(){
    if (window.name != "re_load") {
        location.reload();
        window.name = "re_load";
    }else{
        window.name = "";
    }
});


function isSelected() {
    const file = document.getElementById(id_file)
    if (file.value === '') {
        $("#"+id_default).removeClass("hidden");
        $("#"+id_selected).addClass("hidden");
        $("#"+id_upload_btn).attr("disabled",true);
        $("#"+id_select_btn).addClass("main");
        $("#"+id_upload_text).text(textdef["select_image"]);
        $("#"+id_image).attr("src",null);
    } else {
        $("#"+id_default).addClass("hidden");
        $("#"+id_selected).removeClass("hidden");
        $("#"+id_upload_btn).attr("disabled",false);
        $("#"+id_select_btn).removeClass("main");
        $("#"+id_upload_text).text(textdef["reselect_image"]);
        $("#"+id_image).attr("src",window.URL.createObjectURL(file.files[0]));
    }
}

function disableSubmit() { 
    $("#"+id_upload_btn).attr("disabled",true);
    return true;
}
