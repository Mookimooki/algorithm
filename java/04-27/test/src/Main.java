import java.util.*;

class Edge {
    int dest;
    int weight;

    public Edge(int dest, int weight) {
        this.dest = dest;
        this.weight = weight;
    }
}

public class Main {
    int[] findAndUnion;
    public int find(int value){
        if(findAndUnion[value] != value){
            return findAndUnion[value] = find(findAndUnion[value]);
        }else return value;
    }
    public void union(int a, int b){
        int findA = find(a);
        int findB = find(b);
        findAndUnion[findA] = findB;
    }
    private int solution(int[][] graph, int length){
        int answer = 0;

        Arrays.sort(graph, Comparator.comparingInt(o -> o[2]));
        findAndUnion = new int[length+1];
        for(int i = 1; i <= length; i++) findAndUnion[i] = i;

        for(int[] edge : graph){
            if(find(edge[0]) == find(edge[1])) continue;
            union(edge[0], edge[1]);
            answer += edge[2];
        }

        return answer;
    }

    private int solution(List<List<Edge>> edges, int length){
        int answer = 0;
        boolean[] visited = new boolean[length+1];

        PriorityQueue<Edge> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.weight));
        pq.addAll(edges.get(1));
        visited[1] = true;

        while(!pq.isEmpty()){
            Edge edge = pq.poll();

            if(visited[edge.dest]) continue;
            visited[edge.dest] = true;
            answer += edge.weight;

            pq.addAll(edges.get(edge.dest));
        }

        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);

        int v = scanner.nextInt();
        int e = scanner.nextInt();

        int[][] graph = new int[e][3];
        List<List<Edge>> edges = new ArrayList<>();
        for(int i = 0; i <= v; i++)
            edges.add(new ArrayList<>());


        for(int i = 0; i < e; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int c = scanner.nextInt();
            edges.get(a).add(new Edge(b, c));
            edges.get(b).add(new Edge(a, c));
        }
        System.out.println(main.solution(edges, v));
    }
}