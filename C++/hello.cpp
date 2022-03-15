#include <iostream>
using namespace std;

int a = 10;

int main()
{
    extern int a;

    cout << a << endl;

    return 0;
}