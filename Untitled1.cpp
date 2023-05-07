#include <iostream>
using namespace std;

class MyClass {
    private:
        int num1, num2;
        char letter;
    
    public:
        void setNum(int n, int m, char a) {
            num1 = n;
            num2 = m;
            letter = a;
        }

        void calculate() {
            switch(letter) {
                case '-': 
                    cout << num1 - num2; 
                    break;
                case '+': 
                    cout << num1 + num2; 
                    break;
                case '*': 
                    cout << num1 * num2; 
                    break;
                case '/': 
                    cout << num1 / num2; 
                    break;
                default: 
                    cout << "Incorrect syntax"; 
            }    
        }
};

int main() {
    MyClass obj;
    obj.setNum(10, 20, '+');
    obj.calculate();
    return 0;
}

