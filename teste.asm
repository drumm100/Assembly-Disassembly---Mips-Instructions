.text
.globl  main


main:
	sub $t1, $s3, $s4
	or $t0, $t1, $t2
	sll $t1, $t2, 4
	slt $t1, $t2, $t3
	beq $t5, $t8, label
	beq $t1, $t2, volta
	addu $t1, $t2, $s3
	subu $t7, $t6, $t4
	beq $t7, $t6, loop
	srl $t0, $t1, 4
	srl $t0, $t1, 4
	bne $t0, $t6, denovo

volta:
	sll $t1, $t2, 4
	slt $t1, $t2, $t3

denovo:
	sub $t1, $s3, $s4
	or $t0, $t1, $t2

loop:
	slt $t1, $t2, $t3
	addu $t1, $t2, $s3

label:
 	slt $t1, $t2, $t3