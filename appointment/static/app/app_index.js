document.addEventListener('DOMContentLoaded', function () {
    // Views global variables
    var appointmentview = document.querySelector('#appointmentview');
    var appform = document.querySelector('#appform');
    var crtbtn = document.querySelector('#crtapp');


    // Use buttons to toggle between views
    document.querySelector('#crtapp').addEventListener('click', () => create_appointment());
    document.querySelector('#back').addEventListener('click', () => view_appointmets());

    appointmentview.style.display = 'block';
    appform.style.display = 'none';
    crtbtn.style.display = 'block';

});


function view_appointmets (){
    document.querySelector('#appointmentview').style.display = 'block';
    document.querySelector('#appform').style.display = 'none';
    document.querySelector('#crtapp').style.display = 'block';
}


function create_appointment (){
    document.querySelector('#appointmentview').style.display = 'none';
    document.querySelector('#appform').style.display = 'block';
    document.querySelector('#crtapp').style.display = 'none';
}

