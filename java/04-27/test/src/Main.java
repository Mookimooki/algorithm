import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public int solution(int[][] maps) {
        int answer = 0;
        int[][] directions = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};

        Queue<int []> queue = new LinkedList<>();
        queue.add(new int[]{0, 0});

        while (!queue.isEmpty()) {
            int size = queue.size();
            answer++;

            for(int i = 0; i < size; i++) {
                int[] point = queue.poll();
                int x = point[0], y = point[1];
                if(x == maps.length-1 && y == maps[0].length-1) return answer;
                if(maps[x][y] == 0) continue;
                maps[x][y] = 0;

                for(int[] direction : directions) {
                    int newX = x + direction[0], newY = y + direction[1];
                    if(newX < 0 || newX >= maps.length || newY < 0 || newY >= maps[0].length || maps[newX][newY] == 0) continue;
                    queue.add(new int[]{newX, newY});
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Main main = new Main();
        System.out.println(main.solution(new int[][]{{1,0,1,1,1},{1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,1},{0,0,0,0,1}}));
        System.out.println(main.solution(new int[][]{{1,0,1,1,1},{1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,0},{0,0,0,0,1}}));
        System.out.println(main.solution(new int[][]{{1, 1, 1, 1, 1},{1, 0, 1, 0, 1},{1, 1, 1, 1, 1},{1, 0, 1, 0, 1}, {1, 1, 1, 1, 1}}));
        System.out.println(main.solution(new int[][]{{1, 1, 1, 1, 1},{1, 0, 0, 0, 1},{1, 0, 0, 0, 1},{1, 1, 1, 1, 1}, {1, 1, 1, 1, 1}}));
        System.out.println(main.solution(new int[][]{{1, 0, 1, 1, 1},{0, 0, 1, 1, 1},{1, 1, 1, 1, 1},{1, 1, 1, 0, 0}, {1, 1, 1, 0, 1}}));
    }
}