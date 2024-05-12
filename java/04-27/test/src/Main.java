import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static int[][] directions = {{0,1}, {0,-1}, {1,0}, {-1,0}};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] grid = new int[7][7];
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                grid[i][j] = scanner.nextInt();
            }
        }

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0});
        grid[0][0] = 1;

        int answer = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            answer++;

            for (int i = 0; i < size; i++) {
                int[] cur = queue.poll();
                int x = cur[0], y = cur[1];

                for (int[] direction : directions) {
                    int newX = x + direction[0], newY = y + direction[1];
                    if(newX == 6 && newY == 6) {
                        System.out.println(answer);
                        return;
                    }
                    if(newX < 0 || newX >= 7 || newY < 0 || newY >= 7 || grid[newX][newY] == 1) continue;

                    grid[newX][newY] = 1;
                    queue.offer(new int[]{newX, newY});
                }
            }
        }

        System.out.println(-1);
    }
}