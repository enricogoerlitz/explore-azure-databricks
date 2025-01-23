package routes

import (
	"customer-sales-backend/src/controllers"
	"customer-sales-backend/src/services"

	"github.com/gin-gonic/gin"
)

func setupUserRoutes(router *gin.RouterGroup) {
	controller := controllers.UserController{
		Service: services.UserService,
	}

	router.GET("/users/:id", controller.GetUser)
	router.GET("/users", controller.GetListUsers)
	router.POST("/users", controller.CreateUser)
	router.PATCH("/users/:id", controller.UpdateUser)
	router.DELETE("/users/:id", controller.DeleteUser)
}
