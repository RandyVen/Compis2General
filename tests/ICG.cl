class Factorial {
  	var: Int <- 0;
  	
  	factorial(n: Int) : Int {
      {( let f : Int in
      	 if n=0 then f<-0 else
         if n=1 then f<-1 else
        	 f<-n*factorial(n-1)
         fi fi
       );}
    };

    mul(n: Int, m: Int): Int {
        n * m
    };
  };

class Main inherits IO {
    n: Int;
  	m : Int;
    facto: Factorial;
    r: Int;

  	main() : Int {
	{
		n <- 3;
        m <- 4;
	    facto <- new Factorial;
        r <- facto.mul(n, m);
        facto.factorial(n);
	}
    };
};
