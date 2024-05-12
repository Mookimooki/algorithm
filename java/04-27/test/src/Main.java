import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public int bfs(int[][] tomatoes){
        Queue<int[]> queue = new LinkedList<>();
        for(int i = 0; i < tomatoes.length; i++){
            for(int j = 0; j < tomatoes[i].length; j++){
                if(tomatoes[i][j] == 1){
                    queue.add(new int[]{i, j});
                }
            }
        }

        if(queue.isEmpty()) return 0;

        int answer = -1;
        int[][] directions = {{0,1},{1,0},{0,-1},{-1,0}};
        while(!queue.isEmpty()){
            answer ++;
            int size = queue.size();
            for(int i = 0; i < size; i++){
                int[] arr = queue.poll();
                int x = arr[0], y = arr[1];
                for(int[] direction : directions){
                    int newX = x + direction[0], newY = y + direction[1];
                    if (newX < 0 || newX >= tomatoes.length || newY < 0 || newY >= tomatoes[0].length || tomatoes[newX][newY] != 0) continue;
                    tomatoes[newX][newY] = 1;
                    queue.add(new int[]{newX, newY});
                }
            }
        }

        for(int i = 0; i < tomatoes.length; i++){
            for(int j = 0; j < tomatoes[i].length; j++){
                if(tomatoes[i][j] == 0){
                    return -1;
                }
            }
        }


        return answer;
    }

    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        int[][] tomatoes = new int[n][m];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                tomatoes[i][j] = scanner.nextInt();
            }
        }
        System.out.println(main.bfs(tomatoes));
    }
}