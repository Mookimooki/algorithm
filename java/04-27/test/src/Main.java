import java.util.Scanner;

public class Main {
    private Integer solution(String string){
        return Integer.parseInt(string.replaceAll("\\D", ""));
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();

        System.out.println(main.solution(input));
    }
}