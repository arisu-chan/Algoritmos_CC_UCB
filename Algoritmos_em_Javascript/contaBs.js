function contaBs(palavra){
		var counter = 0;
		//se eu colocar let aqui, ela terá escopo local e não será reconhecida
		//dentro do bloco for
		for(let i=0; i<palavra.length-1; i++){
			if(palavra[i] == 'B' || palavra[i] == 'b'){
				counter += 1;
			}
		}
		return counter;
	}

	contaBs("boneca");