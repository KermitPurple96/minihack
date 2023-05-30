// funcion para esconder/mostrar la contraseña del login
function contraseña() {
    let input = document.getElementById("password");
    let valorinput = input.type
    if (valorinput == 'password') {
        input.type = 'text';
    }
    if (valorinput == 'text') {
        input.type = 'password';
    }
}
// funcion para esconder/mostrar la primera contraseña del Signin
function contraseña1() {
    let input = document.getElementById("Contrasena");
    let valorinput1 = input.type
    if (valorinput1 == 'password') {
        input.type = 'text';
    }
    if (valorinput1 == 'text') {
        input.type = 'password';
    }
}
// funcion para esconder/mostrar la segunda contraseña del Signin
function contraseña2() {
    let input = document.getElementById("Contrasena2");
    let valorinput2 = input.type
    if (valorinput2 == 'password') {
        input.type = 'text';
    }
    if (valorinput2 == 'text') {
        input.type = 'password';
    }
}

// limpieza de notificaciones de errores por si vuelve el usuario a cometer errores
document.getElementById('crearcuenta').addEventListener('click', filtro);
// funcion general
function filtro() {
    // filtro para nombre, usa un mensaje de error ya creado, para el resto de errores crearemos nuevos <p>
    document.getElementById('error').style.display = 'none';
    // capturo el valor del formulario que quiero filtrar
    let valorinput = document.getElementById('nombre').value;
    // si es menor de 20 cambio el display y añado el texto aunque esto ultimo podria estar ya hecho
    if (valorinput.length > 20) {
        document.getElementById('error').innerHTML = 'El nombre no puede tener más de 20 carcateres';
        document.getElementById('error').style.display = 'block';
    }
    else if (valorinput.length < 3) {
        document.getElementById('error').innerHTML = 'Nombre debe tener almenos 3 caracteres';
        document.getElementById('error').style.display = 'block';
    }
    // filtro para el apellido, a partir de aqui los <p> de los errores se crean
    else {
        let valorapellido1 = document.getElementById('apellido1').value;

        if (valorapellido1.length > 20) {
            // creo un elemento <p>
            let errornuevo = document.createElement('p');
            // le atribuyo el id predefinido "error"
            errornuevo.setAttribute('id', 'error');
            // cambio el display a block para que no sea "none"
            errornuevo.style.display = 'block';
            // añado texto en funcion del error
            errornuevo.innerHTML = 'El primer apellido no puede tener más de 20 caracteres';
            // le digo donde debe incluir esta nueva <p>
            document.getElementById('izq').appendChild(errornuevo);
            // limpio el value del input que ha dado error
            document.getElementById('apellido1').value = '';
            // hago focus al input que ha dado error para ahorrar clicks y facilitar
            document.getElementById('apellido1').focus();

        }
        else if (valorapellido1.length < 3) {
            let errornuevo = document.createElement('p');

            errornuevo.setAttribute('id', 'error');
            errornuevo.style.display = 'block';
            errornuevo.innerHTML = 'El primer apellido no puede tener menos de 3 caracteres';
            document.getElementById('izq').appendChild(errornuevo);
            document.getElementById('apellido1').value = '';
            document.getElementById('apellido1').focus();
        }
        // filtro para apellido 2
        else {

            let valorapellido2 = document.getElementById('apellido2').value;

            if (valorapellido2.length > 20) {
                let errorapellido2 = document.createElement('p');

                errorapellido2.setAttribute('id', 'error');
                errorapellido2.style.display = 'block';
                errorapellido2.innerHTML = 'El segundo apellido no puede tener más de 20 caracteres';
                document.getElementById('izq').appendChild(errorapellido2);
                document.getElementById('apellido2').value = '';
                document.getElementById('apellido2').focus();

            }
            else if (valorapellido2.length < 7) {
                let errorapellido2 = document.createElement('p');

                errorapellido2.setAttribute('id', 'error');
                errorapellido2.style.display = 'block';
                errorapellido2.innerHTML = 'El segundo apellido no puede tener menos de 7 caracteres';
                document.getElementById('izq').appendChild(errorapellido2);
                document.getElementById('apellido2').value = '';
                document.getElementById('apellido2').focus();
            }
            // filtro correo, requiere de un @
            else {
                let valorcorreo = document.getElementById('correo').value;

                console.log(valorcorreo);
                if (!(valorcorreo.includes("@"))) {
                    let errorcorreo = document.createElement('p');

                    errorcorreo.setAttribute('id', 'error');
                    errorcorreo.style.display = 'block';
                    errorcorreo.innerHTML = 'El correo debe contener @';
                    document.getElementById('izq').appendChild(errorcorreo);
                    document.getElementById('correo').value = '';
                    document.getElementById('correo').focus();
                }
                // filtro para el telefono, error en la linea 120 no consigo que detecte letras
                else {
                    let valornum = document.getElementById('telefono').value;

                    console.log(valornum);
                    if (valornum.includes('/[A-Za-z]/g')) {
                        let errornum = document.createElement('p');

                        errornum.setAttribute('id', 'error');
                        errornum.style.display = 'block';
                        errornum.innerHTML = 'El telefono no puede incluir letras';
                        document.getElementById('izq').appendChild(errornum);
                        document.getElementById('telefono').value = '';
                        document.getElementById('telefono').focus();
                    }
                    // filtro para el nombre de usuario
                    else {
                        let valoruser = document.getElementById('user').value;

                        if (valoruser.length > 20) {
                            let erroruser = document.createElement('p');

                            erroruser.setAttribute('id', 'error');
                            erroruser.style.display = 'block';
                            erroruser.innerHTML = 'El nombre de usuario no puede tener más de 20 caracteres';
                            document.getElementById('izq').appendChild(erroruser);
                            document.getElementById('user').value = '';
                            document.getElementById('user').focus();

                        }
                        else if (valoruser.length < 3) {
                            let erroruser = document.createElement('p');

                            erroruser.setAttribute('id', 'error');
                            erroruser.style.display = 'block';
                            erroruser.innerHTML = 'El nombre de usuario no puede tener menos de 3 caracteres';
                            document.getElementById('izq').appendChild(erroruser);
                            document.getElementById('user').value = '';
                            document.getElementById('user').focus();
                        }
                        // filtro para contraseña, debe incluir numeros en la linea 179 pero no funciona
                        else {
                            let contra = document.getElementById('Contrasena').value;

                            if (contra.length < 7) {
                                let errorcontra = document.createElement('p');

                                errorcontra.setAttribute('id', 'error');
                                errorcontra.style.display = 'block';
                                errorcontra.innerHTML = 'La contraseña debe tener almenos 7 caracteres';
                                document.getElementById('izq').appendChild(errorcontra);
                                document.getElementById('contra').value = '';
                                document.getElementById('contra').focus();
                            }
                            if (contra.length > 20) {
                                let errorcontra = document.createElement('p');

                                errorcontra.setAttribute('id', 'error');
                                errorcontra.style.display = 'block';
                                errorcontra.innerHTML = 'La contraseña debe tener menos de 20 caracteres';
                                document.getElementById('izq').appendChild(errorcontra);
                                document.getElementById('contra').value = '';
                                document.getElementById('contra').focus();
                            }
                            if (!valornum.includes('/[0-9]/g')) {
                                let errorcontra = document.createElement('p');

                                errorcontra.setAttribute('id', 'error');
                                errorcontra.style.display = 'block';
                                errorcontra.innerHTML = 'La contraseña debe contener un numero';
                                document.getElementById('izq').appendChild(errorcontra);
                                document.getElementById('contra').value = '';
                                document.getElementById('contra').focus();
                            }
                            // filtro para revisar que las contraseñas coinciden
                            else {
                                let contra2 = document.getElementById('Contrasena2').value;
                                if (contra2 != contra) {
                                    errorcontra2.setAttribute('id', 'error');
                                    errorcontra2.style.display = 'block';
                                    errorcontra2.innerHTML = 'La contraseña debe contener un numero';
                                    document.getElementById('izq').appendChild(errorcontra2);
                                    document.getElementById('Contrasena2').value = '';
                                    document.getElementById('Contrasena2').focus();
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

