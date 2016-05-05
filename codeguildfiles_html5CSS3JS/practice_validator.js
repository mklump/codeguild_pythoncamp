/*
    Python Coding Bootcamp (pdxcodeguild)
    Code File for practice_validator.js
    by: Matthew James K on 5/3/2016
 */
"use strict"

/*
 * This helper fuction registers the txtFullName handler using "First Last" format exactly.
 */
function validateTxtFullName() {
    $("#txtFullName").on("input", null, this, validateFullName);
}

/*
 * This helper funtion registers the txtAge handler using YYYY-MM-DD number format exactly.
 */
function validateTxtAge() {
    $("#txtAge").on("input", null, this, validateAge);
}

/*
 * This helper funtion validates the txtPhone input box using 555-555-5555 number format exactly.
 */
function validateTxtPhone() {
    $("#txtPhone").on("input", null, this, validatePhone);
}

/*
 * This function is the delegate callback for validateTxtFullName, and establishes if the #txtFullName
 * control has either valid user input either true or false.
 * This is an output creation function, not data transform.
 * @param {Event} reference access to object members
 * @returns {Boolean} true if the input validation succeeded, otherwise false
 */
function validateFullName(event) { // TODO: This function is doing 3 steps in one, and not modular enough for unit testing. If unit testing this, then will need to re-do.
    var isValid = new Boolean();
    var txt = null;
    if (null !== event)
        txt = event.target.value
    else
        txt = $("#txtFullName")[0].value;
    var matchArray = txt.match("([a-zA-Z].+)[ ]([a-zA-Z].+)");
    if (null === matchArray || "" === matchArray[0] || "" === matchArray[1]) {
        $("#txtFullName").attr("class", "txtWarning");
        $("#formStatus").text("Full name is not valid.");
        isValid = false;
    } else {
        $("#txtFullName").attr("class", "statusOkay");
        $("#formStatus").text("");
        isValid = true;
    }
    return isValid;
}

/*
 * This function is the delegate callback for validateTxtAge, and establishes if the #txtAge
 * control has either valid user input either true or false.
 * This is an output creation function, not data transform.
 * @param {Event} reference access to object members
 * @returns {Boolean} true if the input validation succeeded, otherwise false
 */
function validateAge(event) { // TODO: This function is doing 3 steps in one, and not modular enough for unit testing. If unit testing this, then will need to re-do.
    var isValid = new Boolean();
    var txt = null;
    if (null !== event)
        txt = event.target.value
    else
        txt = $("#txtAge")[0].value;
    var matchArray = txt.match("([0-9]{4})[-]([0-9]{2})[-]([0-9]{2})");
    if (null === matchArray || "" === matchArray[0] || "" === matchArray[1]) {
        $("#txtAge").attr("class", "txtWarning");
        $("#formStatus").text("Age is not valid.");
        isValid = false;
    } else {
        $("#txtAge").attr("class", "statusOkay");
        $("#formStatus").text("");
        isValid = true;
    }
    return isValid;
}

/*
 * This function is the delegate callback for validateTxtPhone, and establishes if the #txtPhone
 * control has either valid user input either true or false.
 * This is an output creation function, not data transform.
 * @param {Event>} reference access to object members
 * @returns {Boolean} true if the input validation succeeded, otherwise false
 */
function validatePhone(event) { // TODO: This function is doing 3 steps in one, and not modular enough for unit testing. If unit testing this, then will need to re-do.
    var isValid = new Boolean();
    var txt = null;
    if (null !== event)
        txt = event.target.value
    else
        txt = $("#txtPhone")[0].value;
    var matchArray = txt.match("([0-9]{3})[-]([0-9]{3})[-]([0-9]{4})");
    if (null === matchArray || "" === matchArray[0] || "" === matchArray[1]) {
        $("#txtPhone").attr("class", "txtWarning");
        $("#formStatus").text("Phone is not valid.");
        isValid = false;
    } else {
        $("#txtPhone").attr("class", "statusOkay");
        $("#formStatus").text("");
        isValid = true;
    }
    return isValid;
}

/*
 * This helper function accepts the total input validation summary of all inputs, and set the
 * form input status accordingly. This is an output creation function, not data transform.
 */
function getValidationSummary(isSummaryValid) {
    if (true === isSummaryValid)
        $("#formStatus").attr("class", "statusOkay").text("Input submission succeeded.");
    else
        $("#formStatus").attr("class", "statusError").text("Input submission did not succeed.");
}

/*
 * This helper function call each of the input box field validator functions before submission.
 */
function validateFormInput() {
    var summaryValidation = validateFullName(null) &&
        validateAge(null) &&
        validatePhone(null);

    getValidationSummary(summaryValidation);
}

/*
 * This helper function registers all the required event handlers for this page.
 */
function registerGlobalEventHandlers() {
    $("form").on("submit", function (event) {
        event.preventDefault();
        validateFormInput();
    });
    validateTxtFullName();
    validateTxtAge();
    validateTxtPhone();
}

/*
 * Main() function entry point JS/JQuery $(document).ready()
 */
$(document).ready(function () {
    registerGlobalEventHandlers();
});