resultados.png sigma.png solar.png : 17.py Datos.dat valores.txt 15.py 16.py
	python 17.py
	python 15.py
	python 16.py
	
Datos.dat : Datos.x
	./Datos.x
	
Datos.x : 17.cpp
	c++ 17.cpp -o Datos.x