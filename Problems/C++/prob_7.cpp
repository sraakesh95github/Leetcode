#include "iostream"
#include "cmath"

using namespace std;

class Solution {
public:
    int reverse(int x) {
      int pop = 0;
      int rev = 0;
      int temp = 0;

      while(x!=0) {
        pop = x % 10;
        if(rev == floor(INT_MAX / 10)) {
          cout << "Entered the equal case...";
          if(pop > 7) {
            return 0;
          }
          else if(pop < -8) {
            return 0;
          }
        }
        else if (rev > floor(INT_MAX / 10) || rev < ceil(INT_MIN / 10)) {
          cout << "Entered the greater case...";
          return 0;
        }
        x = floor(x / 10);
        temp = rev * 10 + pop;
        rev = temp;
      }
      return rev;
    }
};

int main() {
  int a = 2147483647;
  int c = -1463847412;
  int num1 = -2147483648;
  cout << "Max number: " << INT_MAX << "\n";
  // cout << "Enter input: ";
  // cin >> a;
  cout << "Entered input: " << num1 << "\n";
  Solution b;
  cout << "Reversed string: " << b.reverse(num1) << "\n";
}