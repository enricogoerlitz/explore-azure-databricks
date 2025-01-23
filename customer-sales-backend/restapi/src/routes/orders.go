package routes

import (
	"customer-sales-backend/src/controllers"
	"customer-sales-backend/src/services"

	"github.com/gin-gonic/gin"
)

func setupOrderRoutes(router *gin.RouterGroup) {
	// Order routes
	orderController := controllers.OrderController{
		Service: services.OrderService,
	}

	router.GET("/orders/:id", orderController.GetOrder)
	router.GET("/orders", orderController.GetListOrders)
	router.POST("/orders", orderController.CreateOrder)
	router.PATCH("/orders/:id", orderController.UpdateOrder)
	router.DELETE("/orders/:id", orderController.DeleteOrder)

	// OrderItem routes
	orderItemcontroller := controllers.OrderItemController{
		Service: services.OrderItemService,
	}

	router.POST("/orders/:id/items", orderItemcontroller.CreateOrderItem)
	router.PATCH("/orders/:id/items/:item_id", orderItemcontroller.UpdateOrderItem)
	router.DELETE("/orders/:id/items/:item_id", orderItemcontroller.DeleteOrderItem)
}
