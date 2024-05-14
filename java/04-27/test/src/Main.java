import java.util.Scanner;

public class Main {;
    static int[] findAndUnion;
    public int find(int value){
        if (findAndUnion[value] == value) return value;
        return findAndUnion[value] = find(findAndUnion[value]);
    }
    public void union(int a, int b){
        int findA = find(a);
        int findB = find(b);
        findAndUnion[findA] = findB;
    }


    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();

        findAndUnion = new int[n+1];
        for (int i = 1; i <= n; i++) findAndUnion[i] = i;

        int[][] input = new int[m+1][2];
        for (int i = 1; i <= m; i++) {
            input[i][0] = scanner.nextInt();
            input[i][1] = scanner.nextInt();
        }

        for (int i = 1; i <= m; i++) {
            main.union(input[i][0], input[i][1]);
        }

        if(main.find(scanner.nextInt()) == main.find(scanner.nextInt()))
            System.out.println("YES");
        else
            System.out.println("NO");
    }
}