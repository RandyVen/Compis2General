
class BooleanIfWhile {
    variable1: Int;
    variable2: Bool <- true;

    tryOut(): Int {{

        while 0 < 1000000000 loop {
            variable1;
        } pool;


        if variable2 then {
            variable1;
        } else {
            2;
        } fi;
    }};
};


class Main {
    main(): SELF_TYPE {
        self
    };
};