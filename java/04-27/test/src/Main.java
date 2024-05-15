import java.util.Arrays;

public class Main {
    private int count(int distance, int[] rocks, long minTerm){
        int answer = 0;

        int start = 0;
        for(int rock: rocks){
            if(rock - start < minTerm){
                answer++;
            }else{
                start = rock;
            }
        }

        if(distance - start < minTerm){
            answer++;
        }

        return answer;
    }
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        Arrays.sort(rocks);

        int lt = 1;
        int rt = distance;

        while(lt <= rt){
            int mid = (lt + rt) / 2;
            if(count(distance, rocks, mid) <= n){
                lt = mid + 1;
                answer = mid;
            }else{
                rt = mid - 1;
            }
        }

        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();

        System.out.println(main.solution(25, new int[]{2, 14, 11, 21, 17}, 2)); //4
    }
}