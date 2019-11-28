function update(i){
    var elem = document.getElementById('id_salesorderclassification');
    var old  = elem.value;
    elem = old + i.innerHTML ;
}

function myFunction(p1, p2) {
    return p1 * p2;
}
document.getElementById("demo").innerHTML = myFunction(4, 3);