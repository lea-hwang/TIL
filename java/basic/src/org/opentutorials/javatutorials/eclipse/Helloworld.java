package org.opentutorials.javatutorials.eclipse;

public class Helloworld {

	public static void main(String[] args) {
		// 변수: 변하지 않는 값
		int a;
		a = 3;
		System.out.println(a);
		
		double b;
		b = 3;
		System.out.println(b);
		
		double c = 34;
		System.out.println(c);

//-----------------------------------------------------------------------------------
				
/*		
		String first;
		first = "coding";
*/
		String first = "coding";
		System.out.println(first);

//-----------------------------------------------------------------------------------

//		byte d; // -128~127까지 사용가능
//		long e; // 2^32 개 표현가능
//		char f; // 2byte
		
//-----------------------------------------------------------------------------------
		// 상수: 그 값을 변경할 수 없는 데이터 타입
		// 1, 2.3
		
		// 상수에도 데이터타입이 존재!!
		float g = 2.2F; 				// float에 할당하기 위해선 F를 명시적으로 표현하기 위해 뒤에 붙여줘야함.
		double h = 2.2;
		long i = 2147483648L; 	// long에 할당하기 위해서는 L을 따로 붙여줘야함.
		
		// short, byte는 따로 붙여주지 않아도 됨
		
//-----------------------------------------------------------------------------------
		// 자동 형 변환
		double j = 3.0F; 			// 자동으로 float -> double로 형 변환해줌(float < double)
		
		// byte -> short -> int -> long -> float -> double
		// 				char -> 
		
//-----------------------------------------------------------------------------------
		// 명시적 형변환(Explicit Conversion)
		int k = (int)100.0F;  		// 앞에 (int) 를 붙여 float -> int로 형변환할 수 있다.
		
//-----------------------------------------------------------------------------------
		// 이항연산자
		// + - * / %
		
		// 연산
		int l = 10;
		int n = 3;
		float m = 3.0F;
		
		System.out.println(l/m); // 정수/실수 -> 실수
		System.out.println(l/n); // 정수/정수 -> 정수

//-----------------------------------------------------------------------------------
		// 단항연산자
		// +(양수) -(음수) ++ --

//-----------------------------------------------------------------------------------
		// 불린(Boolean): 참과 거짓을 의미
		// true / false
		boolean isTrue = (1==1);
		boolean isFalse = (1==3);
		System.out.println(isTrue);
		System.out.println(isFalse);
		
		String hi = "hi";
		String hi2 = new String("hi");
		System.out.println(hi==hi2); 				// false
		System.out.println(hi.equals(hi2)); 	// 문자열 비교할 때 equals 사용
		
//-----------------------------------------------------------------------------------
		// 조건문: if문
		
		Boolean isTrueFalse = true;
		Boolean isElseIf = true;
		
		if (isTrueFalse) {
			System.out.println("it's true");
		} else if (isElseIf) {
			
		} else {
			System.out.println("it's false");
		}
		
//-----------------------------------------------------------------------------------
		// 입력값 받기
		String id = args[0]; 		// args에 입력값이 담겨져있음
		System.out.println(id);
		
		
//-----------------------------------------------------------------------------------
		// switch 문
		
		int val = 4;
		switch (val) {
		case 1:
			System.out.println("one");
			break; // break를 작성하지 않으면 아래의 구문들이 모두 실행됨
		case 2:
			System.out.println("two");
			break;
		case 3:
			System.out.println("three");
			break;
		default: // 위의 case에 모두 포함되지 않았을 때 실행되는 구문임
			System.out.println("default");
		}
		
//-----------------------------------------------------------------------------------
		// 논리연산자
		//  &&(and) ||(or) !(not)
		System.out.println(true&&false);
		System.out.println(true||false);
		System.out.println(!false);
//-----------------------------------------------------------------------------------
		// 반복문 while
		int num = 3;
		while(num>0) {
			System.out.println(num--);
		}
//-----------------------------------------------------------------------------------
		// for 문
		for (int idx = 0; idx < 3; idx++) {
			System.out.println(idx);
			if (idx==2) {
				//break;
				continue;
			}
		}
		
//-----------------------------------------------------------------------------------
		// 배열
		
		// 배열 생성: 변수형[] 변수명 = {}; {} 안에 값들을 담아줌
		String[] name = {"heewon", "lea"};
		
		System.out.println(name[0]);
		
		// 선언, 배열크기 설정
		String[] students = new String[4]; // 4개의 칸인 배열 생성
		
		// 값 할당
		students[0] = "heewon";
		students[1] = "lea";
		System.out.println(students.length); //4
				
//-----------------------------------------------------------------------------------
		// 배열과 for문
		String[] members = {"p1", "p2", "p3"};
		for (int ii = 0; ii < members.length; ii++) {
			System.out.println(members[ii]);
		}
		
		// for-each: 배열을 탐색할때 각 값들을 받을 수 있음
		for (String member:members) { // member에 각 값들을 하나씩 받을 수 있음
			System.out.println(member);
		}
		
//-----------------------------------------------------------------------------------

		
		
//-----------------------------------------------------------------------------------

		
	}
}
