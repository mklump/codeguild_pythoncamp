/*
    Python Coding Bootcamp (pdxcodeguild)
    Program exercise file static/no_jokes_here_only_dry/index.html
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

function makePunchLinesVisible() {
    return null;
}

/*
 * This function registers the click event handler and delegate call back from for when a select list
 * is clicked on.
 */
function registerSelectItemClickEvent() {
    $('option').on('click', function (event) {
        selectItemClick(event.target);
    });
}

/*
 * This function make visible the punchline control and the associated setup story that was clicked on.
 */
function selectItemClick(selectItemClicked) {

}