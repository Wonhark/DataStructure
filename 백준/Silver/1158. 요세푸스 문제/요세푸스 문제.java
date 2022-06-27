import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int num = Integer.parseInt(st.nextToken());
        int dist = Integer.parseInt(st.nextToken());


        Queue<Integer> queue = new LinkedList<>();
        for (int i=1; i<=num; i++){
            queue.add(i);
        }

        sb.append("<");
        for (int i=0; i<num; i++){
            for (int j=0; j<dist-1; j++){
                queue.add(queue.poll());
            }
            sb.append(queue.poll() + ", ");
        }
        sb.delete(sb.length()-2, sb.length()).append(">");

        System.out.println(sb);
    }
}
