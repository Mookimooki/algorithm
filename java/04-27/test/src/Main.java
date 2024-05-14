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
    private int[] solution(List<List<Edge>> graph, int n, int start){
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
            for(Edge edge: graph.get(currentDestination)){
                if(distance[edge.dest] <= currentCost + edge.cost) continue;

                distance[edge.dest] = currentCost + edge.cost;
                pq.offer(new Edge(edge.dest, currentCost + edge.cost));
            }
        }

        return distance;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();

        List<List<Edge>> graph = new ArrayList<>();
        for(int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for(int i = 0; i < m; i++){
            graph.get(scanner.nextInt()).add(new Edge(scanner.nextInt(), scanner.nextInt()));
        }

        main.solution(graph, n, 1);
    }
}