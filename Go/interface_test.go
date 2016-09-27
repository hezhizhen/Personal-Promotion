package main

import (
	"fmt"
)

// Animal interface
type Animal interface {
	Eat()
	Run()
}

// Dog struct
type Dog struct {
}

// Eat method
func (dog *Dog) Eat() {
	fmt.Println("I eat bone")
}

// Run method
func (dog *Dog) Run() {
	fmt.Println("I run very fast")
}

func main() {
	var a Animal
	a = &Dog{}
	a.Eat()
	a.Run()
}
