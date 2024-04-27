import java.util.Scanner;

public class Main {
    private void solution(String[] string){
        for(String str: string){
            char[] ch = str.toCharArray();
            int lt = 0, rt = ch.length-1;
            while(lt < rt){
                char tmp = ch[lt];
                ch[lt] = ch[rt];
                ch[rt] = tmp;
                lt++;
                rt--;
            }
            str = String.valueOf(ch);
            System.out.println(str);
        }
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        String[] input = new String[n];

        for(int i = 0; i < n; i++){
            input[i] = scanner.next();
        }

        main.solution(input);
    }
}