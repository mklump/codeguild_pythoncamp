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
/*
 * This function accepts the input box ID, warningm message, and the regular expression for that input box,
 * and determines the current user input's validity status for that input for that control.
 * @param {String} inputBoxID is the string representation for each input box control
 * @param {String} inputBoxWarningMessage is the warning message to print if any
 * @param {String} inputBoxRegularExpression is the regular expression with which to parse the present user input
 * @returns {Boolean} true if the validation of the present user input succeeded, otherwise false.
 */
function setInputStatusByControl(inputBoxID, inputBoxWarningMessage, inputBoxRegularExpression) {
    var txt = getInputBoxText(inputBoxID);
    var matchArray = txt.match(inputBoxRegularExpression);
    if (null === matchArray) {
        showValidityStatusOutput(inputBoxID, inputBoxWarningMessage, 'txtWarning');
        return false;
    } else {
        showValidityStatusOutput(inputBoxID, '', 'statusOkay');
        return true;
    }
}
/*
 * This function accepts the status warning mesage if any, and the corresponding CSS error status style to
 * alert the user of their current input error status to the #formStatus control.
 * @param {String} inputBoxID is the string representation for each input box control
 * @param {String} inputBoxRegularExpression is the regular expression with which to parse the present user input
 * @param {String} cssStyleToSet is the visible style of the warning text to set as output should an error, of if the status is okay.
 */
function showValidityStatusOutput(inputBoxID, inputBoxWarningMessage, cssStyleToSet) {
    $('#' + inputBoxID).attr('class', cssStyleToSet);
    $('#formStatus').text(inputBoxWarningMessage);
}
/*
 * This function is the delegate callback for registerTxtFullNameInputHandler, and establishes if the #txtFullName
 * control has either valid user input either true or false.
 * This is an output creation function, not data transform.
 * @returns {Boolean} true if the input validation succeeded, otherwise false
 */
function validateFullName() {
    return setInputStatusByControl('txtFullName', 'Full name is not valid.', '([a-zA-Z].+)[ ]([a-zA-Z].+)');
}

/*
 * This function is the delegate callback for registerTxtAgeInputHandler, and establishes if the #txtAge
 * control has either valid user input either true or false.
 * This is an output creation function, not data transform.
 * @returns {Boolean} true if the input validation succeeded, otherwise false
 */
function validateAge() {
    return setInputStatusByControl('txtAge', 'Age is not valid.', '([0-9]{4})[-]([0-9]{2})[-]([0-9]{2})');
}

/*
 * This function is the delegate callback for registerTxtPhoneInputHandler, and establishes if the #txtPhone
 * control has either valid user input either true or false.
 * This is an output creation function, not data transform.
 * @returns {Boolean} true if the input validation succeeded, otherwise false
 */
function validatePhone() {
    return setInputStatusByControl('txtPhone', 'Phone is not valid.', '([0-9]{3})[-]([0-9]{3})[-]([0-9]{4})');
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