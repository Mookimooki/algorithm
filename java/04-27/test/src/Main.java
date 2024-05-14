import java.util.*;

class Point {
    int x;
    int y;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static List<Point> house, pizzaStores;
    static int[] combi;
    static int answer = Integer.MAX_VALUE;

    private void dfs(int level, int s, int m){
        if(level == m){
            int sum = 0;
            for(Point home: house){
                int minimumDistance = Integer.MAX_VALUE;
                for(int i : combi){
                    Point pizzaStore = pizzaStores.get(i);
                    int distanceX = Math.abs(pizzaStore.x - home.x);
                    int distanceY = Math.abs(pizzaStore.y - home.y);
                    minimumDistance = Math.min(distanceX + distanceY, minimumDistance);
                }
                sum += minimumDistance;
            }
            answer = Math.min(answer, sum);
            return;
        }

        for(int i = s; i < pizzaStores.size(); i++){
            combi[level] = i;
            dfs(level+1, i, m);
        }
    }

    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(), m = scanner.nextInt();

        house = new ArrayList<>();
        pizzaStores = new ArrayList<>();

        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++) {
                int value = scanner.nextInt();
                if(value == 1){
                    house.add(new Point(i, j));
                }else if(value == 2){
                    pizzaStores.add(new Point(i, j));
                }
            }

        combi = new int[m];
        main.dfs(0, 0, m);
        System.out.println(answer);
    }
}