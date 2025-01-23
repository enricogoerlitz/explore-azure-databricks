package services

import (
	"customer-sales-backend/src/libs/crud"
)

type RegionCRUDService struct {
	*crud.CRUDService
}

var RegionService = RegionCRUDService{
	CRUDService: &crud.CRUDService{
		UniqueColumns:         []string{"Name"},
		UniqueColumnsTogether: [][]string{},
		ForeignKeyColumns:     []crud.ForeignKeyColumn{},
		ReadOnlyFields:        []string{},
		PaginationMaxPageSize: 100,
	},
}
