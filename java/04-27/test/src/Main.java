import java.util.Scanner;

public class Main {
    private String solution(int cnt, String input){
        String answer = "";

        for (int i = 0; i < cnt; i++) {
            String codeString = input.substring(i * 7, (i + 1) * 7)
                    .replace('#', '1')
                    .replace('*', '0');
            answer += (char) Integer.parseInt(codeString, 2);
        }

        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int cnt = scanner.nextInt();
        String input = scanner.next();

        System.out.println(main.solution(cnt, input));
    }
}