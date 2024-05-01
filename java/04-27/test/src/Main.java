import java.util.Arrays;
import java.util.Scanner;

public class Main {
    private int[] solution(int[] input){
        int[] answer = new int[input.length];

        Arrays.sort(input);


        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        int[] input = new int[count];
        for (int i = 0; i < count; i++) {
            input[i] = scanner.nextInt();
        }
        for (int score: main.solution(input)) {
            System.out.print(main.solution(input) + " ");
        }
    }
}