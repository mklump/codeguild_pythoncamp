/*
    Python Coding Bootcamp (pdxcodeguild)
    Code File for practice_validator.js
    by: Matthew James K on 5/3/2016
 */
"use strict"

/*
 * 
 */
function validateTxtFullName() {
    $("#txtFullName").on("keydown", function (event) {
        var txt = this.text;
        var re = new RegExp("(.+)[ ](.+)");
        match = re.exec(txt);
        
        if ("" === txt || Number.)
    });
}

/*
 * 
 */
function validateTxtAge() {
    $("#txtAge").on("keydown", function (event) {
    });
}

/*
 * 
 */
function validateTxtPhone() {
    $("#txtPhone").on("keydown", function (event) {
    });
}

/*
 * This helper function registers all the required event handlers for this page.
 */
function registerGlobalEventHandlers() {
    $("Form").on("submit", function (event) {
        event.preventDefault();
        getDiceElementToAdd();
    });
}

/*
 * Main() function entry point JS/JQuery $(document).ready()
 */
$(document).ready(function () {
    registerGlobalEventHandlers();
});