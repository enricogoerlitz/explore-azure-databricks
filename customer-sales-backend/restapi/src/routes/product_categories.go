package routes

import (
	"customer-sales-backend/src/controllers"
	"customer-sales-backend/src/services"

	"github.com/gin-gonic/gin"
)

func setupProductCategoryRoutes(router *gin.RouterGroup) {
	controller := controllers.ProductCategoryController{
		Service: services.ProductCategoryService,
	}

	router.GET("/product-categories/:id", controller.GetProductCategory)
	router.GET("/product-categories", controller.GetListProductCategories)
	router.POST("/product-categories", controller.CreateProductCategory)
	router.PATCH("/product-categories/:id", controller.UpdateProductCategory)
	router.DELETE("/product-categories/:id", controller.DeleteProductCategory)
}
