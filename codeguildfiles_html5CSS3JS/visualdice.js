/*
    Python Coding Bootcamp (pdxcodeguild)
    Code File for Practice visualdice.js
    by: Matthew James K on 5/2/2016
 */
"use strict"

/*
 * This helper function retrieves the current text of txtNumberDice input box as an expected number.
 * @returns {Number} as an integer of the number of dice to roll, if entry is not valid returns null
 */
function getDiceRolled() {
    var numberOfDice = $("#txtNumberDice").val();
    if (false === Number.isInteger(Number.parseInt(numberOfDice)) || 1 > Number.parseInt(numberOfDice)) {
        console.log("You did not enter a valid non-negative number of dice to roll.");
        return null;
    }
    else
        return Number.parseInt(numberOfDice);
}

/*
 * This helper function returns a random integer between min (included) and max (excluded)
 * @param {Number} min is an integer that defines the lower boundary of the range of the random number to get
 * @param {Number} max is an integer that defines the upper boundary of the range of the random number to get
 * @returns {Number} an integer of the requested range of random number.
 */
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

/*
 * This helper function adds each dice .jpg as it is rolled.
 * @returns {text/html} that is the child element control for next dice to display.
 */
function addNextDiceElement() {
    var nextDiceRoll = getRandomInt(0, 5);
    var lookupDiceFile = [
        "one.jpg",
        "two.jpg",
        "three.jpg",
        "four.jpg",
        "five.jpg",
        "six.jpg"
    ];
    var diceImageFile = lookupDiceFile[nextDiceRoll];
    var altText = diceImageFile.split(".")[0];
    var diceDivChild = $("<div><a href=\"\"><img src=\"" + diceImageFile + "\" alt=\"" + altText + "\"/></a></div>");
    return diceDivChild;
}

function createDelLink(sectionElement) {
    var deleteElement = $("<a></a>").text("Delete").attr("href", "");
    deleteElement.on("click", function (event) {
        event.preventDefault();
        sectionElement.remove();
        countImages();
    });
    return deleteElement;
}

/*
 * This helper funcition constructs all dice elements to display by calling the other helper
 * construction functions.
 */
function getDiceElementToAdd() {
    var numberOfDice = getDiceRolled();
    for (var x = 0; x < numberOfDice; ++x) {
        var diceElement = addNextDiceElement();
        $("#diceContainer").append(diceElement);
    }
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