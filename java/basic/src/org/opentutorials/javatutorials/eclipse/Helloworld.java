package org.opentutorials.javatutorials.eclipse;

public class Helloworld {

	public static void main(String[] args) {
		// ����: ������ �ʴ� ��
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

//		byte d; // -128~127���� ��밡��
//		long e; // 2^32 �� ǥ������
//		char f; // 2byte
		
//-----------------------------------------------------------------------------------
		// ���: �� ���� ������ �� ���� ������ Ÿ��
		// 1, 2.3
		
		// ������� ������Ÿ���� ����!!
		float g = 2.2F; 				// float�� �Ҵ��ϱ� ���ؼ� F�� ��������� ǥ���ϱ� ���� �ڿ� �ٿ������.
		double h = 2.2;
		long i = 2147483648L; 	// long�� �Ҵ��ϱ� ���ؼ��� L�� ���� �ٿ������.
		
		// short, byte�� ���� �ٿ����� �ʾƵ� ��
		
//-----------------------------------------------------------------------------------
		// �ڵ� �� ��ȯ
		double j = 3.0F; 			// �ڵ����� float -> double�� �� ��ȯ����(float < double)
		
		// byte -> short -> int -> long -> float -> double
		// 				char -> 
		
//-----------------------------------------------------------------------------------
		// ����� ����ȯ(Explicit Conversion)
		int k = (int)100.0F;  		// �տ� (int) �� �ٿ� float -> int�� ����ȯ�� �� �ִ�.
		
//-----------------------------------------------------------------------------------
		// ���׿�����
		// + - * / %
		
		// ����
		int l = 10;
		int n = 3;
		float m = 3.0F;
		
		System.out.println(l/m); // ����/�Ǽ� -> �Ǽ�
		System.out.println(l/n); // ����/���� -> ����

//-----------------------------------------------------------------------------------
		// ���׿�����
		// +(���) -(����) ++ --

//-----------------------------------------------------------------------------------
		// �Ҹ�(Boolean): ���� ������ �ǹ�
		// true / false
		boolean isTrue = (1==1);
		boolean isFalse = (1==3);
		System.out.println(isTrue);
		System.out.println(isFalse);
		
		String hi = "hi";
		String hi2 = new String("hi");
		System.out.println(hi==hi2); 				// false
		System.out.println(hi.equals(hi2)); 	// ���ڿ� ���� �� equals ���
		
//-----------------------------------------------------------------------------------
		// ���ǹ�: if��
		
		Boolean isTrueFalse = true;
		Boolean isElseIf = true;
		
		if (isTrueFalse) {
			System.out.println("it's true");
		} else if (isElseIf) {
			
		} else {
			System.out.println("it's false");
		}
		
//-----------------------------------------------------------------------------------
		// �Է°� �ޱ�
		String id = args[0]; 		// args�� �Է°��� ���������
		System.out.println(id);
		
		
//-----------------------------------------------------------------------------------
		// switch ��
		
		int val = 4;
		switch (val) {
		case 1:
			System.out.println("one");
			break; // break�� �ۼ����� ������ �Ʒ��� �������� ��� �����
		case 2:
			System.out.println("two");
			break;
		case 3:
			System.out.println("three");
			break;
		default: // ���� case�� ��� ���Ե��� �ʾ��� �� ����Ǵ� ������
			System.out.println("default");
		}
		
//-----------------------------------------------------------------------------------
		// ��������
		//  &&(and) ||(or) !(not)
		System.out.println(true&&false);
		System.out.println(true||false);
		System.out.println(!false);
//-----------------------------------------------------------------------------------
		// �ݺ��� while
		int num = 3;
		while(num>0) {
			System.out.println(num--);
		}
//-----------------------------------------------------------------------------------
		// for ��
		for (int idx = 0; idx < 3; idx++) {
			System.out.println(idx);
			if (idx==2) {
				//break;
				continue;
			}
		}
		
//-----------------------------------------------------------------------------------
		// �迭
		
		// �迭 ����: ������[] ������ = {}; {} �ȿ� ������ �����
		String[] name = {"heewon", "lea"};
		
		System.out.println(name[0]);
		
		// ����, �迭ũ�� ����
		String[] students = new String[4]; // 4���� ĭ�� �迭 ����
		
		// �� �Ҵ�
		students[0] = "heewon";
		students[1] = "lea";
		System.out.println(students.length); //4
				
//-----------------------------------------------------------------------------------
		// �迭�� for��
		String[] members = {"p1", "p2", "p3"};
		for (int ii = 0; ii < members.length; ii++) {
			System.out.println(members[ii]);
		}
		
		// for-each: �迭�� Ž���Ҷ� �� ������ ���� �� ����
		for (String member:members) { // member�� �� ������ �ϳ��� ���� �� ����
			System.out.println(member);
		}
		
//-----------------------------------------------------------------------------------

		
		
//-----------------------------------------------------------------------------------

		
	}
}
