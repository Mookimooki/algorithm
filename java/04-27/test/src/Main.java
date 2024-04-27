import java.util.Scanner;

public class Main {
    private String solution(String string){
        char[] answer = string.toCharArray();

        int lt = 0, rt = string.length() - 1;
        while (lt < rt){
            if(!Character.isAlphabetic(answer[lt])) lt++;
            if(!Character.isAlphabetic(answer[rt])) rt--;

            if(Character.isAlphabetic(answer[lt]) && Character.isAlphabetic(answer[rt])){
                char tmp = answer[lt];
                answer[lt] = answer[rt];
                answer[rt] = tmp;
                lt++;
                rt--;
            }
        }
        return String.valueOf(answer);
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();

        System.out.println(main.solution(input));
    }
}