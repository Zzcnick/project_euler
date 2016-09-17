// Coins
// Given 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p coins, how many ways are there
// to make 200p?

#include <stdio.h>

int main() {
  int p1,p2,p5,p10,p20,p50,p100;
  int answer = 0;
  int sum = 1; // single 200p coin

  // BASH
  for (p1 = 0; p1 <= 200; p1++) {
    for (p2 = 0; p2 <= 100; p2++) {
      for (p5 = 0; p5 <= 40; p5++) {
	for (p10 = 0; p10 <= 20; p10++) {
	  for (p20 = 0; p20 <= 10; p20++) {
	    for (p50 = 0; p50 <= 4; p50++) {
	      for (p100 = 0; p100 <= 2; p100++) {
		if (p1 +
		    2 * p2 +
		    5 * p5 +
		    10 * p10 +
		    20 * p20 +
		    50 * p50 +
		    100 * p100 == 200) // Check Equality
		  {
		    sum++;
		  }
	      }
	    }
	  }
	}
      }
    }
  }
  // END BASH
  printf("%d\n", sum);
  return 0;
}
