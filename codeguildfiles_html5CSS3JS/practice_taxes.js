/*
    Python Coding Bootcamp (pdxcodeguild)
    Code File for Group practice_taxes.html
    by: Andrew & Matthew James K on 4/25/2016

Group Practice: Taxes
Income tax in Oregon is progressive. That means the more you make, the larger fraction of that additional income you pay.

The tax brackets in 2014 were:

First $3,350 of income is taxed at 5%
The next $5,050 is taxed at 7%
The next $116,000 is taxed at 9%
Any more income is taxed at 9.9%
Someone who earns $50,000 this year pays:

5% of their first $3,350 in income -- $167.50
7% of their next $5,050 in income -- $353.50
9% of their next $116,600 in income (which is only $50,000 - $5,050 - $3,350 = $41,600) -- $3,744 So $167.50 + $353.50 + $3,744 or $4,265 total.

Write a program that let's someone enter their income and calculates and prints their total Oregon income tax.

You'll have to figure out how much of their income applies in each bracket.
Then multiply that amount by the rate to get the taxes for that bracket.
Then add together all of the taxes across brackets to get the total tax.

use console.log() for output printed statement in this form of JavaScript
*/
"use strict";

var grossIncome = 0;
​
var taxMap = {
    "3350": 0.05,
    "8400": 0.07,
    "125000": 0.09,
    "over": 0.099
};
​
var arrayTaxMap = function(taxMap) {
    var taxBracketArr = [];
    for (var key in taxMap){
        taxBracketArr.push(key);
    };
    return taxBracketArr;
};
​
var calcTaxes = function(grossIncome, taxBracketArr) {
​
    if (grossIncome <= parseInt(taxBracketArr[0])) {
        return taxObligation = grossIncome * taxMap[taxBracketArr[0]];
    }
​
    if (grossIncome <= parseInt(taxBracketArr[1])) {
        return taxObligation = 167.5 + ((grossIncome - 3350) * taxMap[taxBracketArr[1]]);
    }
​
    if (grossIncome <= parseInt(taxBracketArr[2])) {
        return taxObligation = (167.5 + 353.5) + ((grossIncome - 8400) * taxMap[taxBracketArr[2]]);
    }
​
    if (grossIncome > parseInt(taxBracketArr[2])) {
        return taxObligation = (167.5 + 353.5 + 10494) + ((grossIncome - 125000) * taxMap[taxBracketArr[3]]);
    }
};


void main()
{

}
var taxBracketArr = arrayTaxMap(taxMap);
var taxObligation = calcTaxes(grossIncome, taxBracketArr);
​
console.log(calcTaxes(50000, taxBracketArr));
console.log(calcTaxes(100000, taxBracketArr));
console.log(calcTaxes(125000, taxBracketArr));
console.log(calcTaxes(125001, taxBracketArr));