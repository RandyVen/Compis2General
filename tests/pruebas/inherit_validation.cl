class A {
    var1: String <- "hello";

    method1(param1: Int): String {
        var1
    };
};


class B inherits A {
    var2: String <- "world";

    method1(param1: Int): String {
        "Hola mundo!"
    };

    method2(): String {
        var2
    };
};

class C {
    class_a: A <- new A;
    class_b: B <- new B;

    test(): String {{
        class_a <- class_b;

        class_a.method1(1);

        class_b.method1(1);

        class_a@Object.type_name();
    }};
};

class Main {
    main(): SELF_TYPE {
        self
    };
};