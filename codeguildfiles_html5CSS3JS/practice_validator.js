/*
    Python Coding Bootcamp (pdxcodeguild)
    Code File for practice_validator.js
    by: Matthew James K on 5/3/2016
 */
"use strict"

/*
 * This helper fuction registers the txtFullName handler using "First Last" format exactly.
 */
function registerTxtFullNameInputHandler() {
    $("#txtFullName").on("input", validateFullName);
}

/*
 * This helper funtion registers the txtAge handler using YYYY-MM-DD number format exactly.
 */
function registerTxtAgeInputHandler() {
    $("#txtAge").on("input", validateAge);
}

/*
 * This helper funtion validates the txtPhone input box using 555-555-5555 number format exactly.
 */
function registerTxtPhoneInputHandler() {
    $("#txtPhone").on("input", validatePhone);
}
/*
 * This function finds the text within the full name input box, and returns it.
 * @param {String} is the id="" attribute of the input box to get the value for
 * @returns {String} of the input box text entry from the user.
 */
function getInputBoxText(inputBoxNameByID) {
    var txt = $('#' + inputBoxNameByID).value;
    if (null === txt)
        txt = document.getElementById('#' + inputBoxNameByID).value;
    if (null === txt)
        txt = $('#' + inputBoxNameByID)[0].value;
    return txt;
}
function setStatusOutputByControl(inputBoxID, inputBoxWarningMessage) {

}
/*
 * This function is the delegate callback for registerTxtFullNameInputHandler, and establishes if the #txtFullName
 * control has either valid user input either true or false.
 * This is an output creation function, not data transform.
 * @returns {Boolean} true if the input validation succeeded, otherwise false
 */
function validateFullName() { // TODO: This function is doing 3 steps in one, and not modular enough for unit testing. If unit testing this, then will need to re-do.
    var txt = getInputBoxText('txtFullName');
    var matchArray = txt.match('([a-zA-Z].+)[ ]([a-zA-Z].+)');
    var isValid = false;
    if (null === matchArray) {
        $('#txtFullName').attr('class', 'txtWarning');
        $('#formStatus').text('Full name is not valid.');
        isValid = false;
    } else {
        $('#txtFullName').attr('class', 'statusOkay');
        $('#formStatus').text("");
        isValid = true;
    }
    return isValid;
}

/*
 * This function is the delegate callback for registerTxtAgeInputHandler, and establishes if the #txtAge
 * control has either valid user input either true or false.
 * This is an output creation function, not data transform.
 * @returns {Boolean} true if the input validation succeeded, otherwise false
 */
function validateAge() { // TODO: This function is doing 3 steps in one, and not modular enough for unit testing. If unit testing this, then will need to re-do.
    var txt = getInputBoxText('txtAge');
    var matchArray = txt.match('([0-9]{4})[-]([0-9]{2})[-]([0-9]{2})');
    var isValid = false;
    if (null === matchArray) {
        $('#txtAge').attr('class', 'txtWarning');
        $('#formStatus').text('Age is not valid.');
        isValid = false;
    } else {
        $('#txtAge').attr('class', 'statusOkay');
        $('#formStatus').text('');
        isValid = true;
    }
    return isValid;
}

/*
 * This function is the delegate callback for registerTxtPhoneInputHandler, and establishes if the #txtPhone
 * control has either valid user input either true or false.
 * This is an output creation function, not data transform.
 * @returns {Boolean} true if the input validation succeeded, otherwise false
 */
function validatePhone() { // TODO: This function is doing 3 steps in one, and not modular enough for unit testing. If unit testing this, then will need to re-do.
    var txt = getInputBoxText('txtPhone');
    var matchArray = txt.match("([0-9]{3})[-]([0-9]{3})[-]([0-9]{4})");
    var isValid = false;
    if (null === matchArray) {
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
    if (isSummaryValid)
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
    registerTxtFullNameInputHandler();
    registerTxtAgeInputHandler();
    registerTxtPhoneInputHandler();
}
/*
 * This function delegate is the 'main' call back entry point for the associated
 * practice_validator.html page when it's loaded state is 'ready()'.
 */
function main() {
    registerGlobalEventHandlers();
}
/*
 * Main() function entry point JS/JQuery $(document).ready()
 */
$(document).ready(main);