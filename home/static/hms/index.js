document.addEventListener('DOMContentLoaded', function () {

    // Views global variables
    var inbox = document.querySelector('#dashboardview')
    var patienstview = document.querySelector('#patientsview')
    var registerview = document.querySelector('#registerview')


    // Use buttons to toggle between views
    document.querySelector('#dashboard').addEventListener('click', () => load_dashboard());
    document.querySelector('#registration').addEventListener('click', () => load_register_patients());
    document.querySelector('#patientslist').addEventListener('click', () => load_view_patients());

    document.querySelector('#register-form').onsubmit = register_patient;

    inbox.style.display = 'block';
    patienstview.style.display = 'none';
    registerview.style.display = 'none';

    get_patients();
});


function load_dashboard (){
    document.querySelector('#dashboardview').style.display = 'block';
    document.querySelector('#patientsview').style.display = 'none';
    document.querySelector('#registerview').style.display = 'none';
}


function load_register_patients (){
    document.querySelector('#dashboardview').style.display = 'none';
    document.querySelector('#patientsview').style.display = 'none';
    document.querySelector('#registerview').style.display = 'block';
}


function load_view_patients (){
    document.querySelector('#dashboardview').style.display = 'none';
    document.querySelector('#patientsview').style.display = 'block';
    document.querySelector('#registerview').style.display = 'none';    
}


function register_patient (){
    var name = document.querySelector('#register-name').value;
    var surname = document.querySelector('#register-surname').value;
    var middlename = document.querySelector('#register-middlename').value;
    var patient_ID = document.querySelector('#register-patient-id').value;
    var birthdate = document.querySelector('#register-birthdate').value;
    var phone = document.querySelector('#register-phone').value;
    var mobile = document.querySelector('#register-mobile').value;
    var email = document.querySelector('#register-email').value;
    var address = document.querySelector('#register-address').value;
    var city = document.querySelector('#register-city').value;
    var country = document.querySelector('#register-country').value;


    fetch('/register_patient/', {
        method: 'POST',
        body: JSON.stringify({
            name: name,
            surname: surname,
            middlename: middlename,
            patient_ID: patient_ID,
            birthdate: birthdate,
            phone: phone,
            mobile: mobile,
            email: email,
            address: address,
            city: city,
            country: country,
        })
    })

    document.getElementById("register-form").reset();

    return false;
}


function get_patients() {
    fetch(`patient/`)
    .then(response => response.json())
    .then(patients => {
        console.log(patients)

        const patient = document.createElement('div')

        for (let i of Object.keys(patients)) {
            const patient = document.createElement('div')
            patient.classList.add('patient')

            patient.innerHTML = `
                <div>${patients[i].name}</div>
                <div>${patients[i].surname}</div>
                <div>${patients[i].middlename}</div>
                <div>${patients[i].patient_ID}</div>
                <div>${patients[i].birthdate}</div>
                <div>${patients[i].phone}</div>
                <div>${patients[i].mobile}</div>
                <div>${patients[i].email}</div>
                <div>${patients[i].address}</div>
                <div>${patients[i].city}</div>
                <div>${patients[i].country}</div>
            `;
            const temp = document.getElementById("patientsview");
            temp.insertBefore(patient, temp.childNodes[0]);

            document.querySelector('#patientsview').append(patient);
        };
    });
}