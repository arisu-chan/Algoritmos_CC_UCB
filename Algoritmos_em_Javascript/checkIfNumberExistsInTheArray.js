var array = [1, 2, 3, 4];

function checkIfNumberExistsInArray(number){
    return vetor.indexOf(number)
}

var res = checkIfNumberExistsInArray(5);

if(res >=0){
    document.write('Number does exist!');           
}else{
    document.write('Number does not exist!');
}
