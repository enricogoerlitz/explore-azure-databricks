package controllers

import (
	"customer-sales-backend/src/libs/crud"
	"customer-sales-backend/src/models"
	"customer-sales-backend/src/services"

	"github.com/gin-gonic/gin"
)

type ProductCategoryController struct {
	Service services.ProductCategoryCRUDService
}

func (pcc *ProductCategoryController) GetProductCategory(c *gin.Context) {
	id := c.Param("id")
	crud.HandleGet[models.ProductCategoryResponse](c, id, nil)
}

func (pcc *ProductCategoryController) GetListProductCategories(c *gin.Context) {
	crud.HandleGetList[models.ProductCategoryResponse](c, pcc.Service.CRUDService, nil)
}

func (pcc *ProductCategoryController) CreateProductCategory(c *gin.Context) {
	crud.HandlePost[models.ProductCategoryPOST, models.ProductCategoryResponse](c, pcc.Service.CRUDService)
}

func (pcc *ProductCategoryController) UpdateProductCategory(c *gin.Context) {
	id := c.Param("id")
	crud.HandlePatch[models.ProductCategoryModel, models.ProductCategoryPATCH](c, pcc.Service.CRUDService, id)
}

func (pcc *ProductCategoryController) DeleteProductCategory(c *gin.Context) {
	id := c.Param("id")
	crud.HandleDelete[models.ProductCategoryModel](c, id)
}
