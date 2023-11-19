class Main inherits IO
    a: Int;
    b: Int;
    c: Int;
    d: Int;

    
    var: Int <- 0;

    main() : Int {
        {
           a <- 4;
           c <- 5;
           d <- 6
           (if a < 5 then b <- c else b <- d fi);
        }
    };
};