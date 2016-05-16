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
        makePunchlineVisible(event.target);
    });
}

/*
 * This function delegate makes visible the punchline control and the associated setup story that was clicked on.
 * @param {Object: <option>} is the currently selected list item that was just now clicked.
 */
function makePunchlineVisible(selectItemClicked) {
    var div_parent = $('#hideable')[0];
    div_parent.hidden = false;// Explicitly set hidden property on the <div> with id='hideable' to 'false' making it visible.
    var jokes = getDeSerializedJokesArray();
    createPunchlineOutput(selectItemClicked, jokes);
}

/*
 * This fuction retrieves the jokes array object instance from the hidden html control id=json_serialized_string_array_of_jokes
 * @returns {Array} of jokes from the python global variable for processing here in the html and javascript layer.
 */
function getDeSerializedJokesArray() {
    var serialized_string = $('#json_serialized_string_array_of_jokes').val();
    return JSON.parse(serialized_string);
}

/*
 * This fucntion creates the html block output for the selected story setup item to the associated punchline for reading.
 * @param {Object: <option>} is the currently selected story setup item in the list of jokes
 * @param {Array} of joke story setups and their associated punchlines from the python jokes global variable
 */
function createPunchlineOutput(selectItemClicked, jokes) {
    var parent_div = $('#hideable')[0];
    parent_div.innerText = 'Here are the Punch Lines:';
    var blockquote = $('<blockquote></blockquote>')[0];
    for (var joke = 0; joke < jokes.length; ++joke) {
        if (selectItemClicked.text === jokes[joke][0]) {
            blockquote.innerText = jokes[joke][1] + ' ' + jokes[joke][2];
            break;
        }
    }
    var section = $('<section></section>').append(blockquote);
    $('#hideable').append(section);
}

/*
 * This function registers all the event handlers for every user interaction with this web page.
 */
function registerGlobalEventHandlers() {
    registerSelectItemClickEvent()
}

function main() {
    registerGlobalEventHandlers();
    $('#hideable')[0].hidden = true; // Explicitly set the hidden property on the <div> with id='hideable' to 'true'.
}
/*
 * This statement registers main() to be called when the associated page is 'ready'.
 */
$(document).ready(main);