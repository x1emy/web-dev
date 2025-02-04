let user = prompt("Who is there?: ", '');

if (user =='admin'){
    let pass = prompt("Password?");

    if (pass == 'TheMaster'){
        alert('Welcome!');
    }
    else if (pass == 'Other'){
        alert('Wrong password');
    }
    else if (pass == 'Cancel' || pass == null){
        alert('Canceled');
    }
}
else if (user == 'Cancel'){
    alert('Canceled');
}
else {
    alert('I dont know you');
}