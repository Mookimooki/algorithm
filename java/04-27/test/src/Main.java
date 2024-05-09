import java.util.Arrays;
import java.util.Scanner;

public class Main {
    private int[] solution(int[] input){
        int[] answer = new int[input.length];

        for(int i = 0; i < input.length; i++){
            int rank = 1;
            for(int j = 0; j < input.length; j++){
                if(input[j] > input[i]){
                    rank++;
                }
            }
            answer[i] = rank;
        }
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
            System.out.print(score + " ");
        }
    }
}