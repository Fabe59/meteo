/*$("#add-form").submit(function () {
    var city = $("#input-city").val()
    console.log(city)
})*/

/*function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
console.log(csrftoken)*/

$('#add-form').submit(function(event){
    var city = $("#input-city").val()
    const csrftoken = Cookies.get('csrftoken');
    console.log(city)
    console.log(csrftoken)

    event.preventDefault(),

    $.ajax({
        type: 'POST',
        headers: {
           'X-CSRF-Token' : csrftoken,
        },
        url : "/weather/add/",
        data : {
            'req' : city,
        },
        success:function(){
            alert("Tout est OK!");
        }
    })
})
