import java.util.Scanner;

public class Main {
    private int[] solution(int input){
        int[] answer = new int[input];
        answer[0] = answer[1] = 1;

        for (int i = 2; i < input ; i++) {
            answer[i] = answer[i-1] + answer[i-2];
        }

        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();

        for (int result: main.solution(input))
            System.out.print(result + " ");
    }
}