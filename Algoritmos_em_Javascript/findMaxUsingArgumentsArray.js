function max(){
    var m = -Number.MAX_VALUE;

    for(var i = 0; i < max.arguments.length; i++){
        if(max.arguments[i] > m) m = max.arguments[i];
    }


    return m;
}

var largest = max(12, 1, 4, 25, 98, 100);
console.log(largest);

