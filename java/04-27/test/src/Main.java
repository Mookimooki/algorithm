import java.util.Scanner;

public class Main {
    static int n, m;
    static int[] combi;
    private void dfs(int level, int number){
        if(level == m) {
            for (int i = 0; i < m; i++) {
                System.out.print(combi[i] + " ");
            }
            System.out.println();
            return;
        }

        for (int i = number; i <= n; i++) {
            combi[level] = i;
            dfs(level + 1, i + 1);
        }
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();
        combi = new int[m];

        main.dfs(0, 1);
    }
}