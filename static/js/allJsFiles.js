

$(document).ready(function(){

    $("#fast").click(function(){
      $(".fas").addClass("fast-spin");
      $(".fas").removeClass("slow-spin");

    });
    $("#slow").click(function(){
      $(".fas").addClass("slow-spin");
      $(".fas").removeClass("fast-spin");
    });

});