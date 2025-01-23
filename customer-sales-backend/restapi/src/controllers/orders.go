package controllers

import (
	"customer-sales-backend/src/libs/crud"
	"customer-sales-backend/src/models"
	"customer-sales-backend/src/services"

	"github.com/gin-gonic/gin"
)

type OrderController struct {
	Service services.OrderCRUDService
}

func (oc *OrderController) GetOrder(c *gin.Context) {
	id := c.Param("id")
	oc.Service.HandleGet(c, id)
}

func (oc *OrderController) GetListOrders(c *gin.Context) {
	oc.Service.HandleGetList(c)
}

func (oc *OrderController) CreateOrder(c *gin.Context) {
	crud.HandlePost[models.OrderPayloadPOST, models.OrderResponse](c, oc.Service.CRUDService)
}

func (oc *OrderController) UpdateOrder(c *gin.Context) {
	id := c.Param("id")
	crud.HandlePatch[models.OrderModel, models.OrderPayloadPATCH](c, oc.Service.CRUDService, id)
}

func (oc *OrderController) DeleteOrder(c *gin.Context) {
	id := c.Param("id")
	crud.HandleDelete[models.OrderModel](c, id)
}
