import java.util.Scanner;

public class Main {
    private String solution(String string){
        string = string.toUpperCase();
        int i = 0, length = string.length();
        while(i < length/2){
            if(string.charAt(i) != string.charAt(length-i-1)) return "NO";
            i++;
        }

        return "YES";
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();

        System.out.println(main.solution(input));
    }
}