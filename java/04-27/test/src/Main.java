import java.util.*;
import java.util.stream.Collectors;

public class Main {

    private List<int [][]> bfs(int[][] spaces, int target){
        List<List<int []>> pieces = new ArrayList<>();
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        Queue<int[]> queue = new LinkedList<>();

        for (int i = 0; i < spaces.length; i++) {
            for (int j = 0; j < spaces[i].length; j++) {
                if (spaces[i][j] == target) {
                    queue.add(new int[]{i, j});
                    List<int []> newSpace = new ArrayList<>();
                    pieces.add(newSpace);

                    while (!queue.isEmpty()) {
                        int size = queue.size();
                        for (int k = 0; k < size; k++) {
                            int[] cur = queue.poll();
                            int x = cur[0], y = cur[1];

                            if(x < 0 || x >= spaces.length || y < 0 || y >= spaces[0].length || spaces[x][y] != target) continue;

                            spaces[x][y] = -1;
                            newSpace.add(new int[]{x, y});
                            for (int[] direction : directions) {
                                queue.add(new int[]{x + direction[0], y + direction[1]});
                            }
                        }
                    }
                }
            }
        }

        List<int [][]> answer = new ArrayList<>();
        for (List<int []> piece : pieces) {
            int minX = piece.stream().min(Comparator.comparing(p -> p[0])).get()[0];
            int minY = piece.stream().min(Comparator.comparing(p -> p[1])).get()[1];

            piece = piece.stream().map(point -> {
                point[0] -= minX;
                point[1] -= minY;
                return point;
            }).collect(Collectors.toList());

            int maxX = piece.stream().max(Comparator.comparing(p -> p[0])).get()[0];
            int maxY = piece.stream().max(Comparator.comparing(p -> p[1])).get()[1];

            int[][] matrix = new int[maxX+1][maxY+1];
            for (int i = 0; i < piece.size(); i++)
                matrix[piece.get(i)[0]][piece.get(i)[1]] = 1;
            answer.add(matrix);
        }

        return answer;
    }

    public int solution(int[][] game_board, int[][] table) {
        List<int [][]> spaces = bfs(game_board, 0);
        List<int [][]> pieces = bfs(table, 1);

        boolean[] checked = new boolean[pieces.size()];
        int answer = 0;

        for (int i = 0; i < spaces.size(); i++) {
            for (int j = 0; j < pieces.size(); j++) {
                if (checked[j]) continue;
                if(matchPiece(spaces.get(i), pieces.get(j))) {
                    checked[j] = true;
                    answer += (int) Arrays.stream(pieces.get(j)).flatMapToInt(Arrays::stream).filter(p -> p == 1).count();
                    break;
                }
            }
        }
        return answer;
    }
    private boolean matchPiece(int[][] space, int[][] piece) {
        if(space.length * space[0].length != piece.length * piece[0].length) return false;
        if(space.length != piece.length && space[0].length != piece.length) return false;

        if(Arrays.deepEquals(space, piece)) return true;
        int[][] rotatedPiece = piece;

        for (int i = 0; i < 3; i++) {
            rotatedPiece = rotatePiece(rotatedPiece);
            if(Arrays.deepEquals(space, rotatedPiece))
                return true;
        }
        return false;
    }
    private int[][] rotatePiece(int[][] piece) {
        int[][] newPiece = new int[piece[0].length][piece.length];
        for (int i = 0; i < piece.length; i++) {
            for (int j = 0; j < piece[i].length; j++) {
                newPiece[j][piece.length - i - 1] = piece[i][j];
            }
        }
        return newPiece;
    }

    public static void main(String[] args) {
        Main main = new Main();
        System.out.println(main.solution(
                new int[][]{
                        {1, 1, 0, 0, 1, 0},
                        {0, 0, 1, 0, 1, 0},
                        {0, 1, 1, 0, 0, 1},
                        {1, 1, 0, 1, 1, 1},
                        {1, 1, 0, 0, 1, 0},
                        {0, 1, 0, 1, 0, 0}
                },
                new int[][]{
                        {1, 0, 0, 1, 1, 0},
                        {1, 0, 1, 0, 1, 0},
                        {0, 1, 1, 0, 1, 1},
                        {0, 0, 1, 0, 0, 0},
                        {1, 1, 0, 1, 1, 0},
                        {0, 1, 0, 0, 0, 0}
                }
        ));

        System.out.println(main.solution(
                new int[][] {{0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,0}, {1,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1}, {0,1,1,1,0,0,1,0,1,0,0,1,1,0,1,0,0,0}, {0,0,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0}, {0,1,1,1,0,0,1,1,1,1,0,1,1,1,0,1,1,1}, {1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0}, {0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,0,0,1}, {1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0}, {0,0,1,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0}, {1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,1}, {0,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,1,0}, {1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0}, {0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1,0,0}, {1,0,1,1,0,1,1,0,0,0,1,0,0,0,1,0,0,1}, {1,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0}, {0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0}, {0,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,0}, {0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0}},
                new int[][] {{1,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,1,0}, {0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1,1,0}, {1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,1,0,1}, {1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,0,1}, {1,1,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,1}, {0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,0,0}, {1,1,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,1}, {0,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0}, {1,0,1,0,0,0,0,1,0,1,1,0,1,1,0,1,1,1}, {1,0,1,0,1,1,1,1,0,1,1,0,0,0,1,1,1,0}, {1,1,0,1,0,0,0,0,1,0,0,1,1,1,0,0,0,0}, {0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,1,0,1}, {1,1,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1}, {1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1}, {0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,0,0}, {1,1,1,0,1,0,0,1,0,1,1,0,0,1,0,1,0,1}, {0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,1,1}, {0,1,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1}}
        ));
    }
}