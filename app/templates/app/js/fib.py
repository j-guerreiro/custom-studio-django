

# sequencia fibonacci
# Fn = F n - 1 + F n - 2

# 0 1 1 2 3 5 8 13 21 34
# cada termo subsequente equivale
# a soma dos dois anteriores

num = 0;
subsequente = 0;
anterior = 0;

for i = 0 ;  i <= 55 ; i++ :	
	++anterior;
	subsequente = anterior + i;
