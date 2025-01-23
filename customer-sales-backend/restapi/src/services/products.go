package services

import (
	"customer-sales-backend/src/libs/crud"
	"customer-sales-backend/src/models"
)

type ProductCRUDService struct {
	*crud.CRUDService
}

var categoryForeignKeyColumn = crud.ForeignKeyColumn{
	Model: &models.ProductCategoryModel{},
	Field: "CategoryID",
}

var distributorForeignKeyColumn = crud.ForeignKeyColumn{
	Model: &models.DistributorModel{},
	Field: "DistributorID",
}

var ProductService = ProductCRUDService{
	CRUDService: &crud.CRUDService{
		UniqueColumns:         []string{"Name"},
		UniqueColumnsTogether: [][]string{},
		ForeignKeyColumns: []crud.ForeignKeyColumn{
			categoryForeignKeyColumn,
			distributorForeignKeyColumn,
		},
		ReadOnlyFields:        []string{},
		PaginationMaxPageSize: 100,
	},
}
