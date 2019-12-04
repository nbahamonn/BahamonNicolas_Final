#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

// variable globales
const int Nx = 41;
const int Nt = 20;
const double Tf = 0.5;
const double Ti = 0.0;
const int Xi = 0;
const int Xf = 2;
const double dx = 0.01;
const double dt = 0.01;

int main (){
    
    double **U = new double *[Nt+1];
        for(int i = 0; i <= Nt; i++){
            U[i] = new double[Nx+1];
        }
            
    for(int j = 0; j <= Nx; j++){
        U[0][j] = exp(-0.5*pow((j-1),2)/pow(0.25,2));
    }
    
    for(int i = 1; i < Nt; i++){
		for(int j = 0; j < Nx; j++){
				U[i][j] = U[i][j] - (dt/dx)*(U[i][j]-U[i][j-1]);
		}
	} 
               
    ofstream outfile;
    outfile.open("Datos.dat");
	
	for(int i = 0; i <= Nt; i++){
		for(int j = 0; j <= Nx; j++){
			outfile << U[i][j] << "\t";
		}
		outfile << endl;
	}		
	outfile.close();
            
    return 0;
}

