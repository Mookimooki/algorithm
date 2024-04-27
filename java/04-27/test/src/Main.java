import java.util.Scanner;

public class Main {
    private String solution(String string){
        char lastChar = string.charAt(0);
        int lastChatLength = 1;
        String answer = "" + lastChar;

        for(int i = 1; i < string.length(); i++){
            if(string.charAt(i) == lastChar) lastChatLength++;
            else{
                if(lastChatLength != 1) {
                    answer += lastChatLength;
                    lastChatLength = 1;
                }
                lastChar = string.charAt(i);
                answer += lastChar;
            }
        }
        if(lastChatLength != 1) answer += lastChatLength;

        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();

        System.out.println(main.solution(input));
    }
}