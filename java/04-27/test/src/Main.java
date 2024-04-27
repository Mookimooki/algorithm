import java.util.Scanner;

public class Main {
    private int solution1(String string, char c){
        int answer = 0;

        string = string.toUpperCase();
        c = Character.toUpperCase(c);

        for(char ch: string.toCharArray()){
            if(ch == c) answer ++;
        }
        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();
        char c = scanner.next().charAt(0);

        System.out.println(main.solution1(input, c));
    }
}