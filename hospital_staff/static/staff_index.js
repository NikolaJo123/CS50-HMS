document.addEventListener('DOMContentLoaded', function () {

    // Use buttons to toggle between views
    document.querySelector('#bck').addEventListener('click', () => load_view_professions());
    //document.querySelector('#seeall').addEventListener('click', () => load_view_profession());


    document.querySelector('#professionsview').style.display = 'block';
    document.querySelector('#professionview').style.display = 'none';


    get_professions();
    //get_employees();
    searching();
    
});


function load_view_professions (){
    document.querySelector('#professionsview').style.display = 'block';
    document.querySelector('#professionview').style.display = 'none';
}


function load_view_profession (){
    document.querySelector('#professionsview').style.display = 'none';
    document.querySelector('#professionview').style.display = 'block';
}


function get_professions() {
    fetch(`/getpersonal/`)
    .then(response => response.json())
    .then(members => {

        create_table(members);

    });
}


function get_employees() {
    load_view_profession();

    fetch(`/employees/`)
    .then(response => response.json())
    .then(members => {

        create_proffesion_table(members);

    });
}


function get_profession(id) {
    load_view_profession();

    fetch(`/getprofession/${id}`)
    .then(response => response.json())
    .then(prof => {

        create_proffesion_table(prof);

    });
}


function searching(){
    $('#staff-search').on('keyup', function(){
        var value = $(this).val()

        fetch(`/getpersonal/`)
        .then(response => response.json())
        .then(members => {
            var data = search(value, members)

            create_table(data);

        });

    })

    $('#member-search').on('keyup', function(){
        var value = $(this).val()

        fetch(`/employees/`)
        .then(response => response.json())
        .then(members => {
            var data = memsearch(value, members)

            create_proffesion_table(data);

        });

    })

    function search(value, data) {
        var filterData = []

        for(var i = 0; i < data.length; i++){
            value = value.toLowerCase()
            var name = data[i].title.toLowerCase()

            if(name.includes(value)){
                filterData.push(data[i])
            }
        }
        return filterData
    }

    function memsearch(value, data) {
        var filterData = []

        for(var i = 0; i < data.length; i++){
            value = value.toLowerCase()
            var name = data[i].employee_name.toLowerCase()

            if(name.includes(value)){
                filterData.push(data[i])
            }
        }
        return filterData
    }
}


function create_table(members){
    var table = document.querySelector('#memberrow');

    table.innerHTML = ''
    
    for (let i of Object.keys(members)) {
        const member = document.createElement('tr')
        member.classList.add('member')

        if(members[i].parent ){
            members[i].title = `-- ${members[i].title}`
        }

        member.innerHTML = `
            <td>${members[i].id}</td>
            <td class="titlecolor"><a>${members[i].title}</a></td>
            <td>${members[i].created_at}</td>
            <td>${members[i].updated_at}</td>
            <td id="member${members[i].id}"><button id="staff" onclick="get_profession(${members[i].id})" class="btn btn-block btn-primary btn-sm">See staff</button></td>
        `;
        table.append(member);
        //member.addEventListener('click', () => get_profession(members[i].id));
    };
}


function create_proffesion_table(profs){
    var table = document.querySelector('#membersrow');

    table.innerHTML = ''
    
    for (let i of Object.keys(profs)) {
        const member = document.createElement('tr')
        member.classList.add('member')

        if(profs[i].middlename === null ){
            profs[i].middlename = '-'
        }

        if(profs[i].status === 'Ac' ){
            profs[i].status = 'active'
        }


        member.innerHTML = `
            <td>${profs[i].user}</td>
            <td>${profs[i].employee_name}</td>
            <td>${profs[i].employee_surname}</td>
            <td>${profs[i].middlename}</td>
            <td>${profs[i].personal_ID_number}</td>
            <td>${profs[i].birthdate}</td>
            <td>${profs[i].role_title}</td>
            <td>${profs[i].speciality_name}</td>
            <td>${profs[i].status}</td>
            <td>${profs[i].employed}</td>
            <td>${profs[i].updated_info}</td>
            <td><img src="${profs[i].user_image}" style="width: 50px; height: auto;" alt="personel picture"></td>
        `;

        table.append(member);
    };
}

