public class Main {
    public int solution(int[] numbers, int target) {
        return dfs(0, 0, numbers, target);
    }

    public int dfs(int level, int sum, int[] numbers, int target) {
        if (level == numbers.length) {
            if(sum == target) return 1;
            return 0;
        }
        return dfs(level + 1, sum + numbers[level], numbers, target) + dfs(level + 1, sum - numbers[level], numbers, target);
    }

    public static void main(String[] args) {
        Main main = new Main();

        int[] numbers = new int[] {1, 1, 1, 1, 1};
        int target = 3;
        System.out.println(main.solution(numbers, target));

        numbers = new int[] {4, 1, 2, 1};
        target = 4;
        System.out.println(main.solution(numbers, target));
    }
}