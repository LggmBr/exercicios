#include <stdio.h>

int main(void) {
  int arr[4];
  int largest = 0;
  int sum = 0;
  for (int i = 0 ; i < 4 ; ++i ) {
    printf("Number %d: ", i + 1);
    scanf("%d", &arr[i]);
    if (arr[i] > largest) {
      largest = arr[i];
    }
    sum += arr[i];
  }
  sum -= largest;
  printf("\nThe largest number is: %d\n", largest);
  printf("The sum of the 3 smallest numbers is: %d\n", sum);
  
  return 0;
}
