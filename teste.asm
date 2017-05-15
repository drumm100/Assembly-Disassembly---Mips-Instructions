.text
.globl  main

 teste2:
 	slt $t1, $t2, $t3
 
 main:
	sub $t1, $s3, $s4
	or $t0, $t1, $t2
	beq $t1, $t5, loop
	sll $t1, $t2, 4
	slt $t1, $t2, $t3
	bne $t5, $t8, teste
	addu $t1, $t2, $s3
	subu $t7, $t6, $t4
	beq $t7, $t6, teste2
	srl $t0, $t1, 4
	srl $t0, $t1, 4

teste:
	sub $t1, $s3, $s4
	or $t0, $t1, $t2

loop:
	slt $t1, $t2, $t3
	addu $t1, $t2, $s3
