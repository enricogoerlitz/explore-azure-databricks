package controllers

import (
	"customer-sales-backend/src/libs/crud"
	"customer-sales-backend/src/models"
	"customer-sales-backend/src/services"

	"github.com/gin-gonic/gin"
)

type UserController struct {
	Service services.UserCRUDService
}

func (uc *UserController) GetUser(c *gin.Context) {
	id := c.Param("id")
	crud.HandleGet[models.UserResponse](c, id, nil)
}

func (uc *UserController) GetListUsers(c *gin.Context) {
	crud.HandleGetList[models.UserResponse](c, uc.Service.CRUDService, nil)
}

func (uc *UserController) CreateUser(c *gin.Context) {
	// handle different because of the password. but not important for this project!
	crud.HandlePost[models.UserPOST, models.UserResponse](c, uc.Service.CRUDService)
}

func (uc *UserController) UpdateUser(c *gin.Context) {
	id := c.Param("id")
	crud.HandlePatch[models.UserModel, models.UserPATCH](c, uc.Service.CRUDService, id)
}

func (uc *UserController) DeleteUser(c *gin.Context) {
	id := c.Param("id")
	crud.HandleDelete[models.UserModel](c, id)
}
