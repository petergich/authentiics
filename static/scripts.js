    const texts = [
      "Authentic hub👡",
      "Best shoes👢",
      "Best prices👡",
      "Your Happiness🥿☺"
    ];
    var current=0;
  document.addEventListener("DOMContentLoaded", function() {
  var element = document.getElementById("paragraph");

  setInterval(function() {
    current++; 
    var randomNumber = Math.floor(Math.random() * 100);
    element.textContent = texts[current];
    var max=texts.length-1;
    if(current===max){
      current=0;
    }
  }, 6000);
});

var searchBar = document.getElementById('searchBar');
var optionsList = document.getElementById('optionsList');

function processor(input){
  var searchText=input.toLowerCase();
  fetchOptions(searchText);
}
function fetchOptions(searchText) {
  var url = 'options/?search=' + encodeURIComponent(searchText);

  var xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);
  xhr.onload = function() {
    if (xhr.status === 200) {
      var options = JSON.parse(xhr.responseText);
      if(searchText===""){
        options=[];
      }
      updateOptionsList(options);
    }
  };

  xhr.send();
}

function updateOptionsList(options) {
  var optionsList = document.getElementById('optionsList');
  optionsList.innerHTML = '';
 for (const option of options) {
    var p = document.createElement('p');
    p.textContent = option;
    optionsList.appendChild(p);
    p.onclick = () => selectOption(option);
    }
}
function submitSearch(){
  var search=document.getElementById("searchBar").value;
  var url = "?search=" + encodeURIComponent(search);
  window.location.href=url;
}
function selectOption(option){
  var url = 'item/' + option+ '/';
  window.location.href = url;
}
