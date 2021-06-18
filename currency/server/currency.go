package server

import (
	"context"
	"log"

	protos "github.com/bariqhibat/fleeting-marketplace/currency/protos/currency"
)

type Currency struct {
	protos.UnimplementedCurrencyServer
	log *log.Logger
}

func NewCurrency(l *log.Logger) *Currency {
	return &Currency{log: l}
}

func (c *Currency) GetRate(ctx context.Context, rr *protos.RateRequest) (*protos.RateResponse, error) {
	c.log.Println("Handle GetRate")

	return &protos.RateResponse{Rate: 0.5, Base: rr.Base, Destination: rr.Destination}, nil
}
