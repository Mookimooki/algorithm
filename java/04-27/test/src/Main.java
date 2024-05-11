import java.util.Stack;

public class Main {
    static int n = 3, m = 2;
    static int[] numbers = new int[] {3, 6, 9};
    static int[] visited = new int[n];

    private void dfs(int length, Stack<Integer> arr, int maxNumber, int maxCount){
        if(length == maxCount){
            System.out.println(arr.stream().toList());
            return;
        }

        for(int i = 0; i < maxNumber; i++){
            if(visited[i] == 1) continue;
            visited[i] = 1;
            arr.push(numbers[i]);
            dfs(length + 1, arr, maxNumber, maxCount);
            arr.pop();
            visited[i] = 0;
        }
    }
    public static void main(String[] args) {
        Main main = new Main();
        main.dfs(0, new Stack<>(), n, m);
    }
}