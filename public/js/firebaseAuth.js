function checkIfLoggedIn() {
    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
            console.log('User signed in.');
            console.log(user);
            // document.getElementById('signin').setAttribute('style', 'display: none; visibility: hidden');
            // document.getElementById('signout').setAttribute('style', 'display: inline-block; visibility: visible');
        } else {
            console.log('User not signed in.');
            document.getElementById('signin').setAttribute('style', 'display: inline-block; visibility: visible');
            document.getElementById('signout').setAttribute('style', 'display: none; visibility: hidden');
        }
    });
}
checkIfLoggedIn();

function signOut() {
    firebase.auth().signOut();

    window.location.replace('/');
}

function signInWithGoogle() {
    var googleAuthProvider = new firebase.auth.GoogleAuthProvider;

    firebase.auth().signInWithPopup(googleAuthProvider)
            .then( function(data) {
                console.log(data);
                checkIfLoggedIn();
                window.location.replace('/kearch');
            })
            .catch( function(error) {
                console.log(error);
            });
            
}

function createUserWithEmailAndPassword() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('pwd').value;
    firebase.auth().createUserWithEmailAndPassword(email, password)
        .then(function(user) {
            console.log(user);
            window.location.replace('/');
        })
        .catch(function(error) {
            alert(error.message);
            console.log(error);
        });
}

function signInWithEmailAndPassword() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('pwd').value;
    firebase.auth().signInWithEmailAndPassword(email, password)
        .then(function(user) {
            console.log(user);
            window.location.replace('/kearch');
        })
        .catch(function(error) {
            alert(error.message);
            console.log(error);
        });
}