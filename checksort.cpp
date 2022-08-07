// ip: {8,12,15} op:yes
// ip: arr[]={8,10,10,12} op:yes
// ip: arr[]={100} op:yes  // ip: arr[]={100,20,200} op:no
#include<iostream>
using namespace std;
bool isSorted(int arr[],int n)
{
    for(int i=1;i<n;i++)
    {
        if(arr[i]<arr[i-1])
        {
            return false;
        }
    }
    return true;
}
int main(){
    int arr[]={100};
    int n=sizeof(arr)/sizeof(arr[0]);
    cout<<isSorted(arr,n);
}