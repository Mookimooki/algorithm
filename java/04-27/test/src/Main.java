import java.util.Scanner;

public class Main {
    private int solution(int input){
        int answer = 0;
        boolean[] numbsers = new boolean[input+1];

        for (int i = 2; i < input+1; i++) {
            if(!numbsers[i]){
                answer++;
                for (int j = i; j < input+1; j+=i) {
                    numbsers[j] = true;
                }
            }
        }

        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();

        System.out.println(main.solution(input));
    }
}