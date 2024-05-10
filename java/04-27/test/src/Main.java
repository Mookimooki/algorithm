import java.util.Stack;

public class Main {
    private String solution(String string){
        char[] charString = string.toCharArray();
        Stack<Character> stringStack = new Stack<>();
        Stack<Integer> digitStack = new Stack<>();

        for (int i = 0; i < string.length(); i++) {
            if(Character.isDigit(charString[i])){
                String tmpDigit = "";
                int j = i;
                while(Character.isDigit(charString[j])){
                    tmpDigit += charString[j++];
                }
                i = j;
                digitStack.push(Integer.parseInt(tmpDigit));
            }

            if(Character.isAlphabetic(charString[i])){
                stringStack.push(charString[i]);
            } else if(charString[i] == '['){
                stringStack.push(charString[i]);
            } else if(charString[i] == ']'){
                String tmpString = "";
                while (stringStack.peek() != '['){
                    tmpString = stringStack.pop() + tmpString;
                }
                stringStack.pop();
                int digit = digitStack.pop();
                for(int j = 0; j < digit; j++){
                    for(char ch: tmpString.toCharArray()){
                        stringStack.push(ch);
                    }
                }
            }
        }

        String answer = "";
        while(!stringStack.empty()){
            answer = stringStack.pop() + answer;
        }

        return answer;
    }
    public static void main(String[] args) {
        Main main = new Main();
        String[] input = {"3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"};

        for(String s : input){
            System.out.println(main.solution(s));
        }
    }
}