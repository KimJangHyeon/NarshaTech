/**
 * Created by rlawk on 2017-07-20.
 */
function addPicture() {
    var x = document.createElement("INPUT");
    x.setAttribute("type", "file");
    document.getElementById("img_block").appendChild(x);
    // document.body.appendChild(x);
}