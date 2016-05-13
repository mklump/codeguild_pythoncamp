/*
    Python Coding Bootcamp (pdxcodeguild)
    Code File for mole.js
    by: Matthew James K on 5/5/2016
 */
'use strict';

/*
 * This function sets the timer to call the changeImageToGrid() function delegate
 * @param {Number} that is a unique identifier needed for calling clearInterval() later
 */
function setMoleGridTimer() {
    return setInterval(changeImageToGrid, 1000);
}

/*
 * This function delegate is called by setTimeout in main() to stop the mole image appearing
 * every 1 second after 10 minutes have elasped
 */
function stopMoleGridTimer(intervalID) {
    clearInterval(intervalID);
}

/*
 * This function acts as a delegate call back function to setMoleGridTimer() that randomly
 * selects a Mole Grid location, and assigns the Mole to that cell location for whacking.
 */
function changeImageToGrid() {
    clearAllMoleLocations();
    var nextMoleTargetByID = getRamdomMoleLocation();
    var nextMoleTargetImage = setMoleImgToGridLoc(nextMoleTargetByID);
    highLightMoleLocation(nextMoleTargetImage);
    registerGeneratedImgEventHandler(nextMoleTargetImage);
}
/*
 * This function returns the next random selected mole location.
 * @returns {Number} of the next random mole location
 */
function getRamdomMoleLocation() {
    return getRandomInt(0, 19);
}
/*
 * This function accepts the next randomly selected Mole image location, and applies assignment
 * for the src attribute of that <img> tag so the mole image appears there.
 * @param {Number} is the <img> id control on the grid of the mole's location
 * @returns {Object: <img>} of the mole image grid location
 */
function setMoleImgToGridLoc(nextMoleTargetByID) {
    return $('#' + nextMoleTargetByID).attr('src', 'mole.jpg');
}
/*
 * This function applies a slightly brighter border highlighting around the <img> control
 * so that the mole image targeted for whacking can be better seen.
 * @param {Object: <img>} is the object representation of mole's image on the grid
 */
function highLightMoleLocation(nextMoleTargetImage) {
    $(nextMoleTargetImage).attr('class', 'highlight');
}
/*
 * This functions registers the click event handler for the randomly generated link
 * surrounding the mole image.
 * @param {Object: <img>} is the object representation of mole's image on the grid
 */
function registerGeneratedImgEventHandler(nextMoleTargetImage) {
    $(nextMoleTargetImage).on('click', function (event) {
        clearAllMoleLocations();
    });
}
/*
 * This function clears the appearance of the mole back to all holes.
 * @param {Object: <img>} is the object representation of mole's image to clear on the grid
 */
function clearAllMoleLocations() {
    $('img').attr('src', 'hole.jpg'); // Set clicked image back to empty on <img src=""> tag
    $('img').attr('class', ''); // Clear the highlighting around the last target
    $('img').unbind('click'); // Unbind the click event for the last mole that was whacked
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
 * This is the main entry point for this file.
 */
function main() {
    var intervalID = setMoleGridTimer(); // Start the timer of the mole appearing as soon as the page is loaded and ready.
    setTimeout(stopMoleGridTimer, 600000, intervalID); // Stop the timer of the mole appearing after 10 minutes have elapsed.
    clearAllMoleLocations();
    //isInteger(0);
}
/*
 * This statement registers main() to be called when the associated page is 'ready'.
 */
$(document).ready(main);