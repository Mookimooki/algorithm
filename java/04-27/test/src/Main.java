import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Main main = new Main();

        for (Integer answer: main.countingSort(new ArrayList<>() {{
            add(1);
            add(1);
            add(1);
            add(63);
            add(25);
            add(73);
            add(98);
            add(73);
            add(56);
            add(84);
            add(86);
            add(57);
            add(16);
            add(83);
            add(8);
        }}))
            System.out.print(answer + " ");
    }

    public List<Integer> countingSort(List<Integer> arr) {
        List<Integer> count = new ArrayList<>(Collections.nCopies(100, 0));

        for (int i = 0; i < arr.size(); i++) {
            count.set(arr.get(i), count.get(arr.get(i)) + 1);
        }
        return count;
    }
}