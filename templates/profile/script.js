document.querySelector('.edit-info-button').addEventListener('click', function () {
    var firstName = prompt("Enter your first name:");
    document.getElementById('first-name').innerText = firstName;
    var lastName = prompt("Enter your last name:");
    document.getElementById('last-name').innerText = lastName;
    var email = prompt("Enter your email:");
    document.getElementById('email').innerText = email;
    var phone = prompt("Enter your phone number:");
    document.getElementById('phone').innerText = phone;
    var username = prompt("Enter your username:");
    document.getElementById('username').innerText = username;
});

document.querySelector('.upload-picture-button').addEventListener('click', function () {
    var input = document.getElementById('profile-picture-input');
    if (input.files & amp;& amp; input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
        document.getElementById('profile-picture').src = e.target.result;
    }
    reader.readAsDataURL(input.files[0]);
}
  });