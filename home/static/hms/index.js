document.addEventListener('DOMContentLoaded', function () {

    // Use buttons to toggle between views

    test_fetch();
});


function test_fetch() {
    fetch(`https://api.exchangerate.host/latest`)
    .then(response => response.json())
    .then(profile => {
        console.log(profile)
    });
}