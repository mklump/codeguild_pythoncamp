/*
    Python Coding Bootcamp (pdxcodeguild)
    Code File for Practice visualdice.js
    by: Matthew James K on 5/2/2016
 */
"use strict"

/*
 * This helper function gets the sum of all dice, and passes it to printDiceSum() to print.
 */
function getSumAllDice() {
    var altsArray = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six"
    ];
    var lastTotal = 0;
    var nodes = $("#diceContainer").children();
    for (var i = 0; i < nodes.length; ++i)
        for (var x = 0; x < altsArray.length; ++x)
            if (altsArray[x] === nodes[i].childNodes[0].childNodes[0].alt)
                lastTotal += x + 1;
    printDiceSum(lastTotal);
}

/*
 * This helper function print the current total sum of the dice showing to the <div> with id="diceSum".
 */
function printDiceSum(lastTotal) {
    $("#diceSum").text("Current sum of all dice showing: " + lastTotal);
}

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

/**
 * This helper function adds each dice .jpg as it is rolled.
 * @param {text/html} this is the child dice element control last called or clicked on
 * @returns {text/html} that is the child dice element control for next dice to display.
 */
function addNextDiceElement(diceDivChildElement) {
    var nextDiceRoll = getRandomInt(0, 5);
    var lookupDiceFile = [ // In JavaScript value lookup via array is less code than switch() {}, still switch has its place.
        "one.jpg",
        "two.jpg",
        "three.jpg",
        "four.jpg",
        "five.jpg",
        "six.jpg"
    ];
    var diceImageFile = lookupDiceFile[nextDiceRoll];
    var altText = diceImageFile.split(".")[0];
    var imageElement = $("<img></img>").attr("src", diceImageFile);
    imageElement.attr("alt", altText);
    var anchorElement = $("<a></a>").attr("href", "").append(imageElement);
    anchorElement = createRerollLink(anchorElement);
    var diceDivChild = null;
    if (null === diceDivChildElement)
        diceDivChild = $("<div></div>").append(anchorElement); //$("<div><a href=\"\"><img src=\"" + diceImageFile + "\" alt=\"" + altText + "\"/></a></div>");
    else {
        var anchor = diceDivChildElement.childNodes;
        $(anchor).replaceWith(anchorElement);
        //$(diceDivChildElement).append(anchorElement);
    }
    return diceDivChild;
}

/*
 * This helper function applies the click event handler for the reroll anchor link by calling back
 * addNextDiceElement();
 * @param {text/html} of the current anchorElement being operated on for reroll
 * @returns {text/html} that is the last dice child div element rerolled
 */
function createRerollLink(anchorElement) {
    anchorElement.on("click", function (event) {
        event.preventDefault();
        var divElement = $(event.target).parents()[1];
        addNextDiceElement(divElement); // retrieve the parent html element clicked on <div><img></img></div>
    });
    return anchorElement;
}

/*
 * This helper funcition constructs all dice elements to display by calling the other helper
 * construction functions.
 */
function getDiceElementToAdd() {
    $("#diceContainer").empty();
    var numberOfDice = getDiceRolled();
    for (var x = 0; x < numberOfDice; ++x) {
        var diceElement = addNextDiceElement(null);
        $("#diceContainer").append(diceElement);
    }
    getSumAllDice();
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