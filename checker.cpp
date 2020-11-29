#include <iostream>
#include <cstdlib>
using namespace std;

void f(int a){
    while(a--){
        static int n = 0;
        int x = 0;
        cout << "n: " << n++ << " ,x: " << x++ << endl;
    }
}

int main(){
    f(3);
    return 0;}
