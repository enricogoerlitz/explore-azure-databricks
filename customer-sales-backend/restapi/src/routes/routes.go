package routes

import (
	"github.com/gin-gonic/gin"
	"github.com/sirupsen/logrus"
)

var API_PREFIX = "/api"

func SetupRoutes(router *gin.Engine) {
	logrus.Info("Setting up V1 routes")

	apiV1 := router.Group(API_PREFIX + "/v1")
	{
		setupDistributorRoutes(apiV1)
		setupOrderRoutes(apiV1)
		setupRegionRoutes(apiV1)
		setupProductCategoryRoutes(apiV1)
		setupProductRoutes(apiV1)
		setupUserRoutes(apiV1)
	}
}
