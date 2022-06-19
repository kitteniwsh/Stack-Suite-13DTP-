$(document).ready(function() {
    var a = $(".xor .input #a");
    var b = $('.xor .input #b');
    var xor = () => {
        let alen = a.val().length, blen = b.val().length;
        if (alen == 0 || blen == 0) {
            $(".xor .output").html("XOR output:");
            return;
        }
        let res = "";
        for (let i = 0; i < Math.min(a.val().length, b.val().length); i++) {
            res += (parseInt(a.val()[i], 16) ^ parseInt(b.val()[i], 16)).toString(16);
        }
        $(".xor .output").html("XOR output:  " + res);
    };
    a.on("input change", xor);
    b.on("input change", xor);
    $("textarea").each(function () {
        this.setAttribute("style", "height:" + (this.scrollHeight) + "px;overflow-y:hidden;");
    }).on("input", function () {
        this.style.height = "auto";
        this.style.height = (this.scrollHeight) + "px";
    });
})

$(document).ready(function() {
    var a = $(".hexx .input #a");
    var g = ""
    var hexx = () => {
        if(a.val()[0] == "0" && a.val()[1] == "x"){
          res= parseInt(a.val());
          g = "Decimal output: ";
        }else{
          res = parseInt(a.val()).toString(16);
          g = "Hexadecimal output: ";

        }
        if(res.toString() == "NaN"){
          $(".hexx .output").html("Malformed input");
        }else{
          $(".hexx .output").html(g+res);
        }

    };
    a.on("input change", hexx);
    $("textarea").each(function () {
        this.setAttribute("style", "height:" + (this.scrollHeight) + "px;overflow-y:hidden;");
    }).on("input", function () {
        this.style.height = "auto";
        this.style.height = (this.scrollHeight) + "px";
    });
})
$(document).ready(function() {
    var a = $(".b64 .input #a");
    var g = "";
    var hexx = () => {
        if(a.val()[0] == "~"){
          res= btoa(unescape(encodeURIComponent( a.val().substring(1))));
          g = "Base64 encoded: ";
        }else{
          res= atob(a.val());
          g = "Plaintext output: ";

        }

          $(".b64 .output").html(g + res);


    };
    a.on("input change", hexx);
    $("textarea").each(function () {
        this.setAttribute("style", "height:" + (this.scrollHeight) + "px;overflow-y:hidden;");
    }).on("input", function () {
        this.style.height = "auto";
        this.style.height = (this.scrollHeight) + "px";
    });
})
