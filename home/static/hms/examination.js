document.addEventListener('DOMContentLoaded', function () {
    // Views global variables
    var patienstview = document.querySelector('#patientsview');
    var examview = document.querySelector('#examview');

    // Use buttons to toggle between views
    document.querySelector('#cancel').addEventListener('click', () => view_appointmets());


    //document.querySelector('#examine-form').onsubmit = examine_patient;

    patienstview.style.display = 'block';
    examview.style.display = 'none';

    get_appointments();
    searching();
    
});

function view_appointmets (){
    document.querySelector('#patientsview').style.display = 'block';
    document.querySelector('#examview').style.display = 'none';
}


function examination_view (){
    document.querySelector('#patientsview').style.display = 'none';
    document.querySelector('#examview').style.display = 'block';

}


function get_appointments(){
    fetch(`get_treatment/`)
    .then(response => response.json())
    .then(appointmens => {

        create_table(appointmens);
    });
}


function searching(){
    $('#search-input').on('keyup', function(){
        var value = $(this).val()

        fetch(`get_treatment/`)
        .then(response => response.json())
        .then(appointmens => {
            var data = search(value, appointmens)

            create_table(data);

        });

    })

    function search(value, data) {
        var filterData = []

        for(var i = 0; i < data.length; i++){
            value = value.toLowerCase()
            var name = data[i].patient_name.toLowerCase()

            if(name.includes(value)){
                filterData.push(data[i])
            }
        }
        return filterData
    }
}


function create_table(appointmens){
    var table = document.querySelector('#patrow');

    table.innerHTML = ''
    
    for (let i of Object.keys(appointmens)) {
        const appointment = document.createElement('tr')
        appointment.classList.add('treatment')

        if(appointmens[i].patient_middlename === null){
            appointmens[i].patient_middlename = `-`
        }

        appointment.innerHTML = `
            <td>${appointmens[i].patient}</td>
            <td><a>${appointmens[i].patient_name}</a></td>
            <td><a>${appointmens[i].patient_surname}</a></td>
            <td><a>${appointmens[i].patient_middlename}</a></td>
            <td><a>${appointmens[i].patient_personal_ID}</a></td>
            <td>${appointmens[i].time} ${appointmens[i].date}</td>
            <td>${appointmens[i].scheduled_by_name} ${appointmens[i].scheduled_by_surname}</td>
            <td>${appointmens[i].appointed_at.slice(0,10)}, ${appointmens[i].appointed_at.slice(11,19)}</td>
            <td><button id="update" onclick="check_appointment(${appointmens[i].patient})" class="btn btn-block btn-primary btn-sm">Open</button></td>
            
        `;

        table.append(appointment);
    };
}

function check_appointment(id){
    examination_view();

    fetch(`get_single_patient/${id}`)
    .then(response => response.json())
    .then(patient => {

        for (let i of Object.keys(patient)) {
            
            document.querySelector('#name').innerHTML = patient[i].name;
            document.querySelector('#surname').innerHTML = patient[i].surname;
            document.querySelector('#middlename').innerHTML = patient[i].middlename;
            document.querySelector('#patid').innerHTML = patient[i].patient_ID;
            document.querySelector('#birth').innerHTML = patient[i].birthdate;
            document.querySelector('#phone').innerHTML = patient[i].phone;
            document.querySelector('#mobile').innerHTML = patient[i].mobile;
            document.querySelector('#email').innerHTML = patient[i].email;
            document.querySelector('#address').innerHTML = patient[i].address;
            document.querySelector('#city').innerHTML = patient[i].city;
            document.querySelector('#country').innerHTML = patient[i].country;

        };
    });

    fetch(`get_single_treatment/${id}`)
    .then(response => response.json())
    .then(treatment => {
        document.getElementById("examine-form").reset();

        for (let i of Object.keys(treatment)) {
            let reason = treatment[i].appointment_reason;
            let re_reason = treatment[i].re_apppoinment_reason;
            
            document.querySelector('#reason').value = `${reason}`;
            document.querySelector('#re-reason').value = `${re_reason}`;
            document.querySelector('#patient_id').value = treatment[i].patient;
        };
    });
}

