document.addEventListener('DOMContentLoaded', function () {
    // Views global variables


    // Use buttons to toggle between views
    //document.querySelector('#').addEventListener('click', () => load_view_departments());
    //document.querySelector('#').addEventListener('click', () => load_view_clinic());

    document.querySelector('#departments').style.display = 'block';
    document.querySelector('#clinicview').style.display = 'block';


    get_clnics();
    searching();
    
});


function load_view_departments (){
    document.querySelector('#departments').style.display = 'block';
    document.querySelector('#clinicview').style.display = 'none';
}


function load_view_clinic (){
    document.querySelector('#departments').style.display = 'none';
    document.querySelector('#clinicview').style.display = 'block';
}


function get_clnics() {
    fetch(`/getclinics/`)
    .then(response => response.json())
    .then(clinics => {

        create_table(clinics);

    });
}


function searching(){
    $('#clinics-search').on('keyup', function(){
        var value = $(this).val()

        fetch(`/getclinics/`)
        .then(response => response.json())
        .then(clinics => {
            var data = search(value, clinics)

            create_table(data);

        });

    })

    function search(value, data) {
        var filterData = []

        for(var i = 0; i < data.length; i++){
            value = value.toLowerCase()
            var name = data[i].department_name.toLowerCase()

            if(name.includes(value)){
                filterData.push(data[i])
            }
        }
        return filterData
    }
}


function create_table(clinics){
    var table = document.querySelector('#clinrow');

    table.innerHTML = ''
    
    for (let i of Object.keys(clinics)) {
        const clinic = document.createElement('tr')
        clinic.classList.add('clinic')

        if(clinics[i].parent ){
            clinics[i].department_name = `-- ${clinics[i].department_name}`
        }

        clinic.innerHTML = `
            <td>${clinics[i].id}</td>
            <td><a href="">${clinics[i].department_name}</a></td>
            <td>${clinics[i].created_at}</td>
            <td>${clinics[i].updated_at}</td>
            <td><a href="/clinics/clinicpage/${clinics[i].id}" class="btn btn-block btn-primary btn-sm">See staff</a></td>
        `;

        table.append(clinic);
    };
}

