# TryHackMe-Intro to x86-x64

Username : zx 
password : reismyfavl33t

SSH into the machine with these credentials.

## Task 2

Executing `intro` binary will produce this result

```
tryhackme@ip-10-10-213-153:~/introduction$ ./intro 
value for a is 1 and b is 2
value of a is 2 and b is 1

```

To debug this we use `radare` .

`r2 -d intro`

```
tryhackme@ip-10-10-213-153:~/introduction$ r2 -d intro
Process with PID 1507 started...
= attach 1507 1507
bin.baddr 0x55ebd6a73000
Using 0x55ebd6a73000
asm.bits 64
 -- Ask not what r2 can do for you - ask what you can do for r2
[0x7fdc18484090]> 
```

Using command `aa` will scan for all symbols and entry points in the executable.

```
[0x7fdc18484090]> aa
[x] Analyze all flags starting with sym. and entry0 (aa)
[0x7fdc18484090]> 
```

Finding list of functions in `radare` is command `afl` that returns a list of functions in a binary

<img src="https://imgur.com/xFzPNnK.png"/>

Now to analyze a function we use a command `pdf @function_name` which stands for print disassembly function


<img src="https://imgur.com/ITXqI1O.png"/>

Here left column instruction which is starting from `0x55ebd6a7366a` are memory addresses of instructions

Middle column are instructions `4883ec08`  encoded in bytes which is machine code.

Right column is the human readable instruction `subq $8, %rsp`

%rsp stack pointer (holds the recent memory address)
%rbp frame pointer (points to frame of function being executed)


## Simple Instruction Example

An assembly instruction looks like this

`movq $3 rax ` (movq for 64 bit)
`movl $3 rax`  (movl for 32 bit)

In assembly constatns are represented by this `$3` 

Here the instruction will move a value 3 into a register named rax.

To move value from register to register

`movq %rax %rbx` 


There are some more instructions in assebmly like

```
addq  (add instruction)
subq  (subtract instruction)
imulq (multiply instruction)
andq  (perform AND operation)
orq   (perform OR operation)
xorq  (perform XOR operation
```

## If Statements

if (x == 3 ):
	return 3
else:
	return 0	

Like we see in programming if else statements that have a conidition that needs to be true and if it's true what instruction it performs or if it's false what will it do so assembly it's something like this

`cmpq %rax %rbx` This will just compare the values of two registers

Now after we compare these values it would not do anything until we tell it what instruction is to be performed so we issue a `jump` instruction which can goto different part of code from a point where that instruction occurs

```
movq $10 rax
cmp %rax %rbx
je equal

equal:
```
What this block of instruction will do is assign `rax` register a value of 10

```
rax = 10
```
then will compare `rax` and `rbx` it would not do anything until we perform a jump compare (je equal) if they are equal

```
if rax == rbx

```

Then it will jump to next block instruction which we have named `equal` it's more like a function

So now let's do some room tasks

<img src="https://imgur.com/gxd5EtH.png"/>

I have loaded up the binary in `radare` 

<img src="https://imgur.com/c46VV9W.png"/>

Then selecting main function and adding two breakpoints with `db [instruction_memory_address]`

<img src="https://imgur.com/iq5owfW.png"/>

When we'll run the binary it will hit at the breakpoint and two see the instructions uptil that point we'll use `dr` command

<img src="https://imgur.com/iq5owfW.png"/>

Now for doing these tasks we have to use `if2` binary

<img src="https://imgur.com/2lb6H8e.png"/>

Now add a breakpoint at 

`0x55feb072c630      816dfce70300.  subl $0x3e7, var_4h`

```
db 0x55feb072c630 (this is before the return and pop instruction)
dc
px @ rbp-0x4
px @ rbp-0x8
```

1.  What is the value of var_8h before the popq and ret instructions?
	You'll get in the offset 60 which is in hex so after converting it to decimal it would be 

	<img src="https://imgur.com/0yfXHbr.png"/>

	<img src="https://imgur.com/tFQZx40.png"/>

    `96`

2.  what is the value of var_ch before the popq and ret instructions?

    We can see that only value 0 is assigned to `var_ch` and no further instructions and done on it until pop and return instruction
   
   `0`

3.  What is the value of var_4h before the popq and ret instructions?
	
	`1`
	
4. ` What operator is used to change the value of var_8h, input the symbol as your answer(symbols include +, -, *, /, &, |):`


```
0x55feb072c623      8365f864       andl $0x64, var_8h
```
`&`

## Loops


<img src="https://imgur.com/ufdEZDN.png"/>

<img src="https://imgur.com/tdbPULD.png"/>

<img src="https://imgur.com/3hBTWas.png"/>


1. What is the value of var_8h on the second iteration of the loop?
	`5`


2. What is the value of var_ch on the second iteration of the loop?
	`0`

<img src="https://imgur.com/62ObddX.png"/>

3. What is the value of var_8h at the end of the program?
	
	`2`

4. What is the value of var_ch at the end of the program?

	`0`


## Crackme 1

<img src="https://imgur.com/FFTp5S8.png"/>

<img src="https://imgur.com/luKIkrs.png"/>

Now we know the password is 127 in between you can see `.` and `.01` so by this it is referring to localhost which is 127.0.0.1

`127.0.0.1`


## Crackme 2

<img src="https://imgur.com/RcqRMI4.png"/>

Here we see a text file which being read form the binary on reading the file we see `vs3curepwd` but when entered it isn't the right password ,so I got stuck but through "reversing" the text that was the right password