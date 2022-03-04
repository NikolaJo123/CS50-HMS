document.addEventListener('DOMContentLoaded', function () {
    // Views global variables


    // Use buttons to toggle between views
    //document.querySelector('#').addEventListener('click', () => load_profile());
    document.querySelector('#edit').addEventListener('click', () => load_edit());

    document.querySelector('#profileview').style.display = 'block';
    document.querySelector('#editview').style.display = 'none';


    get_profile();
    
});


function load_edit(){
    document.querySelector('#profileview').style.display = 'none';
    document.querySelector('#editview').style.display = 'block';
}


function get_profile(){
    fetch(`/getprofile/`)
    .then(response => response.json())
    .then(profile => {

        for (let i of Object.keys(profile)) {

            //let vals = Object.values(profile[i])
            //console.log(vals)

            if (profile[i].name === null){
                profile[i].name = 'No record'
            }
            if (profile[i].middlename === null){
                profile[i].middlename = 'No record'
            }
            if (profile[i].employee_surname === null){
                profile[i].employee_surname = 'No record'
            }
            if (profile[i].role_title === null){
                profile[i].role_title = 'No record'
            }
            if (profile[i].speciality_name === null){
                profile[i].speciality_name = 'No record'
            }
            if (profile[i].cninic_name === null){
                profile[i].cninic_name = 'No record'
            }
            if (profile[i].personal_ID_number === null){
                profile[i].personal_ID_number = 'No record'
            }
            if (profile[i].email === null){
                profile[i].email = 'No record'
            }
            if (profile[i].phone === null){
                profile[i].phone = 'No record'
            }
            if (profile[i].mobile === null){
                profile[i].mobile = 'No record'
            }
            if (profile[i].address === null){
                profile[i].address = 'No record'
            }
            if (profile[i].city === null){
                profile[i].city = 'No record'
            }
            if (profile[i].country === null){
                profile[i].country = 'No record'
            }
            if (profile[i].birthdate === null){
                profile[i].birthdate = 'No record'
            }
            if (profile[i].user_image === null){
                profile[i].user_image = '/images/images/emptyuser.jpg"'
            }

            // Profile side info
            document.querySelector('#name').innerHTML = profile[i].employee_name;
            document.querySelector('#middlename').innerHTML = profile[i].middlename;
            document.querySelector('#surname').innerHTML = profile[i].employee_surname;
            document.querySelector('#title').innerHTML = profile[i].role_title;
            document.querySelector('#speciality').innerHTML = profile[i].speciality_name;
            document.querySelector('#clinic').innerHTML = profile[i].cninic_name;
            document.querySelector('#img').innerHTML = `<img class="profile-user-img img-fluid img-circle" src="${ profile[i].user_image }" alt="User profile picture">`;

            // User side info   
            document.querySelector('#personalID').innerHTML = profile[i].personal_ID_number;
            document.querySelector('#birth').innerHTML = profile[i].birthdate;
            // Contanct and Address info
            document.querySelector('#email').innerHTML = profile[i].email;
            document.querySelector('#phone').innerHTML = profile[i].phone;
            document.querySelector('#mobile').innerHTML = profile[i].mobile;
            document.querySelector('#address').innerHTML = profile[i].address;
            document.querySelector('#city').innerHTML = profile[i].city;
            document.querySelector('#country').innerHTML = profile[i].country;


        };

    });

}

