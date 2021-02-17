package ezAl.week01;

import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class B10828 {

	public static List list;
	
	public static void Do(String param){
		String[]  arrParam = param.split(" ");
		
		//PUSH
		if(arrParam[0].toUpperCase().equals("PUSH")){
			if(arrParam[1] == null || arrParam[1].isEmpty() )
			{
				return;
			}
			else
			{
				list.add(arrParam[1]);
			}
		}
		//POP
		else if (arrParam[0].toUpperCase().equals("POP")) {		
			if(list.size() > 0){
				System.out.println(list.get(list.size()-1));
				list.remove(list.size()-1);
			}else{
				System.out.println("-1");
			}
		}
		//SIZE
		else if (arrParam[0].toUpperCase().equals("SIZE")) {
			System.out.println(list.size());
		}
		//EMPTY
		else if (arrParam[0].toUpperCase().equals("EMPTY")) {
			if(list.size()>0){
				System.out.println("0");
			}
			else{
				System.out.println("1");
			}
		}
		//TOP
		else if (arrParam[0].toUpperCase().equals("TOP")) {
			if(list.size()>0){
				System.out.println(list.get(list.size()-1));
			}
			else{
				System.out.println("-1");
			}
		}
	}//end of Do method
	
	public static void main(String[] args) {
		
		list = new LinkedList<String>();
		
		//Input
		Scanner scan = new Scanner(System.in);
		
		int arrLen  =  scan.nextInt();
		if(arrLen < 0) return;		
		String[] arr = new String[arrLen];
		
		scan = new Scanner(System.in);
		for (int i = 0; i < arr.length; i++) {
			arr[i] = scan.nextLine();
		}
		
		//Output
		for (String string : arr) {
			Do(string);
		}					
	}//end of main method

}
