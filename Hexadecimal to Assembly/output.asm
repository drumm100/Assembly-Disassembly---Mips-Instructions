.text
.globl  main

main:
	lui, $t1, 0x123
	lw, $t1, -10($t2)
	sw, $t1, -10($t2)
	addiu, $t3, $t9, -4
	xori, $s1, $s4, 5
	andi, $t3, $t0, 9
	sub, $t1, $s3, $s4
	sltiu, $a1, $a3, 6
	or, $t0, $t1, $t2
	sll, $t1, $t2, 4
	beq, $t1, $t2, volta, 11
	slt, $t1, $t2, $t3
	beq, $t5, $t8, denovo, 7
	addu, $t1, $t2, $s3
	subu, $t7, $t6, $t4
	srl, $t0, $t1, 4
	srl, $t0, $t1, 4
	bne, $t0, $t6, label3, 0

label3
	sub, $t1, $s3, $s4
	or, $t0, $t1, $t2

denovo
	slt, $t1, $t2, $t3
	subu, $t7, $t6, $t4

volta
	sll, $t1, $t2, 4
	slt, $t1, $t2, $t3
