import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Main {
    public static int maxRegion(List<List<Integer>> grid) {
        int result = 0;
        int[][] directions = new int[][] {{0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {-1, -1}, {1, -1}, {-1, 1}};
        int xSize = grid.size(), ySize = grid.get(0).size();

        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(i).size(); j++) {
                if(grid.get(i).get(j) != 1) continue;

                int answer = 0;
                queue.add(new int[]{i, j});
                while(!queue.isEmpty()) {
                    int size = queue.size();
                    for(int k = 0; k < size; k++) {
                        int[] cur = queue.poll();
                        int x = cur[0], y = cur[1];

                        if(x < 0 || x >= xSize || y < 0 || y >= ySize || grid.get(x).get(y) != 1) continue;
                        grid.get(x).set(y, 0);
                        answer++;

                        for(int[] direction : directions) {
                            queue.offer(new int[]{x + direction[0], y + direction[1]});
                        }
                    }
                }
                result = Math.max(answer, result);
            }
        }

        return result;
    }
    public static void main(String[] args) {
        System.out.println(maxRegion(new ArrayList<List<Integer>>(){{
            add(new ArrayList<Integer>(){{
               add(0);
               add(0);
               add(1);
               add(1);
            }});
            add(new ArrayList<Integer>(){{
                add(0);
                add(0);
                add(1);
                add(0);
            }});
            add(new ArrayList<Integer>(){{
                add(0);
                add(1);
                add(1);
                add(0);
            }});
            add(new ArrayList<Integer>(){{
                add(0);
                add(1);
                add(0);
                add(0);
            }});
            add(new ArrayList<Integer>(){{
                add(1);
                add(1);
                add(0);
                add(0);
            }});
        }}));
    }
}