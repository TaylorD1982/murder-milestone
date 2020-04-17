// Javascript for the contact form

function sendMail(contactForm) {
    emailjs.send("gmail", "football_site", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "query": contactForm.query.value
    })
    .then(
        function(response) {
            console.log("Good", response);
        },
        function(error) {
            console.log("bad", error);
        }
    );
    return false;
}