/*
    Python Coding Bootcamp (pdxcodeguild)
    Program exercise file static/no_jokes_here_only_dry/ajax_form_submit.js
    by Matthew James K on 5/12/2016

Practice: Jokes -
    Save your solution as jokes.
    Have a page to submit jokes via a form. A joke has a "setup" and a "punchline" input. Submitted
    jokes should be saved in a global array in your logic module.
    Have a listing page where jokes are shown. Hide the punch lines until someone clicks on the setup.
Advanced:
    Use AJAX to submit your jokes.
 */
'use strict';

/*
 * This function returns the text string entered by the user for the #story_setup textbox.
 * @returns {String} value of the #story_setup textbox
 */
function getStorySetupText() {
  return $('#setup_story').val();
}

/*
 * This function returns the text string entered by the user for the #punch_line textbox.
 * @returns {String} value of the #punch_line textbox
 */
function getPunchlineText() {
  return $('#punch_line').val();
}

/*
 * This is the first of two functions that takes the text input from two textbox inputs
 * and places them into a JQuery style HTTP GET request, and builds the html output for
 * viewing back to the attached ajax_index.html file for viewing.
 */
function postJokeText(storyText, punchlineText) {
  var jokesData = {
    'story_setup': storyText,
    'punch_line': punchlineText
  };
  $.get('/ajax/submit', jokesData, function() {
  });
}

/*
 * This is the second of two functions that takes the text input from two textbox inputs
 * and places them into a JQuery style HTTP GET request, and builds the html output for
 * viewing back to the attached ajax_index.html file for viewing.
 */
function submitJoke() {
  var storyText = getStorySetupText();
  var punchlineText = getPunchlineText();
  postJokeText(storyText, punchlineText);
}

function registerSelectOptionClick() {
  $('option').on('click', function(event) {
    $('#punchLines')[0].hidden = ''; // Make the punchLines select control visible in the click event.
  });
}

/*
 * This functions registers the click event handler for the randomly generated link
 * surrounding the mole image.
 * @param {Object: <img>} is the object representation of mole's image on the grid
 */
function registerGlobalEventHandlers() {
  $('#ajax_submit').on('click', function(event) {
    submitJoke();
    $('#punchLines')[0].hidden = 'hidden';
  });
  registerSelectOptionClick();
}

/*
 * This is the main entry point for this file.
 */
function main() {
  registerGlobalEventHandlers();
}
/*
 * This statement registers main() to be called when the associated page is 'ready'.
 */
$(document).ready(main);