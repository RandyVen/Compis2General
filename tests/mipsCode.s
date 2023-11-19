addi $sp, $sp, -0
jal mainMain
innitMain:
mainMain:
   add $t0, $t0, "Hello, World.\n"
   sw $t0, 0($sp)
   add $v0, this, $zero
