import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int[] visited = new int[n];

        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0; i < n; i++) computers[i][i] = 0;

        for(int i = 0; i < n; i++) {
            if(visited[i] == 0) {
                visited[i] = 1;
                answer++;

                queue.offer(i);
                while(!queue.isEmpty()) {
                    int x = queue.poll();
                    for(int k = 0; k < n; k++) {
                        if(computers[x][k] == 1) {
                            visited[k] = 1;
                            queue.offer(k);
                            computers[x][k] = computers[k][x] = 0;
                        }
                    }
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Main main = new Main();

        System.out.println(main.solution(3, new int[][]{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}}));
        System.out.println(main.solution(3, new int[][]{{1, 1, 0}, {1, 1, 1}, {0, 1, 1}}));
    }
}