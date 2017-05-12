 .text
 .globl  main

 main:
	sub $t1, $s3, $s4
	or $t0, $t1, $t2
	sll $t1, $t2, 4
	slt $t1, $t2, $t3
	addu $t1, $t2, $s3
	subu $t7, $t6, $t4
	srl $t0, $t1, 4
