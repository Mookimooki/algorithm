import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

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
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);

        int v = scanner.nextInt();
        int e = scanner.nextInt();

        int[][] graph = new int[e][3];
        for(int i = 0; i < e; i++) {
            graph[i][0] = scanner.nextInt();
            graph[i][1] = scanner.nextInt();
            graph[i][2] = scanner.nextInt();
        }

        System.out.println(main.solution(graph, v));
    }
}