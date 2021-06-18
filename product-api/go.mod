module github.com/bariqhibat/fleeting-marketplace/product-api

go 1.16

require (
	github.com/bariqhibat/fleeting-marketplace/currency v0.0.0-20210618173354-ae707287b24c
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/go-playground/universal-translator v0.17.0 // indirect
	github.com/go-playground/validator v9.31.0+incompatible
	github.com/gorilla/handlers v1.5.1
	github.com/gorilla/mux v1.8.0
	github.com/leodido/go-urn v1.2.1 // indirect
	google.golang.org/grpc v1.38.0
	gopkg.in/go-playground/assert.v1 v1.2.1 // indirect
	gopkg.in/yaml.v3 v3.0.0-20200615113413-eeeca48fe776 // indirect
)

replace github.com/bariqhibat/fleeting-marketplace/currency => ../currency
