package routes

import (
	"customer-sales-backend/src/controllers"
	"customer-sales-backend/src/services"

	"github.com/gin-gonic/gin"
)

func setupRegionRoutes(router *gin.RouterGroup) {
	controller := controllers.RegionController{
		Service: services.RegionService,
	}

	router.GET("/regions/:id", controller.GetRegion)
	router.GET("/regions", controller.GetListRegions)
	router.POST("/regions", controller.CreateRegion)
	router.PATCH("/regions/:id", controller.UpdateRegion)
	router.DELETE("/regions/:id", controller.DeleteRegion)
}
