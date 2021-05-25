

//sequencia fibonacci
// Fn = F n - 1 + F n - 2

// 0 1 1 2 3 5 8 13 21 34
// cada termo subsequente equivale
// a soma dos dois anteriores

var num = 0;
var subsequente = 0;
var anterior = 0;

for ( var i = 0 ;  i <= 55 ; i++ ) {

	++anterior;
	subsequente = anterior + i;

}