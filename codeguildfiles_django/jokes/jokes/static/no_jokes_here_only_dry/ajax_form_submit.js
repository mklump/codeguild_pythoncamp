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

function getStorySetupText() {
    return $('#setup_story').val()
}

function getPunchlineText() {
    return $('#punch_line').val();
}

function appendStoryText(storyText) {
    var blockquote = $('<blockquote></blockquote>');
    blockquote.text(commentText);
    $('body').append(blockquote);
}

function appendPunchlineText(punchlineText) {
    var blockquote = $('<blockquote></blockquote>');
    blockquote.text(punchlineText);
    $('body').append(blockquote);
}

function postJokeText(storyText, punchlineText) {
    var jokes_data = {
        'story_setup': storyText,
        'punch_line': punchlineText
    };
    $.get('/ajax/submit', jokes_data, function () {
        appendJoke(storyText, punchlineText);
        appendStoryText(storyText);
        appendPunchlineText(punchlineText);
    });
}

function submitJoke() {
    var storyText = getStorySetupText();
    var punchlineText = getPunchlineText();
    postJokeText(storyText, punchlineText);
}

/*
 * This functions registers the click event handler for the randomly generated link
 * surrounding the mole image.
 * @param {Object: <img>} is the object representation of mole's image on the grid
 */
function registerGlobalEventHandlers() {
    $('#ajax_submit').on('click', function (event) {
        submitJoke();
    });
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