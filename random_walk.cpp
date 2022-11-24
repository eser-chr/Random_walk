#include <iostream>
#include <fstream>
#include <string>
#include <functional>
#include <vector>  
#include <random>
#include <chrono>
#include <algorithm> 
using namespace std;

const int N = 100;
const int dim = 2;
int position[dim];
uniform_int_distribution<int> dice(0,2*dim);

unsigned seed =chrono::steady_clock::now().time_since_epoch().count();
mt19937 engine(seed);


int main(){
	for(int i = 0 ; i<N; i++){
		int x = dice(engine);
		position[x/2] += x%2;
	}
	cout<<position[0]<<"  "<<position[1]<< "  "<<position[2]<<endl;
	return 0;
}











