import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        final int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        final boolean[][] visited = new boolean[100][100];
        int answer = 0;

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{characterX, characterY});
        visited[characterX][characterY] = true;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] point = queue.poll();
                if (point[0] == itemX && point[1] == itemY)
                    return answer;

                for (int[] direction : directions) {
                    int newX = point[0] + direction[0];
                    int newY = point[1] + direction[1];

                    if(newX < 0 || newY < 0 || visited[newX][newY]) continue;
                    if(!isOnRectangle(rectangle, point[0] + (double) direction[0]/2,  point[1] + (double) direction[1]/2)) continue;
                    queue.add(new int[]{newX, newY});
                    visited[newX][newY] = true;
                }
            }
            answer++;
        }

        return -1;
    }
    private boolean isOnRectangle(int[][] rectangle, double x, double y) {
        boolean onRectangle = false;
        for(int[] point : rectangle) {
            int bottomLeftX = point[0], bottomLeftY = point[1], topRightX = point[2], topRightY = point[3];
            if(x > bottomLeftX && topRightX > x && y > bottomLeftY && topRightY > y) return false;

            if (x == bottomLeftX || x == topRightX) {
                if (y >= bottomLeftY && y <= topRightY) onRectangle = true;
            } else if (y == topRightY || y == bottomLeftY) {
                if (x >= bottomLeftX && x <= topRightX) onRectangle = true;
            }
        }
        return onRectangle;
    }
    public static void main(String[] args) {
        Main main = new Main();
        System.out.println(main.solution(new int[][]{{1,1,7,4},{3,2,5,5},{4,3,6,9},{2,6,8,8}}, 1, 3, 7, 8));
    }
}