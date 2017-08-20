/**
 * Created by rlawk on 2017-07-22.
 */
function onlyNumber(obj){
    if(event.keyCode>=48&&event.keyCode<=57){
        return true;
    }else{
        event.returnValue=false;
    }
}

function onlyAlp(){
    if(event.keyCode>=65&&event.keyCode<=90){
        return true;
    }if(event.keyCode>=97&&event.keyCode<=122){
        return true;
    }else{
        event.returnValue=false;
    }
}

function alpAndNumber(obj){
    if(event.keyCode>=65&&event.keyCode<=90){
        return true;
    }if(event.keyCode>=97&&event.keyCode<=122){
        return true;
    }if(event.keyCode>=48&&event.keyCode<=57){
        return true;
    }if((event.keyCode==64||event.keyCode==46)&&obj==='e') {
        return true;
    }else
    {
        event.returnValue=false;
    }
}
///////////////////////////////////////////////////////////////////////
function password(){
    var special, number, alp;
    var count=0;

    special=false;
    number=false;
    alp=false;
    for() {
        if (event.keyCode >= 65 && event.keyCode <= 90) {
            alp = true;
        }
        if (event.keyCode >= 97 && event.keyCode <= 122) {
            alp = true;
        }

        if (event.keyCode >= 48 && event.keyCode <= 57) {
            number = true;
        }

        else {
            special = true;
        }
    }

    if(special===true) count++;
    if(alp===true) count++;
    if(number===true)count++;

    if(count>=2){
        //checked
    }

}