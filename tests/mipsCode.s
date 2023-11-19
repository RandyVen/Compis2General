addi $sp, $sp, -4
jal mainMain
innitMain:
   sw $ra 0($sp)
mainMain:
   sw $ra 0($sp)
   addi $sp, $sp, -8
   li $a0, 0
   li $v0, 9
   syscall
   addi $sp, $sp, -4
   addi $sp, $sp , -0
   addi $sp, $sp , 0
   jal type_nameObject
   addi $sp, $sp , -0
   addi $sp, $sp, 0
   addi $sp, $sp, 4
   addi $sp, $sp, -12
   sw $v0, 4($sp)
   li $t0, 1
   sw $t0, 12($sp)
   addi $sp, $sp , -4
   sw $t0, 0($sp)
   addi $sp, $sp , 4
   jal substrString
   addi $sp, $sp , -4
   lw $t0, 0($sp)
   addi $sp, $sp, 4
   addi $sp, $sp, 12
   sw $v0, 4($sp)
   addi $sp, $sp , -4
   sw $t0, 0($sp)
   addi $sp, $sp , 4
   jal out_stringIO
   addi $sp, $sp , -4
   lw $t0, 0($sp)
   addi $sp, $sp, 4
   addi $sp, $sp, 8
   addi $sp, $sp, -8
   addi $sp, $sp, -4
   addi $sp, $sp , -4
   sw $t0, 0($sp)
   addi $sp, $sp , 4
   jal type_nameObject
   addi $sp, $sp , -4
   lw $t0, 0($sp)
   addi $sp, $sp, 4
   addi $sp, $sp, 4
   addi $sp, $sp, -12
   li $t1, 1
   sw $t1, 4($sp)
   li $t2, 3
   sw $t2, 12($sp)
   addi $sp, $sp , -12
   sw $t0, 0($sp)
   sw $t1, 4($sp)
   sw $t2, 8($sp)
   addi $sp, $sp , 12
   jal substrString
   addi $sp, $sp , -12
   lw $t0, 0($sp)
   lw $t1, 4($sp)
   lw $t2, 8($sp)
   addi $sp, $sp, 12
   addi $sp, $sp, 12
   sw $v0, 4($sp)
   addi $sp, $sp , -12
   sw $t0, 0($sp)
   sw $t1, 4($sp)
   sw $t2, 8($sp)
   addi $sp, $sp , 12
   jal out_stringIO
   addi $sp, $sp , -12
   lw $t0, 0($sp)
   lw $t1, 4($sp)
   lw $t2, 8($sp)
   addi $sp, $sp, 12
   addi $sp, $sp, 8
   addi $sp, $sp, -8
   li $t3, "\n"
   sw $t3, 4($sp)
   addi $sp, $sp , -16
   sw $t0, 0($sp)
   sw $t1, 4($sp)
   sw $t2, 8($sp)
   sw $t3, 12($sp)
   addi $sp, $sp , 16
   jal out_stringIO
   addi $sp, $sp , -16
   lw $t0, 0($sp)
   lw $t1, 4($sp)
   lw $t2, 8($sp)
   lw $t3, 12($sp)
   addi $sp, $sp, 16
   addi $sp, $sp, 8
   li $v0, 10
   syscall
