var newCoin = 0;
function showUsername(coin) {
        window.newCoin = coin;
    if (coin >= 1000) {
        // window.newCoin -= 1000;
        $('#username').prop("onclick", null).off("click");
        $('.usernameInput').css("display", "flex");
    }
}
function changeUsername(){
          $.ajax({
              type: 'POST',
              url: '/store/',
              data: {
                'code': 'username',
                'newUsername':$('#newUsername').val(), 
                  // 'newCoin': window.newCoin,
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
function checkDarkmode(coin)
{
  if (coin >= 100) {
    $.ajax({
      type: 'POST',
      url: '/store/',
      data: {
        'code': 'darkMode',
        'csrfmiddlewaretoken': CSRF_TOKEN,
      },
      success: function () {
        console.log("success");
      },
      error: function () {
        console.log("error");
      }
    })
  }
};

function changeavatar(coin)
{
  if (coin >= 1000) {
    $.ajax({
      type: 'POST',
      url: '/store/',
      data: {
        'code': 'avatar',
        'csrfmiddlewaretoken': CSRF_TOKEN,
      },
      success: function () {
        console.log("success");
      },
      error: function () {
        console.log("error");
      }
    })
  }
};

function doubleCoin(coin,price) {
  if (coin >= price) {
    $.ajax({
      type: 'POST',
      url: '/store/',
      data: {
        'code': 'doubleCoin',
        'mode': price,
        'csrfmiddlewaretoken': CSRF_TOKEN,
      },
      success: function () {
        console.log("success");
      },
      error: function () {
        console.log("error");
      }
    })
  }
}