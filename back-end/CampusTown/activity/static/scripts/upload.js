/**
 * Created by rlawk on 2017-07-20.
 */
var index=0;
function addPicture() {
    if(index!=10){
        var x = document.createElement("INPUT");
        x.setAttribute("type", "file");
        document.getElementById("img_block").appendChild(x);
        index++;
    }
    if(index==10){
        var x= document.getElementBy
        document.getElementById("img_block").removeChild();
    }
    // document.body.appendChild(x);
}