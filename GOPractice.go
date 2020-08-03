package main

import (
	"fmt"
	"time"
)
func Test(thing ... int){
	for i := range thing{
		fmt.Println(thing[i])
	}
}

func main(){
	fn := func() string{
		return "Hello"
	}
	fmt.Println(fn())
	fmt.Println("hello world")
	Test(1,2,3,4,5,6,7,8)
	x := map[string]string {
		"1":"Trevor",
		"2":"Cardoza",
	}
	fmt.Println(x)
	const pi float32 = 3.14
	fmt.Println(pi)
	var a [5]int
	a[2] = 100
	fmt.Println(a[2])
	
	for j := 7; j <= 9; j++ {
		fmt.Println(pi+ float32(j))
	}	
	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("It's the weekend")
	default:
		fmt.Println("It's a weekday")
	}
}