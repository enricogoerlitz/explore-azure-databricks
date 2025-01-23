package services

import (
	"customer-sales-backend/src/libs/crud"
)

type UserCRUDService struct {
	*crud.CRUDService
}

var UserService = UserCRUDService{
	CRUDService: &crud.CRUDService{
		UniqueColumns: []string{},
		UniqueColumnsTogether: [][]string{
			{"Firstname", "Lastname"},
		},
		ForeignKeyColumns:     []crud.ForeignKeyColumn{},
		ReadOnlyFields:        []string{},
		PaginationMaxPageSize: 100,
	},
}
