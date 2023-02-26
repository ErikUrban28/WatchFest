let loginLoginError = document.getElementById('login-login-error');
let loginPasswordError = document.getElementById('login-password-error');
let registerLoginError = document.getElementById('register-login-error');
let registerEmailError = document.getElementById('register-email-error');
let registerPasswordError1 = document.getElementById('register-password1-error');
let registerPasswordError2 = document.getElementById('register-password2-error');
let registerSubmit = document.getElementById('register-submit-error');
let loginSubmit = document.getElementById('login-submit-error');

function validateLoginLogin() {
    let login = document.getElementById('login-login').value;
    if (login.length === 0) {
        loginLoginError.innerHTML = 'Login musi byt vyplneny';
        return false;
    }
    if (login.length < 3) {
        loginLoginError.innerHTML = 'Login musi mat aspon 3 charaktery';
        return false;
    }
    if (!(/^[A-Za-z0-9]*$/.test(login))) {
        loginLoginError.innerHTML = 'Login moze obsahovat iba pismena a cisla';
        return false;
    }
    if (login.length >= 30) {
        loginLoginError.innerHTML = 'Login musi mat menej ako 30 znakov';
        return false;
    }
    loginLoginError.innerHTML = 'Validne';
    loginLoginError.style.color = "green";
    return true;
}

function validateRegisterLogin() {
    let login = document.getElementById('register-login').value;
    registerLoginError.style.color = "red";
    if (login.length === 0) {
        registerLoginError.innerHTML = 'Login musi byt vyplneny';
        return false;
    }
    if (login.length < 3) {
        registerLoginError.innerHTML = 'Login musi mat aspon 3 charaktery';
        return false;
    }
    if (!(/^[A-Za-z0-9]*$/.test(login))) {
        registerLoginError.innerHTML = 'Login moze obsahovat iba pismena a cisla';
        return false;
    }
    if (login.length >= 30) {
        registerLoginError.innerHTML = 'Login musi mat menej ako 30 znakov';
        return false;
    }
    registerLoginError.innerHTML = 'Validne';
    registerLoginError.style.color = "green";
    return true;
}

function validateEmail() {
    let email = document.getElementById('register-email').value;
    registerEmailError.style.color = "red";
    if (email.length === 0) {
        registerEmailError.innerHTML = 'Email musi byt vyplneny';
        return false;
    }
    if (!(/^[A-Za-z0-9_]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(email))) {
        registerEmailError.innerHTML = 'Neplany Email';
        return false;
    }

    if (email.length > 50) {
        registerEmailError.innerHTML = 'Email musi mat menej ako 50 znakov';
        return false;
    }
    registerEmailError.innerHTML = 'Validne';
    registerEmailError.style.color = "green";
    return true;
}

function validatePasswordLogin() {
    let pass = document.getElementById('login-password').value;
    loginPasswordError.style.color = "red";
    if (pass.length === 0) {
        loginPasswordError.innerHTML = 'Heslo musi byt vyplnene';
        return false;
    }
    if (pass.length < 6) {
        loginPasswordError.innerHTML = 'Heslo musi mat viac ako 5 znakov';
        return false;
    }
    if (pass.length >= 35) {
        loginPasswordError.innerHTML = 'Heslo musi mat menej ako 35 znakov';
        return false;
    }
    loginPasswordError.innerHTML = 'Validne';
    loginPasswordError.style.color = "green";
    return true;
}

function validatePassword1Register() {
    let pass = document.getElementById('register-password1').value;
    registerPasswordError1.style.color = "red";
    if (pass.length === 0) {
        registerPasswordError1.innerHTML = 'Heslo musi byt vyplnene';
        return false;
    }
    if (pass.length < 6) {
        registerPasswordError1.innerHTML = 'Heslo musi mat viac ako 5 znakov';
        return false;
    }
    if (pass.length >= 35) {
        registerPasswordError1.innerHTML = 'Heslo musi mat menej ako 35 znakov';
        return false;
    }
    registerPasswordError1.innerHTML = 'Validne';
    registerPasswordError1.style.color = "green";
    return true;
}

function validatePassword2Register() {
    let pass = document.getElementById('register-password2').value;
    registerPasswordError2.style.color = "red";
    if (pass.length === 0) {
        registerPasswordError2.innerHTML = 'Zopakovane Heslo musi byt vyplnene';
        return false;
    }
    if (pass.length < 6) {
        registerPasswordError2.innerHTML = 'Zopakovane Heslo musi mat viac ako 5 znakov';
        return false;
    }
    if (pass.length >= 35) {
        registerPasswordError2.innerHTML = 'Zopakovane Heslo musi mat menej ako 35 znakov';
        return false;
    }
    registerPasswordError2.innerHTML = 'Validne';
    registerPasswordError2.style.color = "green";
    return true;
}

function validateRegisterSubmit() {
    if (!validatePassword1Register() || !validateRegisterLogin() || !validateEmail() || !validatePassword2Register()) {
        registerSubmit.style.display = 'inline';
        registerSubmit.innerHTML = "Chybne vyplnene udaje";
        setTimeout(function () {
            registerSubmit.style.display = 'none';
        }, 500)
        return false;
    }
}

function validateLoginSubmit() {
    if (!validateLoginLogin() || !validatePasswordLogin()) {
        loginSubmit.style.display = 'inline';
        loginSubmit.innerHTML = "Chybne vyplnene udaje";
        setTimeout(function () {
            loginSubmit.style.display = 'none';
        }, 500)
        return false;
    }
}



