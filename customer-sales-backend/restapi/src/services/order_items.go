package services

import (
	"customer-sales-backend/src/libs/crud"
	"customer-sales-backend/src/models"

	"github.com/gin-gonic/gin"
)

type OrderItemCRUDService struct {
	*crud.CRUDService
}

func (s *OrderItemCRUDService) HandlePost(c *gin.Context, orderID int) {
	var payload models.OrderItemPOST
	if err := c.ShouldBindJSON(&payload); err != nil {
		crud.HandlePayloadError(c, err)
		return
	}
	payload.OrderID = orderID

	crud.HandlePostCustomPayload[models.OrderItemPOST, models.OrderItemResponse](c, s.CRUDService, payload)
}

func (s *OrderItemCRUDService) HandlePatch(c *gin.Context, id int, orderID int) {
	var payload models.OrderItemPATCH
	if err := c.ShouldBindJSON(&payload); err != nil {
		crud.HandlePayloadError(c, err)
		return
	}
	payload.OrderID = orderID

	crud.HandlePatchCustomPayload[models.OrderItemResponse, models.OrderItemPATCH](c, s.CRUDService, id, payload)
}

var orderForeignKeyColumn = crud.ForeignKeyColumn{
	Model: &models.OrderModel{},
	Field: "OrderID",
}

var productForeignKeyColumn = crud.ForeignKeyColumn{
	Model: &models.ProductModel{},
	Field: "ProductID",
}

var OrderItemService = OrderItemCRUDService{
	CRUDService: &crud.CRUDService{
		UniqueColumns:         []string{},
		UniqueColumnsTogether: [][]string{},
		ForeignKeyColumns: []crud.ForeignKeyColumn{
			orderForeignKeyColumn,
			productForeignKeyColumn,
		},
		ReadOnlyFields:        []string{},
		PaginationMaxPageSize: 100,
	},
}
