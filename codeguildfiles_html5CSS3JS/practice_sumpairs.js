/*
 *  Python Coding Bootcamp (pdxcodeguild)
 *  Code File for practice_sumpairs.js
 *  by: Matthew James K on 4/25/2016
 * 
 *  Practice: Sum Pairs
 *  Write a function named find_sum_pairs. It takes two arguments: a list of ints to search, and a sum to find.
 *  Go through the search list and find all pairs of numbers that would add together to the sum.
 *  Example output:
 *  >>> find_sum_pairs([-1, 0, 1, 2], 3)
 *  [[1, 2]]
 *  >>> find_sum_pairs([-1, 0, 1, 2], 1)
 *  [[-1, 2], [0, 1]]
 *  >>> find_sum_pairs([2, -1, 2], 1)
 *  [[2, -1], [-1, 2]]
 *  >>> find_sum_pairs([-1, 1, 2, 2], 3)
 *  [[1, 2], [1, 2]]
 */
"use strict"

function find_sum_pairs(list_to_search, sum_to_find) {
    /*
     * This function for this practice accepts two arguments: a list of ints to search, and a sum to find.
     * With these two parameters, the funtion will Go through the search list and find all pairs of numbers
     * that would add together to the sum.
     * :param 1: list_ints_to_search as the list of integers to search through
     * :returns: the list of pairs found to be the sum of which to find
     */
    if (Array !== list_to_search.constructor) { // Always use the === or !== "strictly equals" equality versus the == and != regular equals that casts the operands in the expression if ("4" == 4).
        console.log("Error: list_ints_to_search is not correct type - expected List() type or [].");
    };
    if (false === Number.isInteger(sum_to_find)) {
        console.log("Error: sum_to_find is not correct type - expected int type or 1, 2, 3, etc.");
    };
    var list_found_pairs = [];
    var next_element_to_initialize = 0;
    for (var x = 0; x < list_to_search.length; ++x) {
        for (var y = x; y < list_to_search.length; ++y) {
            if (sum_to_find === list_to_search[x] + list_to_search[y]) {
                list_found_pairs[next_element_to_initialize] = [list_to_search[x], list_to_search[y]]; // A matched sum is found, create next array element and assign it.
                next_element_to_initialize++; // Increment the next array element to initialize for the next matching found sum pairs.
            };
        };
    };
    return list_found_pairs;
};

var main = function () {
    console.log("The found sum pairs are: " + find_sum_pairs([-1, 0, 1, 2], 3));
    console.log("The found sum pairs are: " + find_sum_pairs([-1, 0, 1, 2], 1));
    console.log("The found sum pairs are: " + find_sum_pairs([2, -1, 2], 1));
    console.log("The found sum pairs are: " + find_sum_pairs([-1, 1, 2, 2], 3));
};
    
main();