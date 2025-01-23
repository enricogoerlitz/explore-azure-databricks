package main

import (
	"customer-sales-backend/src/database"
	"customer-sales-backend/src/routes"
	"customer-sales-backend/src/utils"
	"os"

	"github.com/gin-gonic/gin"
	"github.com/sirupsen/logrus"
)

func main() {
	isRelease := os.Getenv("MODE") == "release"

	// Initialize the Gin router
	router := gin.Default()

	// Connect to the database
	database.ConnectDB()

	// Setup routes
	routes.SetupRoutes(router)

	// Release actions
	if isRelease {
		logrus.Info("Running in release mode")
		// gin.SetMode(gin.ReleaseMode)
		database.MigrateDBModels()
	} else {
		logrus.Info("Running in debug mode")
		database.MigrateDBModels()
		utils.ExecuteDebugingActions()
	}

	// Start the server
	router.Run("0.0.0.0:80")
}
