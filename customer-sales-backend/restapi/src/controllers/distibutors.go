package controllers

import (
	"customer-sales-backend/src/libs/crud"
	"customer-sales-backend/src/models"
	"customer-sales-backend/src/services"

	"github.com/gin-gonic/gin"
)

type DistributorController struct {
	Service services.DistributorCRUDService
}

func (dc *DistributorController) GetDistributor(c *gin.Context) {
	id := c.Param("id")
	crud.HandleGet[models.DistributorResponse](c, id, nil)
}

func (dc *DistributorController) GetListDistributors(c *gin.Context) {
	crud.HandleGetList[models.DistributorResponse](c, dc.Service.CRUDService, nil)
}

func (dc *DistributorController) CreateDistributor(c *gin.Context) {
	crud.HandlePost[models.DistributorPOST, models.DistributorResponse](c, dc.Service.CRUDService)
}

func (dc *DistributorController) UpdateDistributor(c *gin.Context) {
	id := c.Param("id")
	crud.HandlePatch[models.DistributorModel, models.DistributorPATCH](c, dc.Service.CRUDService, id)
}

func (dc *DistributorController) DeleteDistributor(c *gin.Context) {
	id := c.Param("id")
	crud.HandleDelete[models.DistributorModel](c, id)
}
