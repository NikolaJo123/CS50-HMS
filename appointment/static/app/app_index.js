document.addEventListener('DOMContentLoaded', function () {
    // Views global variables
    var appointmentview = document.querySelector('#appointmentview');
    var appform = document.querySelector('#appform');
    var crtbtn = document.querySelector('#crtapp');


    // Use buttons to toggle between views
    document.querySelector('#crtapp').addEventListener('click', () => create_appointment());
    document.querySelector('#back').addEventListener('click', () => view_appointmets());
    document.querySelector('#back2').addEventListener('click', () => view_appointmets());
    document.querySelector('#del').addEventListener('click', () => delete_appointmet());

    document.querySelector('#appointment-form').onsubmit = make_appointmen;
    document.querySelector('#update-form').onsubmit = update;

    appointmentview.style.display = 'block';
    appform.style.display = 'none';
    crtbtn.style.display = 'block';
    document.querySelector('#updateform').style.display = 'none';

    get_patients();
    get_clinic();
    get_staff();
    show_app();
    searching();
});


function view_appointmets (){
    document.querySelector('#appointmentview').style.display = 'block';
    document.querySelector('#appform').style.display = 'none';
    document.querySelector('#updateform').style.display = 'none';
    document.querySelector('#crtapp').style.display = 'block';
    //location.reload()
}


function create_appointment (){
    document.querySelector('#appointmentview').style.display = 'none';
    document.querySelector('#appform').style.display = 'block';
    document.querySelector('#updateform').style.display = 'none';
    document.querySelector('#crtapp').style.display = 'none';

    document.getElementById("appointment-form").reset();
}


function appointment_update (){
    document.querySelector('#appointmentview').style.display = 'none';
    document.querySelector('#appform').style.display = 'none';
    document.querySelector('#updateform').style.display = 'block';
    document.querySelector('#crtapp').style.display = 'none';
}


function get_patients() {
    fetch(`patient/`)
    .then(response => response.json())
    .then(patients => {

        var select = document.querySelector('#selpat');
    
        for (let i of Object.keys(patients)) {
            const patient = document.createElement('option')
            patient.classList.add('patient')

            if(patients[i].middlename === null ){
                patients[i].middlename = ``
            }

            patient.innerHTML = `${patients[i].id} ${patients[i].name} ${patients[i].surname} ${patients[i].middlename}`;

            select.append(patient);
        };

    });
}


function get_clinic() {
    fetch(`clinic/`)
    .then(response => response.json())
    .then(clinics => {

        var select = document.querySelector('#selclnk');
    
        for (let i of Object.keys(clinics)) {
            const clinic = document.createElement('option')
            clinic.classList.add('clinic')

            if(clinics[i].parent ){
                clinics[i].department_name = `- ${clinics[i].department_name}`
            }

            clinic.innerHTML = `${clinics[i].id} ${clinics[i].department_name}`;

            select.append(clinic);
        };

    });
}


function get_staff() {
    fetch(`staff/`)
    .then(response => response.json())
    .then(doctors => {

        var select = document.querySelector('#seldoc');
    
        for (let i of Object.keys(doctors)) {
            const staff = document.createElement('option')
            staff.classList.add('staff')

            if(doctors[i].middlename === null ){
                doctors[i].middlename = ``
            }

            staff.innerHTML = `${doctors[i].user} ${doctors[i].employee_name} ${doctors[i].middlename} ${doctors[i].employee_surname}, ${doctors[i].speciality_name}`;

            select.append(staff);
        };

    });
}


function show_app(){
    fetch(`getappointments/`)
    .then(response => response.json())
    .then(appointmens => {

        create_table(appointmens);
    });
}


function searching(){
    $('#appsearch').on('keyup', function(){
        var value = $(this).val()

        fetch(`getappointments/`)
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
    var table = document.querySelector('#approw');

    table.innerHTML = ''
    
    for (let i of Object.keys(appointmens)) {
        const appointment = document.createElement('tr')
        appointment.classList.add('appointment')

        if(appointmens[i].re_apppoinment_reason === null || appointmens[i].re_apppoinment_reason ===''){
            appointmens[i].re_apppoinment_reason = `-`
        }

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
            <td>${appointmens[i].updated_at.slice(0,10)}, ${appointmens[i].updated_at.slice(11,19)}</td>
            <td><button id="update" onclick="update_appointment(${appointmens[i].patient})" class="btn btn-block btn-primary btn-sm">Open</button></td>
            
        `;

        table.append(appointment);
    };
}


function update_appointment(id){
    appointment_update();

    let selpat = document.querySelector('#selpat2');
    var seldoc = document.querySelector('#seldoc2');
    var selclnk = document.querySelector('#selclnk2');

    fetch(`getappointment/${id}`)
    .then(response => response.json())
    .then(appointment => {
        document.getElementById("appointment-form").reset();

        for (let i of Object.keys(appointment)) {

            selpat.innerHTML = `
                <option value=${appointment[i].patient} ${appointment[i].patient_name} ${appointment[i].patient_middlename} ${appointment[i].patient_surname}>
                ${appointment[i].patient} ${appointment[i].patient_name} ${appointment[i].patient_middlename} ${appointment[i].patient_surname}
                </option>`;
            selclnk.innerHTML = `
                <option value=${appointment[i].clinic} ${appointment[i].clinic_name}>
                ${appointment[i].clinic} ${appointment[i].clinic_name}
                </option>`;
            seldoc.innerHTML = `
                <option value=${appointment[i].doctor} ${appointment[i].doctor_name} ${appointment[i].doctor_surname}>
                ${appointment[i].doctor} ${appointment[i].doctor_name} ${appointment[i].doctor_surname}, ${appointment[i].clinic_name}
                </option>`;
            
            document.querySelector('#update-patient-id').value = appointment[i].patient_personal_ID;
            document.querySelector('#update-appointment-id').value = appointment[i].id;
            date = document.querySelector('#update-date').value = appointment[i].date;
            time = document.querySelector('#update-time').value = appointment[i].time;
            document.querySelector('#updateby').value = appointment[i].scheduled_by_name, appointment[i].scheduled_by_surname;
            appointment_reason = document.querySelector('#app-reason2').value = appointment[i].appointment_reason;
            re_apppoinment_reason = document.querySelector('#reapp-reason2').value = appointment[i].re_apppoinment_reason;
        };
    });
    //document.querySelector('#update-form').onsubmit = update;
}


function update() {
    let appointment_id = document.querySelector('#update-appointment-id').value;
    var patient = document.querySelector('#selpat2').value;
    var patient_ID = document.querySelector('#update-patient-id').value;
    var date = document.querySelector('#update-date').value;
    var time = document.querySelector('#update-time').value;
    var doctor = document.querySelector('#seldoc2').value;
    var clinic = document.querySelector('#selclnk2').value;
    var scheduled_by = document.querySelector('#updateby').value;
    var appointment_reason = document.querySelector('#app-reason2').value;
    var re_apppoinment_reason = document.querySelector('#reapp-reason2').value;

    var split_patient = patient.split(' ')
    var int = parseInt(split_patient[0]);
    var split_doctor = doctor.split(' ')
    var docint = parseInt(split_doctor[0]);
    var split_clinic = clinic.split(' ')
    var clnkint = parseInt(split_clinic[0]);
    var id_id = parseInt(appointment_id);

    fetch(`reappointment/`, {
        method: 'POST',
        body: JSON.stringify({
            id: id_id,
            patient: int,
            patient_personal_ID: patient_ID,
            date: date,
            time: time,
            doctor: docint,
            clinic: clnkint,
            scheduled_by: scheduled_by,
            appointment_reason: appointment_reason,
            re_apppoinment_reason: re_apppoinment_reason,
        })
    })
    view_appointmets()
    //location.reload();

    return false;
}


function delete_appointmet(){
    let appointment_id = document.querySelector('#update-appointment-id').value;
    var id_id = parseInt(appointment_id);

    fetch(`delete/${id_id}`, {
        method: 'POST',
        body: JSON.stringify({
            id: id_id,
        })
    })
    location.reload();

    return false;

}


function make_appointmen(){
    var patient = document.querySelector('#selpat').value;
    var patient_ID = document.querySelector('#schedule-patient-id').value;
    var date = document.querySelector('#schedule-date').value;
    var time = document.querySelector('#schedule-time').value;
    var doctor = document.querySelector('#seldoc').value;
    var clinic = document.querySelector('#selclnk').value;
    var scheduled_by = document.querySelector('#scheduleby').value;
    var appointment_reason = document.querySelector('#app-reason').value;
    var re_apppoinment_reason = document.querySelector('#reapp-reason').value;

    var split_patient = patient.split(' ')
    var int = parseInt(split_patient[0]);
    var split_doctor = doctor.split(' ')
    var docint = parseInt(split_doctor[0]);
    var split_clinic = clinic.split(' ')
    var clnkint = parseInt(split_clinic[0]);

    fetch('makeappointment/', {
        method: 'POST',
        body: JSON.stringify({
            patient: int,
            patient_personal_ID: patient_ID,
            date: date,
            time: time,
            doctor: docint,
            clinic: clnkint,
            scheduled_by: scheduled_by,
            appointment_reason: appointment_reason,
            re_apppoinment_reason: re_apppoinment_reason,
        })
    })

    document.getElementById("appointment-form").reset();

    view_appointmets();
    location.reload();

    /*$(document).ready(function() {
        $("#make").click(function() {
            $("#approw").load("/appointment");
        });
    });*/

    return false;
}

