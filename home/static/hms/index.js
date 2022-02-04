document.addEventListener('DOMContentLoaded', function () {

    // Use buttons to toggle between views

    test_fetch();
});


function test_fetch() {
    //fetch(`https://api.exchangerate.host/latest`)
    fetch(`patient/`)
    .then(response => response.json())
    .then(patients => {
        console.log(patients)

        for (let i of Object.keys(patients)) {
            const patient = document.createElement('div')
            patient.classList.add('patient')

            patient.innerHTML = `
                <div>${patients[i].name}</div>
                <div>${patients[i].surname}</div>
                <div>${patients[i].middlename}</div>
                <div>${patients[i].patient_ID}</div>
                <div>${patients[i].age}</div>
                <div>${patients[i].phone}</div>
                <div>${patients[i].mobile}</div>
                <div>${patients[i].email}</div>
                <div>${patients[i].address}</div>
                <div>${patients[i].city}</div>
                <div>${patients[i].country}</div>
            `;

            document.querySelector('#patientview').append(patient);
        };
    });
}