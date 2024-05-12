import java.util.Scanner;

public class Main {
    static int[][] directions = {{0,1}, {0,-1}, {1,0}, {-1,0}};
    private static int dfs(int[] point, int[][] grid){
        if(point[0] == grid.length-1 && point[1] == grid[0].length-1) return 1;
        grid[point[0]][point[1]] = 1;

        int answer = 0;
        for(int[] direction : directions) {
            int x = point[0] + direction[0], y = point[1] + direction[1];
            if(x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || grid[x][y] == 1) continue;
            answer += dfs(new int[]{x, y}, grid);
        }

        grid[point[0]][point[1]] = 0;
        return answer;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] grid = new int[7][7];
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                grid[i][j] = scanner.nextInt();
            }
        }

        System.out.println(dfs(new int[]{0, 0}, grid));
    }
}