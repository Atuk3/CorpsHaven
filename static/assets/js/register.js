// function validateForm() {
//     // Email validation
//     var email = document.forms["myForm"]["email"].value;
//     if (!email.endsWith('@gmail.com') && !email.endsWith('@yahoo.com') && !email.endsWith('@outlook.com')) {
//         alert("Email must be either @gmail.com, @yahoo.com, or @outlook.com");
//         return false;
//     }

//     // Phone number validation
//     var phoneNumber = document.forms["myForm"]["phonenumber"].value;
//     if (phoneNumber.length !== 11 || isNaN(phoneNumber)) {
//         alert("Phone number must be 11 digits.");
//         return false;
//     }

//     // Service year validation
//     var year = document.forms["myForm"]["year"].value;
//     var currentYear = new Date().getFullYear();
//     if (year < currentYear - 1 || year > currentYear) {
//         alert("Service year must be between " + (currentYear - 1) + " and " + currentYear);
//         return false;
//     }

//     // Password validation
//     var password = document.forms["myForm"]["psw"].value;
//     var confirmPassword = document.forms["myForm"]["psw-repeat"].value;
//     if (password.length < 8) {
//         alert("Password must be at least 8 characters long.");
//         return false;
//     }
//     if (password != confirmPassword) {
//         alert("Passwords do not match.");
//         return false;
//     }

//     // Account type validation
//     var accountTypeChecked = false;
//     var accountTypes = document.getElementsByName("account_type");
//     for (var i = 0; i < accountTypes.length; i++) {
//         if (accountTypes[i].checked) {
//             accountTypeChecked = true;
//             break;
//         }
//     }
//     if (!accountTypeChecked) {
//         alert("Please select an account type.");
//         return false;
//     }

    // // If all checks pass, submit the form to the /login route
    // document.getElementById("myForm").action = "/login";
    // return true; // Form is valid
   
}