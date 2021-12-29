var newCoin = 0;
function showUsername(coin) {
        window.newCoin = coin;
    if (coin >= 1000) {
        window.newCoin -= 1000;
        console.log(window.newCoin)
        $('#username').prop("onclick", null).off("click");
        $('.usernameInput').css("display", "flex");
    }
}
function changeUsername(){
console.log($('#newUsername').val())
          $.ajax({
              type: 'POST',
              url: '/store/',
              data: {
                'newUsername':$('#newUsername').val(), 
                  'newCoin': window.newCoin,
                  'csrfmiddlewaretoken': CSRF_TOKEN,
              },
              success: function () {
                console.log("success");
              },
              error: function () {
                console.log("error");
              }
            })
    };
