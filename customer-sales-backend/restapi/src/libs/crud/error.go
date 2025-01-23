package crud

import (
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/sirupsen/logrus"
	"gorm.io/gorm"
)

func HandleDatabaseNotFound(c *gin.Context, err error) error {
	if err == gorm.ErrRecordNotFound {
		c.JSON(http.StatusNotFound, gin.H{"error": "Record not found"})
		return nil
	}

	HandleInternalServerError(c, err)
	return err
}

func HandleInternalServerError(c *gin.Context, err error) error {
	logrus.Error(err.Error())
	c.JSON(http.StatusInternalServerError, gin.H{"error": "Unexpected error"})
	return err
}

func HandlePayloadError(c *gin.Context, err error) error {
	logrus.Debug(err.Error())
	c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid payload"})
	return err
}

func HandleBadRequest(c *gin.Context, err error) error {
	logrus.Debug(err.Error())
	c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
	return err
}
