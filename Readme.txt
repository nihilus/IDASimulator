IDASimulator is a plugin that extends IDA's conditional breakpoint support, making it easy to augment / replace complex executable code inside a debugged process with Python code.
Specifically, IDASimulator makes use of conditional breakpoints in the IDA debugger to hijack the execution flow of a process and invoke Python handler functions whenever particular code blocks are executed. With support for multiple target architectures, it handles details such as register initialization, memory allocation, pointers, function arguments and return values seamlessly and transparently, making it easy to replace, modify and subvert existing functionality (or lack thereof) in the target process.
IDASimulator also includes the IDASim python module, on which IDASimulator is based. This allows for all of the features of IDASimulator to be integrated into more complex IDAPython scripts.
IDASimulator currently supports the x86, x86_64, ARM and MIPS32 architectures. Porting to other architectures is very easy.
	
	Why?

** The ability to dynamically intercept, replace or modify process logic is useful in a variety of situations, such as:
** Monitoring function calls
** Non-intrusive function hooking
** Simulating library functions when emulating code snippets in IDA
** Simulating hardware-dependant functionality (embedded firmware, custom hardware, unsupported ioctl's, etc)
** Any situation where the application code does one thing and you want it to do something else

	Introduction

IDASimulator is a plugin that allows IDA users to easily augment / replace executable code inside a debugged process with Python code.
Specifically, IDASimulator makes use of conditional breakpoints in the IDA debugger to hijack the execution flow of a process and invoke Python handler functions whenever particular code blocks are executed. With support for multiple target architectures, it handles details such as register initialization, memory allocation, pointers, function arguments and return values seamlessly and transparently, making it easy to replace, modify and subvert existing functionality (or lack thereof) in the target process.
IDASimulator currently supports the x86, x86_64, ARM and MIPS32 architectures. Porting to other architectures is very easy.
Installation

The IDASimulator plugin and its associated IDASim python module can be installed with the install.py script:
$ python install.py /path/to/ida/install/directory
​
	Using IDASimulator

See DOCS

Thanks to Storm shadow keeping a copy of this!