package services

import (
	"customer-sales-backend/src/libs/crud"
)

type DistributorCRUDService struct {
	*crud.CRUDService
}

var DistributorService = DistributorCRUDService{
	CRUDService: &crud.CRUDService{
		UniqueColumns:         []string{"Name"},
		UniqueColumnsTogether: [][]string{},
		ForeignKeyColumns:     []crud.ForeignKeyColumn{},
		ReadOnlyFields:        []string{},
		PaginationMaxPageSize: 100,
	},
}
