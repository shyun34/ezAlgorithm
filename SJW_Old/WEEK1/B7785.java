package ezAl.week01;

import java.util.*;

public class B7785 {

	public static void main(String[] args) {
		
		HashMap<String, String> obj = new HashMap<String,String>();
		Scanner sc = new Scanner(System.in);
		
		//Input		
		int arrLen  =  sc.nextInt();
		if(arrLen < 0) return;		
		
		String[] arr = new String[arrLen];
		
		String name = null;
		String condition = null;
		for (int i = 0; i < arr.length; i++) {
			name = sc.next();
			condition = sc.next();
			
			if(condition.equals("enter")){
				obj.put(name, condition);
			}
			else{
				obj.remove(name);
			}
		}
		sc.close();
		
		//sort
		Object[] mapKey = obj.keySet().toArray();
		Arrays.sort(mapKey,Collections.reverseOrder());
		
		//output
		for (Object object : mapKey) {
			System.out.println(object);
		}
		
	}// end of main method

}
