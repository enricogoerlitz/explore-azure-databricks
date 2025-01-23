package controllers

import (
	"customer-sales-backend/src/libs/crud"
	"customer-sales-backend/src/models"
	"customer-sales-backend/src/services"

	"github.com/gin-gonic/gin"
)

type ProductController struct {
	Service services.ProductCRUDService
}

func (pc *ProductController) GetProduct(c *gin.Context) {
	id := c.Param("id")
	crud.HandleGet[models.ProductResponse](c, id, nil)
}

func (pc *ProductController) GetListProducts(c *gin.Context) {
	crud.HandleGetList[models.ProductResponse](c, pc.Service.CRUDService, nil)
}

func (pc *ProductController) CreateProduct(c *gin.Context) {
	crud.HandlePost[models.ProductPOST, models.ProductResponse](c, pc.Service.CRUDService)
}

func (pc *ProductController) UpdateProduct(c *gin.Context) {
	id := c.Param("id")
	crud.HandlePatch[models.ProductModel, models.ProductPATCH](c, pc.Service.CRUDService, id)
}

func (pc *ProductController) DeleteProduct(c *gin.Context) {
	id := c.Param("id")
	crud.HandleDelete[models.ProductModel](c, id)
}
