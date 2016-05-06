/*
    Python Coding Bootcamp (pdxcodeguild)
    Code File for mole.js
    by: Matthew James K on 5/5/2016
 */
'use strict';

/*
 * This function sets the timer to call the changeImageToGrid() function delegate
 */
function setMoleGridTimer() {
    setInterval(changeImageToGrid, 1000);
}

/*
 * This function acts as a delegate call back function to setMoleGridTimer() that randomly
 * selects a Mole Grid location, and assigns the Mole to that cell location for whacking.
 */
function changeImageToGrid() {
    var nextMoleTarget = getRandomInt(0, 19);
    registerGeneratedLinkEventHandler(nextMoleTarget);
    highLightMoleLocation(moleImageLink);
}
/*
 * This functions registers the click event handler for the randomly generated link
 * surrounding the mole image.
 */
function registerGeneratedImgEventHandler(nextMoleTarget) {
    $(nextMoleTarget).on('click', function (event) {
        event.preventDefault();
        // Get the parent element of this child element
        // Call parent.replaceChild(wrapper, element); // set the wrapper as child (instead of the element)
        // wrapper.appendChild(element); // set element as child of wrapper
    });
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
 * This helper function registers all the required event handlers for this page.
 */
function registerGlobalEventHandlers() {
}
/*
 * This is the main entry point for this file.
 */
function main() {
    registerGlobalEventHandlers();
    setMoleGridTimer();
}
/*
 * This statement registers main() to be called when the associated page is 'ready'.
 */
$(document).ready(main);