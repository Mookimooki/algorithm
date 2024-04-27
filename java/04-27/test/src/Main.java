import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    private String solution(String string){
        String answer = "";
        Set<String> stringSet = new HashSet<>();
        for(char ch: string.toCharArray()){
            if(!stringSet.contains(String.valueOf(ch))) answer += ch;
            stringSet.add(String.valueOf(ch));
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