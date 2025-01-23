package routes

import (
	"customer-sales-backend/src/controllers"
	"customer-sales-backend/src/services"

	"github.com/gin-gonic/gin"
)

func setupProductRoutes(router *gin.RouterGroup) {
	controller := controllers.ProductController{
		Service: services.ProductService,
	}

	router.GET("/products/:id", controller.GetProduct)
	router.GET("/products", controller.GetListProducts)
	router.POST("/products", controller.CreateProduct)
	router.PATCH("/products/:id", controller.UpdateProduct)
	router.DELETE("/products/:id", controller.DeleteProduct)
}
