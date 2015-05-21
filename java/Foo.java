

public class Foo {
	public static void main (String[] args) throws InterruptedException{
		
		Thread trd = new Thread () {
			
			public void run () {
				
				System.out.println("hel from trd");
			}
		};
		
		trd.start();
		Thread.yield();
		
		System.out.println("hel from main");
		
		trd.join();
	}
}