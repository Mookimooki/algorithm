import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();

        int s = 5;
        int e = 14;
        int answer = 0;

        queue.add(s);

        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i = 0; i < size; i++) {
                s = queue.poll();

                if(s == e) break;
                if(s < 0 || s > e) continue;

                queue.offer(s + 1);
                queue.offer(s - 1);
                queue.offer(s + 5);
            }
            if(s == e) break;
            answer++;
        }
        System.out.println(answer);
    }
}