.text
.globl  main

main:
	lui, $t1, 0x123
	lw, $t1, -10($t2)
	sw, $t1, -10($t2)
	addiu, $t3, $t9, -4
	xori, $s1, $s4, 5
	andi, $t3, $t0, 9
	sltiu, $a1, $a3, 6
	slt, $t1, $t2, $t3
