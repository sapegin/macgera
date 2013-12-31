$(function(){
    var num = (Math.floor(Math.random()*4));
    var array = ['one', 'two', 'three', 'four'];
    var elem = document.getElementById('main');
    elem.classList.add(array[num]);
});