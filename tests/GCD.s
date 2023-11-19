.data
num1:.asciiz"Primer Numero:"
num2: .asciiz"Segundo Numero:"

.text
.globl main
main:
    li $v0,4
    la $a0,num1
    syscall
    
    li  $v0, 5     
    syscall
    move $t0,$v0 
  
    li $v0,4
    la $a0,num2
    syscall

    li  $v0, 5      
    syscall
    move $a1,$v0
    move $a0,$t0    

    jal GCD #Calling GCD func

    add $a0,$v0,$zero 
    li $v0,1
    syscall # print result
    li $v0, 10 # exit the program
    syscall
    
GCD:

    addi $sp, $sp, -12
    sw $ra, 0($sp) # Func stored in stack
    sw $s0, 4($sp) # Value stored in stack
    sw $s1, 8($sp) # Value stored in stack

    add $s0, $a0, $zero) 
    add $s1, $a1, $zero 

    addi $t1, $zero, 0 # $t1 = 0
    beq $s1, $t1, return 

    add $a0, $zero, $s1 
    div $s0, $s1 # num1/num2
    mfhi $a1 

    jal GCD
    
exitGCD:
    lw $ra, 0 ($sp)  # read registers from stack
    lw $s0, 4 ($sp)
    lw $s1, 8 ($sp)
    addi $sp,$sp , 12 # bring back stack pointer
    jr $ra
return:
    add $v0, $zero, $s0 
    j exitGCD   