package services

import (
	"customer-sales-backend/src/libs/crud"
)

type ProductCategoryCRUDService struct {
	*crud.CRUDService
}

var ProductCategoryService = ProductCategoryCRUDService{
	CRUDService: &crud.CRUDService{
		UniqueColumns:         []string{"Name"},
		UniqueColumnsTogether: [][]string{},
		ForeignKeyColumns:     []crud.ForeignKeyColumn{},
		ReadOnlyFields:        []string{},
		PaginationMaxPageSize: 100,
	},
}
