	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 26, 0	sdk_version 26, 2
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	mov	w8, #0                          ; =0x0
	str	w8, [sp, #16]                   ; 4-byte Folded Spill
	stur	wzr, [x29, #-4]
	mov	w0, #5                          ; =0x5
	mov	w1, #7                          ; =0x7
	bl	_add
	stur	w0, [x29, #-8]
	mov	w8, #5210                       ; =0x145a
	movk	w8, #17309, lsl #16
	fmov	s0, w8
	stur	s0, [x29, #-12]
	ldur	w8, [x29, #-8]
                                        ; kill: def $x8 killed $w8
	mov	x9, sp
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	ldur	s0, [x29, #-12]
	fcvt	d0, s0
	mov	x8, sp
	str	d0, [x8]
	adrp	x0, l_.str.1@PAGE
	add	x0, x0, l_.str.1@PAGEOFF
	bl	_printf
	ldr	w0, [sp, #16]                   ; 4-byte Folded Reload
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"Sum of 5 + 7: %d\n"

l_.str.1:                               ; @.str.1
	.asciz	"Area of circle (radius 10): %f\n"

.subsections_via_symbols
