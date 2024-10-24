```java
import java.util.*;
public class MinMax {
    public static void FindMin(int[] arr){
        int min = 1000;
        for (int j : arr) {
            if (j < min) {
                min = j;
            }
        }
        System.out.println("The Smallest Element in the array is : "+min);
    }
    public static void FindMax(int[] arr){
        int max = -1000;
        for (int j : arr) {
            if (j > max) {
                max = j;
            }
        }
        System.out.println("The Largest Element in the array is : "+max);
    }
    public static void SortMinMax(int[] arr){
        Arrays.sort(arr);
        System.out.println("The Smallest Element in the array is : "+arr[0]);
        System.out.println("The Largest Element in the array is :"+arr[arr.length - 1]);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner( System.in);
        System.out.print("Array Size : ");
        int n = sc.nextInt();
        System.out.print("Array Elements : ");
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }

//        Time complexity: O(n log n)
//        Auxiliary Space: is O(1)
        SortMinMax(arr);

//        Time Complexity: O(N)
//        Auxiliary Space: O(1)
        FindMin(arr);
        FindMax(arr);
    }
}
```