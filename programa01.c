#include <stdio.h>

int main(void) {
  int number;
  printf("Choose a number: ");
  scanf("%d", &number);
  if (number % 5 == 0 && number % 3 == 0) {
    printf("Your number is divisible by 5 and 3!\n");
  } else {
    printf("Your number isn't divisible by 5 and 3!\n");
  }
}
