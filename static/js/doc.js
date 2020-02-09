$(document).ready(function () {
    var rendererMD = new marked.Renderer();
    marked.setOptions({
      renderer: rendererMD,
      gfm: true,
      tables: true,
      breaks: true,
      pedantic: false,
      sanitize: false,
      smartLists: true,
      smartypants: false
    });
    marked.setOptions({
        highlight: function (code) {
        return hljs.highlightAuto(code).value;
      }
    });

    $.get("/docs/"+name+".md",function (response) {
        document.getElementById("content").innerHTML = marked(response);
        $("#footer").show();
    })
    });