import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Main main = new Main();
        List matrix = new ArrayList<List<Integer>>() {{
            add(new ArrayList<Integer>() {{
                add(112);
                add(42);
                add(83);
                add(119);
            }});
            add(new ArrayList<Integer>() {{
                add(56);
                add(125);
                add(56);
                add(49);
            }});
            add(new ArrayList<Integer>() {{
                add(15);
                add(78);
                add(101);
                add(43);
            }});
            add(new ArrayList<Integer>() {{
                add(62);
                add(98);
                add(114);
                add(108);
            }});
        }};
        main.flippingMatrix(matrix);
    }

    public static int flippingMatrix(List<List<Integer>> matrix) {
        int n = matrix.size() / 2;
        int size = matrix.size();
        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                answer += Arrays.stream(new int[]{
                        matrix.get(i).get(j),
                        matrix.get(i).get(size - j - 1),
                        matrix.get(size - i - 1).get(j),
                        matrix.get(size - i - 1).get(size - j - 1)
                }).max().getAsInt();
            }
        }
        return answer;
    }
}