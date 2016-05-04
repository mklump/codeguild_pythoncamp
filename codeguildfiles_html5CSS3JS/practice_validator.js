/*
    Python Coding Bootcamp (pdxcodeguild)
    Code File for practice_validator.js
    by: Matthew James K on 5/3/2016
 */
"use strict"

/*
 * This helper fuction validates the txtFullName input box using "First Last" format exactly.
 */
function validateTxtFullName() {
    $("#txtFullName").on("keydown", function (event) {
        var txt = this.text;
        var matchArray = txt.match("([a-zA-Z].+)[ ]([a-zA-Z].+)");
        if ("" !== matchArray[0] && "" != matchArray[1]) {
            $("#txtFullName").attr("class", "txtWarning");
            $("#formStatus").innerText = $("#formStatus").innerText + "Full name is not valid.";
        } else {
            $("#txtFullName").attr("class", "");
            $("#formStatus").innerText = $("#formStatus").innerText + "";
        }
    });
}

/*
 * This helper funtion validates the txtAge input box using YYYY-MM-DD number format exactly.
 */
function validateTxtAge() {
    $("#txtAge").on("keydown", function (event) {
        var txt = this.text;
        var matchArray = txt.match("([0-9]{3})[-]([0-9]{3})[-]([0-9]{4})");
        if ("" !== matchArray[0] && "" != matchArray[1]) {
            $("#txtAge").attr("class", "txtWarning");
            $("#formStatus").innerText = $("#formStatus").innerText + "Full name is not valid.";
        } else {
            $("#txtAge").attr("class", "");
            $("#formStatus").innerText = $("#formStatus").innerText + "";
        }
    });
}

/*
 * This helper funtion validates the txtPhone input box using 555-555-5555 number format exactly.
 */
function validateTxtPhone() {
    $("#txtPhone").on("keydown", function (event) {
        var txt = this.text;
        var matchArray = txt.match("([0-9]{4})[-]([0-9]{2})[-]([0-9]{2})");
        if ("" !== matchArray[0] && "" != matchArray[1]) {
            $("#txtPhone").attr("class", "txtWarning");
            $("#formStatus").innerText = $("#formStatus").innerText + "Full name is not valid.";
        } else {
            $("#txtPhone").attr("class", "");
            $("#formStatus").innerText = $("#formStatus").innerText + "";
        }
    });
}

/*
 * This helper function call each of the input box field validator functions before submission.
 */
function validateFormInput() {
    validateTxtFullName();
    validateTxtAge();
    validateTxtPhone();
}

/*
 * This helper function registers all the required event handlers for this page.
 */
function registerGlobalEventHandlers() {
    $("Form").on("submit", function (event) {
        event.preventDefault();
        validateFormInput();
    });
}

/*
 * Main() function entry point JS/JQuery $(document).ready()
 */
$(document).ready(function () {
    registerGlobalEventHandlers();
});