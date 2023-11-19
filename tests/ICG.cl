class Main {
    a: Int;
    b: Int;
    c: Int;
    d: Int;

    main() : Int {
        {
           a <- 4;
           c <- 5;
           d <- 6
           (if a < 5 then b <- c else b <- d fi);
        }
    };
};