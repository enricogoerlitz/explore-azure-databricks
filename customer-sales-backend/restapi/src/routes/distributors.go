package routes

import (
	"customer-sales-backend/src/controllers"
	"customer-sales-backend/src/services"

	"github.com/gin-gonic/gin"
)

func setupDistributorRoutes(router *gin.RouterGroup) {
	controller := controllers.DistributorController{
		Service: services.DistributorService,
	}

	router.GET("/distributors", controller.GetListDistributors)
	router.GET("/distributors/:id", controller.GetDistributor)
	router.POST("/distributors", controller.CreateDistributor)
	router.PATCH("/distributors/:id", controller.UpdateDistributor)
	router.DELETE("/distributors/:id", controller.DeleteDistributor)
}
