// 63
// How many pairs of positive ints, x and n, exist such that x^n has n digits? 

#include <stdio.h>
#include <math.h>

int main() {
  // We want to find x and n such that
  // 10^(n-1) <= x^n < 10^n 

  // Let us consider the upper bound on x
  // x^n < 10^n
  // We see that x must be less than 10 for this to be true
  // Therefore, 0 < x < 10, x must be from 1 through 9

  // Let us consider the lower bound on x and n
  // 10^(n-1) <= x^n
  // 10^n <= 10 * x^n
  // We can let equal the upper bound here in order to solve for the largest 
  // possible value of n, so let x = 9
  // 10^n <= 10 * 9^n 

  // Sample code for solving for n:
  /*
  double n = 1;
  while (pow(10,n) <= 10 * pow(9,n)) {n++;}
  n--;
  printf("%e\n",n);
  */
  // We discover that n = 21 is the largest possible n. 
  // Now, we simply test values of x from 1 to 9, n from 1 to 21.
  int x, n;
  int solutions = 0;
  for (x = 1 ; x < 10 ; x++) {
    for (n = 1 ; n < 22 ; n++) {
      if (pow(10,n-1) <= pow(x,n) && pow(x,n) < pow(10,n))
	solutions++;
    }
  }

  // Print Answer
  printf("Number of Solutions: %d\n",solutions);
}
