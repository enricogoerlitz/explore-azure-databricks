package services

import (
	"customer-sales-backend/src/database"
	"customer-sales-backend/src/libs/crud"
	"customer-sales-backend/src/models"

	"github.com/gin-gonic/gin"
)

type OrderCRUDService struct {
	*crud.CRUDService
}

func (s *OrderCRUDService) HandleGet(c *gin.Context, id interface{}) {
	isDetailRoute := c.Query("detail") == "true"

	if isDetailRoute {
		dbQuery := database.DB.Preload("Region").Preload("User").Preload("OrderItems")
		crud.HandleGet[models.OrderResponseDetail](c, id, dbQuery)
	} else {
		crud.HandleGet[models.OrderResponse](c, id, nil)
	}
}

func (s *OrderCRUDService) HandleGetList(c *gin.Context) {
	isDetailRoute := c.Query("detail") == "true"

	if isDetailRoute {
		dbQuery := database.DB.Preload("Region").Preload("User").Preload("OrderItems")
		crud.HandleGetList[models.OrderResponseDetail](c, s.CRUDService, dbQuery)
	} else {
		crud.HandleGetList[models.OrderResponse](c, s.CRUDService, nil)
	}
}

var userForeignKeyColumn = crud.ForeignKeyColumn{
	Model: &models.UserModel{},
	Field: "UserID",
}

var regionForeignKeyColumn = crud.ForeignKeyColumn{
	Model: &models.RegionModel{},
	Field: "DestinationRegionID",
}

var OrderService = OrderCRUDService{
	CRUDService: &crud.CRUDService{
		UniqueColumns:         []string{},
		UniqueColumnsTogether: [][]string{},
		ForeignKeyColumns: []crud.ForeignKeyColumn{
			userForeignKeyColumn,
			regionForeignKeyColumn,
		},
		ReadOnlyFields:        []string{},
		PaginationMaxPageSize: 100,
	},
}
