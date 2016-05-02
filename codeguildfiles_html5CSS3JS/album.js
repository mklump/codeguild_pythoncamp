/*
    Python Coding Bootcamp (pdxcodeguild)
    Code File for Group album.js
    by: Erin Efough and Matthew James K on 4/29/2016
 */
"use strict"

function getURLString(){
    return $("#urlAddress").val();
}

function createDelLink(sectionElement) {
    var deleteElement = $("<a></a>").text("Delete").attr("href", "");
    deleteElement.on("click", function (event) {
        event.preventDefault();
        sectionElement.remove();
        countImages();
    });
    return deleteElement;
}

function createImageSection(URLString) {
    // var albumChild = document.createElement("section");
    var imageElement = $("<img>").attr("src", URLString);
    var linkElement = $("<a></a>").text("click to download").attr("href", URLString);
    var albumChild = $("<section></section>").append(imageElement);   
    albumChild.append(linkElement);
    var deleteElement = createDelLink(albumChild);
    albumChild.append(deleteElement);
    return albumChild;
}

function addAlbumSectionBlock(){
    var URLString = getURLString();
    var sectionElement = createImageSection(URLString);
    $("#albumlist").append(sectionElement); // Adding album section child to parent section
}

function addPictureControlSet() {
    $("form").on("submit", function (event) {
        event.preventDefault();
        addAlbumSectionBlock();
        countImages();
    });
}

function countImages() {
    var parent = $("#albumlist");
    var childCount = parent.children().length;
    $("#imagecount").text("Count of Images:  " + childCount);
}

$(document).ready(function() {
    //this could be the equivalent of jquery main
    addPictureControlSet();
})