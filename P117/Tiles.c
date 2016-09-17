// Tiles
// There are tiles of size 1, 2, 3, 4
// How many ways are there to tile a piece of length 50? 

// At first glance, this is a pretty standard recursion problem with
// S(n) = S(n-1) + S(n-2) + S(n-3) + S(n-4).

#include <stdio.h>

long long int recurseH(int iterations, long long t1, long long t2, long long t3, long long t4) {
  if (iterations > 1) {
    printf("S(%d): %lld\n", 51 - iterations, t1);
    recurseH(iterations-1, t2, t3, t4, t1 + t2 + t3 + t4);
  } else {
    return t1;
  }
}

long long int recurse(int its) {
  return recurseH(its, 1LL, 2LL, 4LL, 8LL);
}


int main() {
  printf("S(50): %lli\n", recurse(50));
  return 0;
}
