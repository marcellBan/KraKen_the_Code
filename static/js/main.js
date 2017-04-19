var onSignIn = function (googleUser) {
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
}

var signInCallback = function (authResult) {
    //debugger;
    // ajax back to server
    if(authResult["code"]){
        console.log('code: ' + authResult["code"])
    }
}

var onFailure = function (error) {
    console.log(error);
}

var signOut = function () {
    auth2.signOut().then(function () {
        console.log('User signed out.');
    });
}

var start = function () {
    gapi.load('auth2', function () {
        auth2 = gapi.auth2.init({
            client_id: '95366867191-gjj1d97guk88o6lj23338lma223hrk31.apps.googleusercontent.com'
        });
    });
    gapi.signin2.render('my-signin2', {
        'scope': 'profile email',
        'width': 40,
        'height': 40,
        'longtitle': false,
        'theme': 'dark',
        'onsuccess': onSignIn,
        'onfailure': onFailure
    });
}