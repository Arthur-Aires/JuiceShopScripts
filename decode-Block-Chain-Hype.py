import math

N = 145906768007583323230186939349070635292401872375357164399581871019873438799005358938369571402670149802121818086292467422828157022922076746906543401224889672472407926969987100581290103199317858753663710862357656510507883714297115637342788911463535102712032765166518411726859837988672111837205085526346618740053
e = 65537

fileEncrypted = open("announcement_encrypted.md","r")

for _ in fileEncrypted.readlines():
	
	_ = _.rstrip()
	
	for __ in range(0,300):
		
		resultadoBruteCriptografado = str(pow(__, e, N))
		
		print(resultadoBruteCriptografado)
			
		if resultadoBruteCriptografado ==  _:

			with open("decode.txt", "a") as resultadoScript:
    				resultadoScript.write(chr(__))			
			
			print(chr(__))
			break
	
	
