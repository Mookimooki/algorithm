import java.util.Scanner;

public class Main {
    private String solution(String string){
        String answer = "";
        string += " ";
        int length = 1;

        for (int i = 0; i < string.length() - 1; i++ ){
            if(string.charAt(i) == string.charAt(i+1)) length++;
            else{
                answer += string.charAt(i);
                if(length > 1) answer += length;
                length = 1;
            }
        }

        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();

        System.out.println(main.solution(input));
    }
}