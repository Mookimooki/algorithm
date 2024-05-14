import java.util.Arrays;
import java.util.Scanner;

public class Main {
    private int count(int[] barns, int distance){
        int answer = 1, sum = 0;

        for(int i = 0; i < barns.length-1; i++){
            sum += barns[i+1] - barns[i];
            if(sum >= distance){
                sum = 0;
                answer++;
            }
        }

        return answer;
    }
    private int solution(int[] barns, int horseCount){
        int answer = 0;

        int lt = 1;
        int rt = barns[barns.length - 1];
        int mid;
        while (lt <= rt) {
            mid = (lt + rt) / 2;
            if(count(barns, mid) >= horseCount){
                answer = mid;
                lt = mid + 1;
            }else {
                rt = mid - 1;
            }
        }

        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(), c = scanner.nextInt();
        int[] barns = new int[n];
        for(int i = 0; i < n; i++){
            barns[i] = scanner.nextInt();
        }
        Arrays.sort(barns);

        System.out.println(main.solution(barns, c));
    }
}