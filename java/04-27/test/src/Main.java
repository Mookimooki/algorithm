import java.util.Arrays;
import java.util.Comparator;
import java.util.Stack;

public class Main {
    static boolean flag;
    static String[] answer;
    static boolean[] visited;

    public String[] solution(String[][] tickets) {
        Arrays.sort(tickets, new Comparator<String[]>() {
            @Override
            public int compare(String[] o1, String[] o2) {
                if(o1[0].equals("ICN") && o2[0].equals("ICN")) return o1[1].compareTo(o2[1]);
                if(o1[0].equals("ICN")) return -1;
                if(o2[0].equals("ICN")) return 1;

                if(o1[0].compareTo(o2[0]) == 0)
                    return o1[1].compareTo(o2[1]);
                return o1[0].compareTo(o2[0]);
            }
        });

        flag = false;
        visited = new boolean[tickets.length];
        Stack<String> stack = new Stack<>();

        for(int i = 0; i < tickets.length; i++) {
            if(tickets[i][0].equals("ICN")) {
                stack.push(tickets[i][0]);
                visited[i] = true;
                dfs(1, tickets[i][1], stack, tickets);
                visited[i] = false;
                stack.pop();
            }else break;
        }
        return answer;
    }
    private void dfs(int level, String next, Stack<String> stack, String[][] tickets){
        if(flag) return;
        if(tickets.length == level) {
            stack.push(next);
            answer = stack.toArray(new String[0]);
            flag = true;
            return;
        }
        for(int i = 0; i < tickets.length; i++) {
            if(!visited[i] && tickets[i][0].equals(next)) {
                stack.push(tickets[i][0]);
                visited[i] = true;
                dfs(level + 1, tickets[i][1], stack, tickets);
                visited[i] = false;
                stack.pop();
            }
        }
    }

    public static void main(String[] args) {
        Main main = new Main();
        System.out.println(Arrays.stream(main.solution(new String[][]{{"ICN", "JFK"}, {"HND", "IAD"}, {"JFK", "HND"}})).toList());
        System.out.println(Arrays.stream(main.solution(new String[][]{{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"}, {"ATL", "SFO"}})).toList());
    }
}