class Results {

    ress: Int; 

    get_ress() : Int {
        ress
    };

    set_res(i: Int) : SELF_TYPE {
        {
            ress <- i;
            self;
        }
    };
};

class Div {
    div(n: Int, o: Int) : Int {
        n/o
    };
};

class SumSub inherits Div {

    sum(n: Int, o: Int) : Int {
        n + o 
    };
    sub(n: Int, o: Int) : Int {
        n - o
    };
};

class Calculator inherits SumSub {
    mul(n: Int, o: Int) : Int {
        n*o
    };
};

class Main inherits IO {
    a : Results;
    calc: Calculator;
    m : Int;
    v : Int;

    main() : SELF_TYPE {
        {
            a.set_res(calc.mul(5,4));
            self;
        }
    } ;

};