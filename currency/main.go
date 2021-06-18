package main

import (
	"log"
	"net"
	"os"

	protos "github.com/bariqhibat/fleeting-marketplace/currency/protos/currency"
	"github.com/bariqhibat/fleeting-marketplace/currency/server"
	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
)

func main() {
	log := log.New(os.Stdout, "currency ", log.LstdFlags)

	gs := grpc.NewServer()
	c := server.NewCurrency(log)

	protos.RegisterCurrencyServer(gs, c)

	reflection.Register(gs)

	l, err := net.Listen("tcp", ":9092")

	if err != nil {
		log.Println("[ERROR] Unable to listen")
	}

	gs.Serve(l)
}
