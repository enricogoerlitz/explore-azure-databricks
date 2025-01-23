package controllers

import (
	"customer-sales-backend/src/libs/crud"
	"customer-sales-backend/src/models"
	"customer-sales-backend/src/services"

	"github.com/gin-gonic/gin"
)

type RegionController struct {
	Service services.RegionCRUDService
}

func (rc *RegionController) GetRegion(c *gin.Context) {
	id := c.Param("id")
	crud.HandleGet[models.RegionResponse](c, id, nil)
}

func (rc *RegionController) GetListRegions(c *gin.Context) {
	crud.HandleGetList[models.RegionResponse](c, rc.Service.CRUDService, nil)
}

func (rc *RegionController) CreateRegion(c *gin.Context) {
	crud.HandlePost[models.RegionPOST, models.RegionResponse](c, rc.Service.CRUDService)
}

func (rc *RegionController) UpdateRegion(c *gin.Context) {
	id := c.Param("id")
	crud.HandlePatch[models.RegionModel, models.RegionPATCH](c, rc.Service.CRUDService, id)
}

func (rc *RegionController) DeleteRegion(c *gin.Context) {
	id := c.Param("id")
	crud.HandleDelete[models.RegionModel](c, id)
}
