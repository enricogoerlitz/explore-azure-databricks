package controllers

import (
	"customer-sales-backend/src/libs/crud"
	"customer-sales-backend/src/models"
	"customer-sales-backend/src/services"
	"fmt"
	"strconv"

	"github.com/gin-gonic/gin"
)

type OrderItemController struct {
	Service services.OrderItemCRUDService
}

func (oic *OrderItemController) CreateOrderItem(c *gin.Context) {
	orderID, _ := strconv.Atoi(c.Param("id"))
	oic.Service.HandlePost(c, orderID)
}

func (oic *OrderItemController) UpdateOrderItem(c *gin.Context) {
	id, idErr := strconv.Atoi(c.Param("item_id"))
	orderID, orderIDErr := strconv.Atoi(c.Param("id"))

	if idErr != nil || orderIDErr != nil {
		crud.HandleBadRequest(c, fmt.Errorf(":id and :item_id should be datatype of int"))
		return
	}

	oic.Service.HandlePatch(c, id, orderID)
}

func (oic *OrderItemController) DeleteOrderItem(c *gin.Context) {
	id := c.Param("item_id")
	crud.HandleDelete[models.OrderItemModel](c, id)
}
