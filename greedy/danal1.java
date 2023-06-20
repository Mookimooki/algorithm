public long solution6(int r, int c) {
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();

        for(int i = r + c - 2; i > r - 1; i--)
            list1.add(i);

        for(int i = c - 1; i > 1; i--)
            list2.add(i);
        
        while(list2.size() > 0)
            for(int i = 0; i < list1.size(); i ++){
                for(int j = 0; j < list2.size(); j ++){
                    if(list1.get(i) % list2.get(j) == 0){
                        int temp = list1.get(i) / list2.get(j);
                        list1.set(i, temp);
                        if(temp == 1) list2.remove(j);
                        list2.remove(j);
                        break;
                    }
                    else if(list1.get(i) < list2.get(j)){
                        break;
                    }
                }
            }

        int answer = 1;
        for(Integer i: list1)
            answer *= i;

        return answer;
        // return method1(r+c-2, r-1) / method1(c-1, 1);
    }