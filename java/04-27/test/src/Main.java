import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    private List<Integer> solution(int[] input){
        List<Integer> answer = new ArrayList<>();
        int max = Arrays.stream(input).max().getAsInt();
        boolean[] numbers = new boolean[max+1];

        numbers[0] = numbers[1] = true;
        for (int i = 2; i < max+1; i++) {
            if(!numbers[i]){
                for (int j = i*2; j < max+1; j+=i) {
                    numbers[j] = true;
                }
            }
        }

        for(int number: input){
            if (!numbers[number]) answer.add(number);
        }

        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        int[] input = new int[count];

        for (int i = 0; i < count; i++) {
            String str = scanner.next();
            input[i] = Integer.parseInt(new StringBuilder(str).reverse().toString());
        }

        for (int ans: main.solution(input))
            System.out.print(ans + " ");
    }
}