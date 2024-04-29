import java.util.Scanner;

public class Main {
    private char[] solution(int[][] input){
        char[] answer = new char[input.length];

        for (int i = 0; i < input.length; i++) {
            if(input[i][0] == input[i][1]) answer[i] = 'D';
            else if(input[i][0] == 1 && input[i][1] == 3) answer[i] = 'A';
            else if(input[i][0] == 3 && input[i][1] == 1) answer[i] = 'B';
            else if(input[i][0] < input[i][1]) answer[i] = 'B';
            else answer[i] = 'A';
        }

        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        int[][] input = new int[count][2];

        for (int i = 0; i < 2; i++) {
            for (int k = 0; k < count; k++) {
                input[k][i] = scanner.nextInt();
            }
        }

        for(char ch: main.solution(input))
            System.out.println(ch);
    }
}