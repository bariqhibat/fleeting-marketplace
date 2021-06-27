package data

import (
	"fmt"
	"log"
	"os"
	"testing"
)

func TestNewRates(t *testing.T) {

	l := log.New(os.Stdout, "[test] currency", log.LstdFlags)

	tr, err := NewRates(l)

	if err != nil {
		t.Fatal(err)
	}

	fmt.Printf("%#v", tr.rates)

}
