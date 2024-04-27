import java.util.Scanner;

public class Main {
    private String solution(String string){
        String onlyAlphabeticString = "";
        for(char ch: string.toLowerCase().toCharArray()){
            if(Character.isAlphabetic(ch)) onlyAlphabeticString += ch;
        }
        if(onlyAlphabeticString.equals(
                new StringBuilder(onlyAlphabeticString).reverse().toString())
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