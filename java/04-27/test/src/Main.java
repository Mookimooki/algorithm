import java.util.Scanner;

public class Main {
    static int[] fibo;
    private int solution(int input){
        if(input < 3) return 1;
        if(fibo[input] != 0) return fibo[input];
        return fibo[input] = solution(input-1) + solution(input-2);
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();
        fibo = new int[input+1];
        fibo[0] = fibo[1] = 1;

        System.out.println(main.solution(input));
    }
}