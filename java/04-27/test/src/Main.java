import java.util.Scanner;

public class Main {
    private int solution(int[] input){
        int answer = 1;
        int maxHeight = input[0];

        for (int i = 1; i < input.length; i++) {
            if(input[i] > maxHeight) {
                answer++;
                maxHeight = input[i];
            }
        }

        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int length = scanner.nextInt();
        int[] input = new int[length];
        for (int i = 0; i < length; i++) {
            input[i] = scanner.nextInt();
        }

        System.out.println(main.solution(input));
    }
}