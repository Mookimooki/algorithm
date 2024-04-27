import java.util.Scanner;

public class Main {
    private String solution(String string){
        string = string.toUpperCase().replaceAll("[^A-Z]", "");
        if(string.equals(
                new StringBuilder(string).reverse().toString())
        ) return "YES";
        return "NO";
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();

        System.out.println(main.solution(input));
    }
}