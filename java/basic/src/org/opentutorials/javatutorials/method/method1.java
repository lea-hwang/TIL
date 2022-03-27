package org.opentutorials.javatutorials.method;

public class method1 {
	public static String[] getMembers() {
		String[] members = {"hw", "dh"};
		return members;
	}
	
	public static int func1(int input1) {
		System.out.println("func1");
		System.out.println(input1);
		return input1 + 5;
	}

	public static void main(String[] args) {
		
		System.out.println("main");
		int result = func1(5);
		System.out.println(result);
		
		String[] members = getMembers();
		
		//-----------------------------------------------
		// 현재 파일 실행 java -cp bin org.opentutorials.javatutorials.method.method1 입력값 입력값
		System.out.println(args.length); 
	}

}
