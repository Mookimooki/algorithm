public class Main {
    static int n = 33, r = 19;
    static int[][] answer = new int[n+1][n+1];

    private int dfs(int n, int r){
        if(answer[n][r] != 0) return answer[n][r];
        if(r == 0 || n == r) return answer[n][r] = 1;
        if(r == 1) return answer[n][r] = n;

        return answer[n][r] = dfs(n-1, r-1) + dfs(n-1, r);
    }
    public static void main(String[] args) {
        Main main = new Main();
        System.out.println(main.dfs(n, r));
    }
}