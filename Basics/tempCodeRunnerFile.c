#include<stdio.h>

int main() {
    int n = 5;

    for(int i=2;i*i<n;i++){
        if(n%i == 0){
            cout<<"Not Prime"<<endl;
            break;
        }
        cout<<"Prime";    
    }
    return 0;
}