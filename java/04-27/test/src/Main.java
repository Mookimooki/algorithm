import java.util.*;

class Edge implements Comparable<Edge> {
    int dest;
    int cost;

    Edge(int dest, int cost) {
        this.dest = dest;
        this.cost = cost;
    }

    @Override
    public int compareTo(Edge o) {
        return Integer.compare(this.cost, o.cost);
    }
}

public class Main {
    private int[] solution(int[][] graph, int n, int start){
        int[] distance = new int[n+1];
        Arrays.fill(distance, Integer.MAX_VALUE);

        PriorityQueue<Edge> pq = new PriorityQueue<>();
        pq.offer(new Edge(start, 0));
        distance[start] = 0;

        while(!pq.isEmpty()) {
            Edge curr = pq.poll();
            int currentDestination = curr.dest;
            int currentCost = curr.cost;

            if(distance[currentDestination] < currentCost) continue;
            for(int i = 1; i <= n; i++){
                if(i == start || graph[currentDestination][i] == -1) continue;

                if(distance[i] > currentCost + graph[currentDestination][i]){
                    distance[i] = currentCost + graph[currentDestination][i];
                    pq.offer(new Edge(i, distance[i]));
                }
            }
        }

        return distance;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();

        int[][] graph = new int[n+1][n+1];
        for(int i = 0; i <= n; i++) {
            Arrays.fill(graph[i], -1);
        }
        for(int i = 0; i < m; i++){
            graph[scanner.nextInt()][scanner.nextInt()] = scanner.nextInt();
        }

        main.solution(graph, n, 1);
    }
}