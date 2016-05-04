/*
    Python Coding Bootcamp (pdxcodeguild)
    Code File for practice_validator.js
    by: Matthew James K on 5/3/2016
 */
"use strict";

/*
 * This helper fuction validates the txtFullName input box using "First Last" format exactly.
 * This is an output creation function, not data transform.
 * @returns {Boolen} true if the validation for this input succeeded, otherwise false.
 */
function validateTxtFullName() {
    var valid = false;
    $("#txtFullName").on("input", function (event) {
        event.preventDefault();
        var txt = this.value;
        var matchArray = txt.match("([a-zA-Z].+)[ ]([a-zA-Z].+)");
        if (null === matchArray || "" === matchArray[0] || "" === matchArray[1]) {
            $("#txtFullName").attr("class", "txtWarning");
            $("#formStatus").text("Full name is not valid.");
            valid = true;
        } else {
            $("#txtFullName").attr("class", "statusOkay");
            $("#formStatus").text("");
            valid = false;
        }
    });
    return valid;
}

/*
 * This helper funtion validates the txtAge input box using YYYY-MM-DD number format exactly.
 * This is an output creation function, not data transform.
 * @returns {Boolen} true if the validation for this input succeeded, otherwise false.
 */
function validateTxtAge() {
    var valid = false;
    $("#txtAge").on("input", function (event) {
        event.preventDefault();
        var txt = this.value;
        var matchArray = txt.match("([0-9]{4})[-]([0-9]{2})[-]([0-9]{2})");
        if (null === matchArray || "" === matchArray[0] || "" === matchArray[1]) {
            $("#txtAge").attr("class", "txtWarning");
            $("#formStatus").text("Age is not valid.");
            valid = true;
        } else {
            $("#txtAge").attr("class", "statusOkay");
            $("#formStatus").text("");
            valid = false;
        }
    });
    return valid;
}

/*
 * This helper funtion validates the txtPhone input box using 555-555-5555 number format exactly.
 * This is an output creation function, not data transform.
 * @returns {Boolen} true if the validation for this input succeeded, otherwise false.
 */
function validateTxtPhone() {
    var valid = false;
    $("#txtPhone").on("input", function (event) {
        event.preventDefault();
        var txt = this.value;
        var matchArray = txt.match("([0-9]{3})[-]([0-9]{3})[-]([0-9]{4})");
        if (null === matchArray || "" === matchArray[0] || "" === matchArray[1]) {
            $("#txtPhone").attr("class", "txtWarning");
            $("#formStatus").text("Phone is not valid.");
            valid = true;
        } else {
            $("#txtPhone").attr("class", "statusOkay");
            $("#formStatus").text("");
            valid = false;
        }
    });
    return valid;
}

/*
 * This helper function accepts the total input validation summary of all inputs, and set the
 * form input status accordingly. This is an output creation function, not data transform.
 */
function createValidationSummary(isSummaryValid) {
    if (true === isSummaryValid)
        $("#formStatus").attr("class", "statusOkay").text("Input submission succeeded.");
    else
        $("#formStatus").attr("class", "statusError").text("Input submission did not succeed.");
}

/*
 * This helper function call each of the input box field validator functions before submission.
 * This is an output creation function, not data transform.
 */
function validateFormInput() {
    var summaryValidation = validateTxtFullName() &&
        validateTxtAge() &&
        validateTxtPhone();

    createValidationSummary(summaryValidation);
}

/*
 * This helper function sets the input event handlers by calling them directly.
 * This is an output creation function, not data transform.
 */
function createInputHandlers() {
    validateTxtFullName();
    validateTxtAge();
    validateTxtPhone();
}

/*
 * This helper function registers all the required event handlers for this page.
 * This is an output creation function, not data transform.
 */
function registerGlobalEventHandlers() {
    $("form").on("submit", function (event) {
        event.preventDefault();
        validateFormInput();
    });
    createInputHandlers();
}

/*
 * Main() function entry point JS/JQuery $(document).ready()
 */
$(document).ready(function () {
    registerGlobalEventHandlers();
});