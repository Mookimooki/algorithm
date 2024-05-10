import java.util.Scanner;

public class Main {
    private int solution(int n){
        if(n < 3) return n;
        int[] stairs = new int[n+1];
        stairs[1] = 1;
        stairs[2] = 2;

        for (int i = 3; i <= n; i++) {
            stairs[i] = stairs[i-1] + stairs[i-2];
        }
        return stairs[n];
    }
    public static void main(String[] args) {
        Main main = new Main();

        System.out.println(main.solution(1));
    }
}