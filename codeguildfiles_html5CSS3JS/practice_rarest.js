/*
    Python Coding Bootcamp (pdxcodeguild)
    Code File for Group practice_taxes.html
    by: Andrew & Matthew James K on 4/25/2016

    Practice: Rarest Age in a JS Map/Object key:value pair data structure
Given an object that maps names to ages, find the rarest age, then print it out using.
*/
"use strict"

var namesToAges = {
    "Alyssa": 22,    "Charley": 25,    "Dan": 25,    "Jeff": 20,    "Kasey": 20,    "Kim": 20,    "Morgan": 25,    "Ryan": 25,    "Stef": 22
};

var getRarestAgeCount = function (namesToAgesMap, what_to_count) {
    /*
     * This helper function accepts the namesToAges Map structure,
     * and returns the count age number to search for.
     * :param1: namesToAgesMap as the namesToAges Map data structure to count number of occurences.
     * :returns: the count occurences of the age value for the specified Map.
     */
    var age_value_count = 0;
    for (var key in namesToAgesMap) {
        if (what_to_count == namesToAgesMap[key]) {
            age_value_count++;
        };
    };
    return age_value_count;
};

var getNamesToAgeRarestAge = function () {
    /*
     * This helper function accepts the Map data structure in the outter function scope, and
     * :returns: the rarest occurences of each set age in the Map object structure
     */
    var occurences_of_age = 999999999999, /*initialize as maximum occurences to find the lowest*/
        current_count_of_age = 0,
        lowest_age_occurence = 0;
    for (var key in namesToAges) {
        current_count_of_age = getRarestAgeCount(namesToAges, namesToAges[key]);
        if (occurences_of_age > current_count_of_age) {
            occurences_of_age = current_count_of_age;
            lowest_age_occurence = namesToAges[key];
        };
    };
    return lowest_age_occurence;
};

var main = function () {
    console.log("The rarest occurences of age in the namesToAge Map was: " + getNamesToAgeRarestAge().toString());
};

main();