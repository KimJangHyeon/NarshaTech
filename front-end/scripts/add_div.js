/**
 * Created by rlawk on 2017-07-27.
 */
//http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js

function add_div(){
    var div = document.createElement('div');
    div.innerHTML = document.getElementById('intro_block').innerHTML;
    document.getElementById('col1_contain5').appendChild(div);
}



function remove_div(obj){
    document.getElementById('field').removeChild(obj.parentNode);
}
