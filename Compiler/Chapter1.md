# Chapter 1 Introduction

Programming languages are notations for describing computations to people and to machines

Before a program can be run, it first must be translated into a form in which it can be executed by a computer. The software systems that do this translation are called **compilers**

the book is about how to **design and implement** compilers

in this Chapter

- introduce the different forms of language translators
- give a high level overview of the structure of a typical compiler
- discuss the trends in programming languages and machine architecture that are shaping compilers
- include some observations on the relationship between compiler design and computer-science theory and an outline of the applications of compiler technology that go beyond compilation
- end with a brief outline of key programming-language concepts that will be needed for our study of compilers

## 1.1 Language Processors

a compiler is a program that can read a program in one language (the **source** language) and translate it into an equivalent program in another language (the **target** language)

an important role of the compiler is to **report any errors** in the source program that it detects during the translation process

- interpreter: (another kind of language processor) directly execute the operations specified in the source program on inputs supplied by the user
- compiler: produce a target program as a translation
- advantages: the machine-language target program produced by a compiler is usually much faster than an interpreter at mapping inputs to outputs; interpreter can usually give better error diagnostics than a compiler (because it executes the source program statement by statement)

the process of creating an executable target program

1. a source program may be divided into modules stored in separate files (the task of collecting the source program is sometimes entrusted to a separate program, called a **preprocessor**, which may also expand shorthands, called macros, into source language statements)
2. the modified source program is then fed to a compiler. The compiler may produce an assembly-language program as its output, because assembly language is easier to produce as output and is easier to debug
3. the assembly language is then processed by a program called an **assembler** that produces relocatable machine code as its output
4. large programs are often compiled in pieces, so the relocatable machine code may have to be linked together with other relocatable object files and library files into the code that actually runs on the machine. the **linker** resolves external memory addresses, where the code in one file may refer to a location in another files
5. the **loader** then puts together all of the executable object files into memory for execution

## 1.2 The Structure of a Compiler

## 1.3 The Evolution of Programming Languages

## 1.4 The Science of Building a Compiler

## 1.5 Applications of Compiler Technology

## 1.6 Programming Language Basics
