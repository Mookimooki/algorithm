import java.util.*;

class Lecture implements Comparable<Lecture> {
    int days;
    int money;

    public Lecture(int money, int days) {
        this.money = money;
        this.days = days;
    }

    @Override
    public int compareTo(Lecture o) {
        return Integer.compare(o.days, this.days);
    }
}

public class Main {
    private int solution(List<Lecture> lectures){
        int answer = 0;
        PriorityQueue<Lecture> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(o2.money, o1.money));
        Collections.sort(lectures);

        int day = lectures.get(0).days;
        int j = 0;
        for(int i = day; i > 0; i--) {
            while (true) {
                if(j == lectures.size() || lectures.get(j).days != i) break;
                pq.add(lectures.get(j));
                j++;
            }
            if(!pq.isEmpty())
                answer += pq.poll().money;
        }

        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();

        List<Lecture> lectures = new ArrayList<>();
        for (int i = 0; i < count; i++) {
            Lecture lecture = new Lecture(scanner.nextInt(), scanner.nextInt());
            lectures.add(lecture);
        }

        System.out.println(main.solution(lectures));
    }
}