var onSignIn = function (googleUser) {
    var profile = googleUser.getBasicProfile();
    window.location.replace('/modules?usr=' + MD5(profile.getEmail()))
}

var onFailure = function (error) {
    console.log(error);
}

var signOut = function () {
    auth2.signOut().then(function () {
        window.location.replace('/logout')
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