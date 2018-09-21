## No vectorization - add.c ##

If you compile this code,

```
void add(double *A, double *B) {
    for (int i=0; i<N; i++) {
        A[i] += B[i];
    }
}
```

using ```gcc add.c -o add``` and disassemble with ```objdump -d add```, then the following assembly is produced:

```
0000000000400567 <add>:
  400567:       55                      push   %rbp
  400568:       48 89 e5                mov    %rsp,%rbp
  40056b:       48 89 7d e8             mov    %rdi,-0x18(%rbp)
  40056f:       48 89 75 e0             mov    %rsi,-0x20(%rbp)
  400573:       c7 45 fc 00 00 00 00    movl   $0x0,-0x4(%rbp)
  40057a:       eb 50                   jmp    4005cc <add+0x65>
  40057c:       8b 45 fc                mov    -0x4(%rbp),%eax
  40057f:       48 98                   cltq
  400581:       48 8d 14 c5 00 00 00    lea    0x0(,%rax,8),%rdx
  400588:       00
  400589:       48 8b 45 e8             mov    -0x18(%rbp),%rax
  40058d:       48 01 d0                add    %rdx,%rax
  400590:       f2 0f 10 08             movsd  (%rax),%xmm1
  400594:       8b 45 fc                mov    -0x4(%rbp),%eax
  400597:       48 98                   cltq
  400599:       48 8d 14 c5 00 00 00    lea    0x0(,%rax,8),%rdx
  4005a0:       00
  4005a1:       48 8b 45 e0             mov    -0x20(%rbp),%rax
  4005a5:       48 01 d0                add    %rdx,%rax
  4005a8:       f2 0f 10 00             movsd  (%rax),%xmm0
  4005ac:       8b 45 fc                mov    -0x4(%rbp),%eax
  4005af:       48 98                   cltq
  4005b1:       48 8d 14 c5 00 00 00    lea    0x0(,%rax,8),%rdx
  4005b8:       00
  4005b9:       48 8b 45 e8             mov    -0x18(%rbp),%rax
  4005bd:       48 01 d0                add    %rdx,%rax
  4005c0:       f2 0f 58 c1             addsd  %xmm1,%xmm0
  4005c4:       f2 0f 11 00             movsd  %xmm0,(%rax)
  4005c8:       83 45 fc 01             addl   $0x1,-0x4(%rbp)
  4005cc:       83 7d fc 09             cmpl   $0x9,-0x4(%rbp)
  4005d0:       7e aa                   jle    40057c <add+0x15>
  4005d2:       90                      nop
  4005d3:       5d                      pop    %rbp
  4005d4:       c3                      retq
```

We can tell that this is not vectorized because the instructions being used have the suffix **sd** like movsd and addsd (with the "s" meaning "scalar"). 

## Vectorization - add_v.c ##

If you compile this code,
```
void add_v(double * restrict A, double * restrict B) {
    double *AA = __builtin_assume_aligned(A,16);
    double *BB = __builtin_assume_aligned(B,16);
    for (int i=0; i<N; i++) {
        AA[i] += BB[i];
    }
}
```

using ```gcc -O3 add_v.c -o add_v``` and disassemble, then we get:
```
0000000000400600 <add_v>:
  400600:       66 0f 28 07             movapd (%rdi),%xmm0
  400604:       66 0f 58 06             addpd  (%rsi),%xmm0
  400608:       0f 29 07                movaps %xmm0,(%rdi)
  40060b:       66 0f 28 47 10          movapd 0x10(%rdi),%xmm0
  400610:       66 0f 58 46 10          addpd  0x10(%rsi),%xmm0
  400615:       0f 29 47 10             movaps %xmm0,0x10(%rdi)
  400619:       66 0f 28 47 20          movapd 0x20(%rdi),%xmm0
  40061e:       66 0f 58 46 20          addpd  0x20(%rsi),%xmm0
  400623:       0f 29 47 20             movaps %xmm0,0x20(%rdi)
  400627:       66 0f 28 47 30          movapd 0x30(%rdi),%xmm0
  40062c:       66 0f 58 46 30          addpd  0x30(%rsi),%xmm0
  400631:       0f 29 47 30             movaps %xmm0,0x30(%rdi)
  400635:       66 0f 28 47 40          movapd 0x40(%rdi),%xmm0
  40063a:       66 0f 58 46 40          addpd  0x40(%rsi),%xmm0
  40063f:       0f 29 47 40             movaps %xmm0,0x40(%rdi)
  400643:       c3                      retq
  400644:       66 90                   xchg   %ax,%ax
  400646:       66 2e 0f 1f 84 00 00    nopw   %cs:0x0(%rax,%rax,1)
  40064d:       00 00 00
```

We can tell this ***is vectorized*** because the instructions are different. The **addpd** is the add instruction for "packed" values ("add two, four or eight packed double-precision floating-point values", [link](https://www.felixcloutier.com/x86/ADDPD.html)).











 
