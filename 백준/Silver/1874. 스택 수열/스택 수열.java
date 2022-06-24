import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int times = Integer.parseInt(br.readLine());
        Stack<Integer> seq = new Stack<>();
        Stack<Integer> temp = new Stack<>();
        int push_num = 1;
        boolean success = true;
        for (int i=0; i<times; i++){
            int num = Integer.parseInt(br.readLine());
            if (push_num <= num){
                for (int j=push_num; j<=num; j++){
                    temp.push(j); push_num++;
                    sb.append("+\n");
                }
                seq.push(temp.pop()); sb.append("-\n");
            }
            else{
                if (temp.peek() != num) success = false;
                seq.push(temp.pop()); sb.append("-\n");

            }

        }
        if (success == false) System.out.println("NO");
        else System.out.println(sb);



    }
}
