import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Student20180955 {
	
	static ArrayList<Integer> result = new ArrayList<Integer>();
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int[][] switches = new int[10][];

		for (int i = 0; i < 10; i++) {
			String s = scanner.nextLine();
			String[] splitString = s.split(" ");
			int index = Integer.parseInt(splitString[0]);
			int length = Integer.parseInt(splitString[1]);
			switches[index] = new int[length];
			for (int j = 0; j < length; j++) {
				switches[index][j] = Integer.parseInt(splitString[j + 2]);
			}
		}
		
		int[] clock = new int[16];
		String s = scanner.nextLine();
		String[] splitString = s.split(" ");
		for (int i = 0; i < clock.length; i++) {
			clock[i] = Integer.parseInt(splitString[i]);
		}

		int[] bucket = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; 
		int[] items = {0, 1, 2, 3};
		
		solution(items, bucket, 10, switches, clock);
		System.out.println(Collections.min(result));
		scanner.close();
	}
	
	private static void solution(int[] items, int[] bucket, int k, int[][] switches, int[] clock) {
		if (k == 0) {			
			int[] temp = new int[16];
			for (int i = 0; i < temp.length; i++) {
				temp[i] = clock[i];
			}
			
			int count = 0;
			for (int i = 0; i < bucket.length; i++) {
				count += bucket[i];
				for (int j = 0; j < switches[i].length; j++) {
					temp[switches[i][j]] += 3 * bucket[i];
				}
			}
			
			int i;
			for (i = 0; i < temp.length; i++) {
				if (temp[i] % 12 != 0) {
					break;
				}
			}
			if (i == temp.length) {
				result.add(count);
			}
			
			return;
		}
		int lastIndex= bucket.length - k -1; 
		
		for(int i= 0; i < items.length; i++) 
		{
			bucket[lastIndex+1] = items[i];
			solution(items, bucket, k -1, switches, clock);
		}
	}

}
