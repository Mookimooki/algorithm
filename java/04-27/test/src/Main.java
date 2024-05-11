import java.util.Arrays;

public class Main {
    static int sumOfArr;
    static boolean flag = false;
    private void bfs(int length, int sum, int[] arr){
        if(flag) return;
        if(sum > sumOfArr/2) return;
        if(length == arr.length){
            if (sum == sumOfArr/2) flag = true;
            System.out.println(length + ": " + sum);
            return;
        }
        bfs(length+1, sum+arr[length], arr);
        bfs(length+1, sum, arr);
    }
    public static void main(String[] args) {
        Main main = new Main();

        int[] arr = new int[]{1, 3, 5, 6, 7, 10};
        sumOfArr = Arrays.stream(arr).sum();
        main.bfs(0, 0, arr);
        if (flag) System.out.println("YES");
        else System.out.println("NO");
    }
}