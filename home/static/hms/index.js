document.addEventListener('DOMContentLoaded', function () {
    // Views global variables
    var patienstview = document.querySelector('#patientsview');
    var registerview = document.querySelector('#registerview');
    var archied = document.querySelector('#archivedview');


    // Use buttons to toggle between views
    document.querySelector('#registration').addEventListener('click', () => load_register_patients());
    document.querySelector('#patientslist').addEventListener('click', () => load_view_patients());
    document.querySelector('#archivedpatiets').addEventListener('click', () => load_archived_patients());

    document.querySelector('#register-form').onsubmit = register_patient;

    patienstview.style.display = 'block';
    registerview.style.display = 'none';
    archied.style.display = 'none';

    get_patients();
    searching();
    
});


function load_register_patients (){
    document.querySelector('#patientsview').style.display = 'none';
    document.querySelector('#registerview').style.display = 'block';
    document.querySelector('#archivedview').style.display = 'none';
}


function load_view_patients (){
    document.querySelector('#patientsview').style.display = 'block';
    document.querySelector('#registerview').style.display = 'none';
    document.querySelector('#archivedview').style.display = 'none';    
}


function load_archived_patients (){
    document.querySelector('#patientsview').style.display = 'none';
    document.querySelector('#registerview').style.display = 'none';
    document.querySelector('#archivedview').style.display = 'block';    
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


    fetch('register_patient/', {
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

        create_table(patients);
        archived_table(patients);

    });
}


function searching(){
    $('#search-input').on('keyup', function(){
        var value = $(this).val()

        fetch(`patient/`)
        .then(response => response.json())
        .then(patients => {
            var data = search(value, patients)

            create_table(data);

        });

    })

    $('#archived_search').on('keyup', function(){
        var value = $(this).val()

        fetch(`patient/`)
        .then(response => response.json())
        .then(patients => {
            var data = search(value, patients)

            archived_table(data);

        });

    })

    function search(value, data) {
        var filterData = []

        for(var i = 0; i < data.length; i++){
            value = value.toLowerCase()
            var name = data[i].name.toLowerCase()

            if(name.includes(value)){
                filterData.push(data[i])
            }
        }
        return filterData
    }
}


function create_table(patients){
    var table = document.querySelector('#patrow');

    table.innerHTML = ''
    
    for (let i of Object.keys(patients)) {
        const patient = document.createElement('tr')
        patient.classList.add('patient')

        if(patients[i].middlename === null ){
            patients[i].middlename = '-'
        }

        patient.innerHTML = `
            <td><div class="form-check">
            <input type="checkbox" class="form-check-input" id="box${patients[i].id}">
            </div></td>
            <td>${patients[i].id}</td>
            <td><a href="/">${patients[i].name}</a></td>
            <td>${patients[i].surname}</td>
            <td>${patients[i].middlename}</td>
            <td>${patients[i].patient_ID}</td>
            <td>${patients[i].birthdate}</td>
            <td>${patients[i].phone}</td>
            <td>${patients[i].mobile}</td>
            <td>${patients[i].email}</td>
            <td>${patients[i].address}</td>
            <td>${patients[i].city}</td>
            <td>${patients[i].country}</td>
        `;

        table.append(patient);
    };
}


function archived_table(patients){
    var arch_table = document.querySelector('#archived');

    arch_table.innerHTML = ''
    
    for (let i of Object.keys(patients)) {
        const patient = document.createElement('tr')
        patient.classList.add('archivedpatient')

        if(patients[i].middlename === null ){
            patients[i].middlename = '-'
        }

        patient.innerHTML = `
            <td><div class="form-check">
            <input type="checkbox" class="form-check-input" id="box${patients[i].id}">
            </div></td>
            <td>${patients[i].id}</td>
            <td><a href="/">${patients[i].name}</a></td>
            <td>${patients[i].surname}</td>
            <td>${patients[i].middlename}</td>
            <td>${patients[i].patient_ID}</td>
            <td>${patients[i].birthdate}</td>
            <td>${patients[i].phone}</td>
            <td>${patients[i].mobile}</td>
            <td>${patients[i].email}</td>
            <td>${patients[i].address}</td>
            <td>${patients[i].city}</td>
            <td>${patients[i].country}</td>
        `;

        arch_table.append(patient);
    };
}

